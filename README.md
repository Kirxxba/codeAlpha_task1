# Data Redundancy Removal System

## Project Overview
The Data Redundancy Removal System identifies duplicate email records and prevents duplicate entries from being stored in an SQLite database.

## Objectives
- Validate user input.
- Detect duplicate email addresses.
- Store unique records in an SQLite database.
- Display saved records through a web interface.

## Technologies Used
- Python 3.13
- Flask
- SQLite
- HTML
- CSS

## Features
- Add new records.
- Validate email input.
- Detect duplicate email addresses.
- Display saved records.
- Show the total number of unique records.

## Project Files
- `main.py` - Command-line version.
- `app.py` - Flask web application.
- `data.db` - SQLite database created when the application runs.

## How to Run

1. Install Python.
2. Install Flask:

   `python -m pip install flask`

3. Open the project folder in the terminal.
4. Run the application:

   `python app.py`

5. Open `http://127.0.0.1:5000` in your browser.

## Testing
- Add a new email address and verify that it is saved.
- Submit the same email address again and verify that the duplicate is rejected.
- Check the saved records table.

## Current Status
Local prototype implemented and duplicate-email detection tested.

## Future Improvements
- Deploy to a cloud platform.
- Add stronger input validation.
- Add authentication and access control.
- Add automated tests.
-