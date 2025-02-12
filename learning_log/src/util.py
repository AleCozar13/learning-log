'''
Dependencies
'''


def readpath(environment, filename):
    '''
    Get the directory of current Python script and append filename,
    Obtain .yml conf
    '''
    import os
    import logging

    filepath = os.path.join(os.path.dirname(__file__),
                            filename % environment)
    logging.info("Filepath: %s", filepath)

    return filepath


def dataframe_to_s3(dataframe, parquet_file_key):
    '''
    Takes a df, its format and uploads it to S3 bucket
    '''
    import awswrangler as wr
    import logging
    try:
        wr.s3.to_parquet(
            df=dataframe, path=parquet_file_key,
            index=False, dataset=True
        )
        logging.info("Succesfull DatafFrame upload to S3")

    except Exception as e:
        logging.error("Can't upload Dataframe to S3 due to %s", e)


def execute_query_athena(query, database):
    '''Execute a SQL query on Athena database, returns a df'''
    import awswrangler as wr

    return wr.athena.read_sql_query(
        sql=query,
        database=database,
        ctas_approach=False,
        s3_output='s3://imaginaenergia-datalake/athena-query-results/',
        workgroup='datalake'
        )


def get_property(file_path, section, property_name):
    '''
    Read configuration file using configparser module
    and retrieves a specific property
    '''
    import configparser

    config_parser = configparser.RawConfigParser()
    config_parser.read(file_path)

    default_value = config_parser.get('DEFAULT', property_name, fallback="")
    property_value = config_parser.get(section, property_name,
                                       fallback=default_value)

    if not property_value:
        raise ValueError(
            f'Error reading `{property_name}` in section `{section}` in file `{file_path}`')

    return property_value


def export_dynamodb(bucket_name, table_name, table_arn, prefix):
    '''
    Create an export of DynamoDB tables in S3, also get the Earliest
    recoverable timestamp and transform to desired format
    '''
    import boto3
    import logging
    import time

    # First create the DynamoDB export for tables
    # Initialize dynamodb client
    dynamodb = boto3.client('dynamodb')

    # PITR date EarliestRestorableDateTime, from describe_continuous_backups
    response = dynamodb.describe_continuous_backups(TableName=table_name)
    # Check if continuous backups and PITR are enabled
    if response['ContinuousBackupsDescription'][
        'PointInTimeRecoveryDescription'][
            'PointInTimeRecoveryStatus'] == 'ENABLED':
        # Get the earliest and latest recoverable timestamps
        earliest_datetime = response['ContinuousBackupsDescription'][
            'PointInTimeRecoveryDescription']['EarliestRestorableDateTime']
        latest_datetime = response['ContinuousBackupsDescription'][
            'PointInTimeRecoveryDescription']['LatestRestorableDateTime']

        logging.info("Earliest recoverable timestamp: %s", earliest_datetime)
        logging.info("Latest recoverable timestamp: %s", latest_datetime)
    else:
        logging.info("Point-in-Time Recovery is not enabled for %s table",
                     table_name)

    # Convert datetime object to desired datetime format
    # earliest_datetime = earliest_datetime.strftime('%Y-%m-%d %H:%M:%S%z')
    latest_datetime = latest_datetime.strftime('%Y-%m-%d %H:%M:%S%z')

    # Create the DynamoDB export to S3
    response = dynamodb.export_table_to_point_in_time(
        TableArn=table_arn,
        ExportTime=latest_datetime,
        S3Bucket=bucket_name,
        S3Prefix=prefix,
        S3SseAlgorithm='AES256',
        ExportFormat='DYNAMODB_JSON'
    )
    export_arn = response['ExportDescription']['ExportArn']
    # Continuously check the status of the export operation
    while True:
        try:
            export_status = dynamodb.describe_export(
                ExportArn=export_arn)['ExportDescription']['ExportStatus']
            if export_status == 'IN_PROGRESS':
                logging.info("Export is in progress.")
                print("Export is in progress.")
            elif export_status == 'COMPLETED':
                logging.info("Export completed.")
                print("Export completed.")
                break  # Exit the loop once export is completed
            else:
                logging.info("Export failed or has another status.")
                print("Export failed or has another status.")

            # Wait for a few seconds before checking again
            time.sleep(60)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break


def retrieve_jsonZip_transform_dataframe(bucket_name, export_prefix,
                                         columns, new_colums):
    '''
    Explain here...
    '''
    from datetime import datetime
    import io
    import gzip
    import json
    import boto3
    import pandas as pd

    # Initialize S3 client to get the file_key_path extraction
    s3 = boto3.client('s3')

    # List objects in the specified path
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=export_prefix)

    # Find file with ending .json.gz
    file_key_path = [obj['Key'] for obj in response['Contents']
                     if obj['Key'].endswith('.json.gz')]

    # Retrieve file
    response = s3.get_object(Bucket=bucket_name, Key=file_key_path[0])

    # Read the content of the gzip file
    gzip_content = response['Body'].read()

    # Decompress the gzip content
    with gzip.GzipFile(fileobj=io.BytesIO(gzip_content)) as f:
        json_content = f.read().decode('utf-8')

    # Transform json_content into the desired dataframe
    # Parse JSON data and extract values for specified columns
    values = []
    for line in json_content.split('\n'):
        if line:
            data = json.loads(line)
            item = data.get("Item")
            values.append([item.get(column, {}).get("S", "")
                           for column in columns])

    # Create DataFrame and rename columns
    df = pd.DataFrame(values, columns=columns)
    df.rename(columns=new_colums, inplace=True)

    return df


def delete_objectS3(bucket_name, export_prefix):
    '''
    Explain here...
    '''
    import boto3
    import logging
    # Initialize S3 client to get the file_key_path extraction
    s3 = boto3.client('s3')
    # List objects in the specified path
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=export_prefix)
    objects = [{'Key': obj['Key']} for obj in response['Contents']]

    # Delete objects
    try:
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})
        logging.info("Delete objects completed")
        print("Delete objects completed")
    except Exception as e:
        logging.warning("Problem with delete, %s", e)


def get_dataframe_s3(path):
    '''
    Read Parquet file stored on S3, returns a df
    '''
    import awswrangler as wr
    from awswrangler.exceptions import NoFilesFound

    try:
        return wr.s3.read_parquet(path=path, dataset=True)
    except NoFilesFound:
        print(f"No files found on: {path}. Returning None.")
        return None
    except Exception as e:
        print(f"Error occurred while reading Parquet file: {e}")
        return None


def get_xls_to_dataframe_s3(path):
    '''
    Read xlsx file stored on S3 and return a dataframe.
    '''
    import awswrangler as wr
    from awswrangler.exceptions import NoFilesFound

    try:
        return wr.s3.read_excel(path=path, engine='openpyxl')
    except NoFilesFound:
        print(f"No files found on: {path}. Returning None.")
        return None
    except Exception as e:
        print(f"Error occurred while reading file: {e}")
        return None
