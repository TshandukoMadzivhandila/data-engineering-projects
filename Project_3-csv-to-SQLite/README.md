# InstructorDB Manager

A lightweight ETL (Extract, Transform, Load) Python project that reads instructor data from a CSV file, loads it into an SQLite database, runs SQL queries, and appends new data—all using `pandas` and `sqlite3`.

---

## Features

- **Extract**: Reads instructor data from a CSV file
- **Transform**: Applies column headers and formats data using pandas
- **Load**: Loads the data into a SQLite database
- **Querying**:
  - Display all records
  - Select specific columns
  - Count total rows
- **Append**: Adds a new instructor record and shows updated row count

---

## ETL Process

This script follows a basic ETL flow:

| Step       | Action                                        |
|------------|-----------------------------------------------|
| **Extract**| Load CSV data using `pandas.read_csv()`       |
| **Transform**| Apply column names, format data (minimal)   |
| **Load**   | Save to SQLite using `to_sql()`               |

---

## File Structure

Project_3-csv-to-SQLite/
│
├── manage_instructor_data.py # Main script
│├──data/
│    ├── INSTRUCTOR.csv # Input CSV file (must exist)
├── STAFF.db # SQLite database (created by script)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── screenshots/ # Query output images
├── query1_all_rows.png
├── query2_fname_column.png
├── query3_row_count.png
└── query4_row_count_after_append.png


---

## Requirements

- Python 3.x
- pandas

Install the required library with:

```bash
pip install pandas
Usage
Ensure INSTRUCTOR.csv is in your project folder and contains five fields per row in this order:

ID,FNAME,LNAME,CITY,CCODE
Run the script:

python manage_instructor_data.py
The script will:

Load CSV data into STAFF.db

Run SQL queries and display output

Append a new instructor and re-display the updated row count

Query Output Screenshots
1. Display All Rows
All Rows

2. Display Only First Names
First Names

3. Count of Total Rows (Before Append)
Row Count

4. Count of Total Rows (After Append)
Row Count After Append

Notes
The script will overwrite the table if it already exists (if_exists='replace').

The database STAFF.db and the table INSTRUCTOR are created automatically.
