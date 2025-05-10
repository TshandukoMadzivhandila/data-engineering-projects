# Instructor Data Manager with SQLite and Pandas

This project demonstrates how to use Python with `pandas` and `sqlite3` to manage instructor data. The script reads a CSV file, loads it into a SQLite database, performs queries, appends a new row, and shows the updated results.

---

## Features

- Loads instructor data from a CSV file
- Creates a SQLite database and table (`INSTRUCTOR`)
- Performs basic SQL queries:
  - Display all rows
  - Select specific columns
  - Count total rows
- Appends a new instructor record
- Recounts and displays the updated number of rows

---

## Project Structure

Project 2, Web scraping etl/
│
├── etl.py # Main script
├── README.md # Project documentation
└── INSTRUCTOR.csv # Input CSV file (you must provide this)


---

## Requirements

- Python 3.x
- `pandas` library

Install pandas using pip if needed:

```bash
pip install pandas
Usage
Place your INSTRUCTOR.csv file in the project directory.

Run the script:

python etl.py
The script will:

Create (or overwrite) a SQLite database called STAFF.db

Create a table named INSTRUCTOR

Load the data into the table

Print query results

Append a new instructor row

Print the updated row count

Data Source
Input CSV: INSTRUCTOR.csv

The file is expected to have no header and five columns in this order:

ID

FNAME

LNAME

CITY

CCODE
