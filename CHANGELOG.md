# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),

## [0.1.2] 2024-09-11

### Changed

- `models.py` - Define a model for the kinds of entries user can make in their learning logs.

### Added
- `admin.py` - Admin site registrer.

## [0.1.0] 2024-09-11

### Changed

- `models.py` - Add class Topic.
- `settings.py` - Add the app `learning_logs`.

### Added

- `CHANGELOG.md`
- `poetry.lock`, `pyproject.toml` - Start poetry, creates virtual env where Django where installed.
- `ll_project` - Folder with necessary files to deploy the app to a server:
    - `__init__.py`
    - `asgi.py`
    - `settings.py` - Control how Django interacts with the system and manages the project.
    - `urls.py` - Tells Django which pages to build in response to browser requests.
    - `wsgi.py` - Helps Django serve the files it creates (Web Server Gateway Interface).
- `manage.py` - Short program that takes in commands and feed them to the relevant part of Django.
- `db.sqlite3` - Database file sqlite type.
- `learning_logs` - Folder with the infrastructure needed to build the app.
    - `__init__.py`
    - `admin.py`
    - `tests.py`
    - `apps.py`
    - `models.py` - Define the data we want to manage in our app.
    - `views.py`
    - `migrations` - Store information about the model.