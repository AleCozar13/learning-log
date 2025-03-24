# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [0.3.0] - 2025-03-24

### Added
- Configured deployment to **Platform.sh**.
- Added necessary configuration files for **Platform.sh** deployment.
- Updated settings to support production environment.

### Changed
- Adjusted database settings to align with **Platform.sh** environment.
- Modified static file handling to work with the deployment setup.


## [0.2.0] - 2025-03-23

### Changed

- `learning_logs/templates/ all templates` - Rewrite using Bootstrap template
- `accounts/templates/login.html` - Rewrite using Bootstrap template


### Added
- Integrated Django - Bootstrap5 for improved UI styling and responsiveness.
- Updated templates to use Bootstrap components and grid system.

- `ll_project/settings.py` - Third party apps.


## [0.1.3] - 2025-03-23

### Changed
- `learning_logs/views.py` - Added @login_required decorator also showing users only the topics that belong to them
- `ll_project/settings.py` - Implement log in to see, create, edit topics and entries


## [0.1.2] - 2025-03-23

### Added
- `learning_logs/templates/learning_logs/topics.html` - Added "New Topic" button.
- `learning_logs/templates/learning_logs/new_topic.html` - Created HTML template for the "New Topic" page.
- `learning_logs/templates/learning_logs/edit_entry.html` - Created HTML template for the "Edit Entry" page.
- `learning_logs/urls.py` - Defined URL patterns for creating a new topic, adding a new entry, and editing an entry.
- `learning_logs/forms.py` - Created forms for the `Topic` and `Entry` models.

- `accounts` - New app, contains all related to work with users.

## [0.1.1] - 2025-02-16

### Changed
- `ll_project/urls.py` - Added `learning_logs.urls.py` to the project.
- `views.py` - Set up views for the home page and topics page.
- `models.py` - Added `Topic` and `Entry` models.
- `ll_project/settings.py` - Registered `learning_logs` as an installed app.

### Added
- `learning_logs/urls.py` - Defined URL pattern for the home page.
- `learning_logs/templates/learning_logs/base.html` - Base HTML template.
- `learning_logs/templates/learning_logs/index.html` - Home page HTML template.
- `learning_logs/templates/learning_logs/topics.html` - Topics page HTML template.
- `learning_logs/templates/learning_logs/topic.html` - Specific topic page HTML template.
- `admin.py` - Registered models in the Django admin site.

## [0.1.0] - 2025-02-14

### Added
- `CHANGELOG.md` - Created this changelog file.
- `poetry.lock`, `pyproject.toml` - Initialized Poetry for dependency management and created a virtual environment where Django was installed.
- `ll_project/` - Project folder containing necessary files for deployment:
  - `__init__.py`
  - `asgi.py`
  - `settings.py` - Configured Django project settings.
  - `urls.py` - Defined URL routing for the project.
  - `wsgi.py` - Web Server Gateway Interface for serving Django applications.
- `manage.py` - Command-line utility for managing the Django project.
- `db.sqlite3` - SQLite database file.
- `learning_logs/` - Folder containing the core app structure:
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py` - Defined the `Topic` and `Entry` models.
  - `views.py`
  - `tests.py`
  - `migrations/` - Stores migration history for database changes.

## [0.1.1] - 2025-02-16

### Changed
- `ll_project/urls.py` - Added `learning_logs.urls.py` to the project.
- `views.py` - Set up views for the home page and topics page.
- `models.py` - Added `Topic` and `Entry` models.
- `settings.py` - Registered `learning_logs` as an installed app.

### Added
- `learning_logs/urls.py` - Defined URL pattern for the home page.
- `learning_logs/templates/learning_logs/base.html` - Base HTML template.
- `learning_logs/templates/learning_logs/index.html` - Home page HTML template.
- `learning_logs/templates/learning_logs/topics.html` - Topics page HTML template.
- `learning_logs/templates/learning_logs/topic.html` - Specific topic page HTML template.
- `admin.py` - Registered models in the Django admin site.

## [0.1.0] - 2025-02-14

### Added
- `CHANGELOG.md` - Created this changelog file.
- `poetry.lock`, `pyproject.toml` - Initialized Poetry for dependency management and created a virtual environment where Django was installed.
- `ll_project/` - Project folder containing necessary files for deployment:
  - `__init__.py`
  - `asgi.py`
  - `settings.py` - Configured Django project settings.
  - `urls.py` - Defined URL routing for the project.
  - `wsgi.py` - Web Server Gateway Interface for serving Django applications.
- `manage.py` - Command-line utility for managing the Django project.
- `db.sqlite3` - SQLite database file.
- `learning_logs/` - Folder containing the core app structure:
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py` - Defined the `Topic` and `Entry` models.
  - `views.py`
  - `tests.py`
  - `migrations/` - Stores migration history for database changes.