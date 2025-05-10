# Multi-Source ETL Project

This project implements an **ETL (Extract, Transform, Load)** pipeline that extracts data from multiple sources (CSV, JSON, and XML files), transforms the data by converting height (in inches) to meters and weight (in pounds) to kilograms, and loads the transformed data into a CSV file.

## Project Structure

multi-source-etl/
├── data/ # Input data files (CSV, JSON, XML)
│ ├── sample1.csv
│ ├── sample2.json
│ └── sample3.xml
├── logs/ # Log file for ETL process
│ └── log_file.txt
├── output/ # Transformed output data
│ └── transformed_data.csv
├── etl.py # Main ETL script
├── README.md # Project description and instructions
├── requirements.txt # Python dependencies
└── .gitignore # Files and folders to ignore in git


## Description

The **Multi-Source ETL** project performs the following operations:

1. **Extract**: Reads data from multiple input sources:
   - CSV files (`data/*.csv`)
   - JSON files (`data/*.json`)
   - XML files (`data/*.xml`)

2. **Transform**: Converts height from inches to meters and weight from pounds to kilograms.

3. **Load**: Saves the transformed data to a CSV file (`output/transformed_data.csv`).

4. **Log**: Logs the progress of the ETL process into `logs/log_file.txt`.

## Requirements

To run this project, you need to install the required Python packages. You can install them by running:

```bash
pip install -r requirements.txt
Installation
Clone or download this repository to your local machine.

Install dependencies:

pip install -r requirements.txt
Put your input files (CSV, JSON, and XML) in the data/ folder.

Run the ETL script:

python etl.py
After the script finishes running, the transformed data will be saved in the output/ folder as transformed_data.csv.

Example of Data Flow
Extract: Data is read from files like sample1.csv, sample2.json, and sample3.xml.

Transform: Heights (in inches) are converted to meters, and weights (in pounds) are converted to kilograms.

Load: The transformed data is saved to output/transformed_data.csv.

Logs
The progress of each step (Extract, Transform, Load) is logged to logs/log_file.txt. This file records the time and status of each phase.
