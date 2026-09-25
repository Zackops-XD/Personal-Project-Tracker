# Personal Project & Assignment Tracker

A Flask-based web application for managing personal projects and assignments.

## Features

* Create projects
* Edit projects
* Delete projects
* View project details
* Track project status
* Track project priority
* Track deadlines
* Dashboard with deadline urgency
* Search projects
* Filter projects by status
* Filter projects by priority
* Automatic deadline ordering
* Reset filters
* Delete confirmation

## Tech Stack

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript

## Project Structure

```text
Personal-Project-Tracker/
├── app.py
├── database.py
├── templates/
├── static/
├── test_database.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Personal-Project-Tracker
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

Start the Flask application:

```bash
python app.py
```

Then open the local address provided by Flask in your browser.

The SQLite database will be created automatically when the application is initialized.

## Database

The project uses SQLite for local data storage.

The database file (`tracker.db`) is intentionally excluded from Git using `.gitignore`.

This keeps personal project data out of the repository.

## Version

**Version 1.0**

This version contains the core project management functionality.

## Future Development

Planned improvements for future versions include:

* Project tags
* Tag management
* Tag filtering
* Additional dashboard statistics
* AI-assisted project management
* External messaging integration
