import os

import glob

import pandas as pd

import xml.etree.ElementTree as ET

from datetime import datetime

# Ensure needed directories exist

os.makedirs("logs", exist_ok=True)

os.makedirs("output", exist_ok=True)

# File paths

log_file     = "logs/log_file.txt"

target_file  = "output/transformed_data.csv"

def extract_from_csv(file_to_process):

    return pd.read_csv(file_to_process)

def extract_from_json(file_to_process):

    return pd.read_json(file_to_process, lines=True)

def extract_from_xml(file_to_process):

    df = pd.DataFrame(columns=["name", "height", "weight"])

    tree = ET.parse(file_to_process)

    root = tree.getroot()

    for person in root:

        df = pd.concat([

            df,

            pd.DataFrame([{

                "name":   person.find("name").text,

                "height": float(person.find("height").text),

                "weight": float(person.find("weight").text)

            }])

        ], ignore_index=True)

    return df

def extract():

    # master DataFrame

    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

    # CSV files

    for csvfile in glob.glob("data/*.csv"):

        extracted_data = pd.concat(

            [extracted_data, extract_from_csv(csvfile)],

            ignore_index=True

        )

    # JSON files

    for jsonfile in glob.glob("data/*.json"):

        extracted_data = pd.concat(

            [extracted_data, extract_from_json(jsonfile)],

            ignore_index=True

        )

    # XML files

    for xmlfile in glob.glob("data/*.xml"):

        extracted_data = pd.concat(

            [extracted_data, extract_from_xml(xmlfile)],

            ignore_index=True

        )

    return extracted_data

def transform(df):

    # inches → meters, lbs → kg

    df['height'] = (df['height'] * 0.0254).round(2)

    df['weight'] = (df['weight'] * 0.45359237).round(2)

    return df

def load_data(path, df):

    df.to_csv(path, index=False)

def log_progress(message):

    fmt = '%Y-%m-%d %H:%M:%S'

    now = datetime.now().strftime(fmt)

    with open(log_file, "a") as f:

        f.write(f"{now}, {message}\n")

if __name__ == "__main__":

    log_progress("ETL Job Started")

    log_progress("Extract phase Started")

    raw = extract()

    log_progress(f"Extract phase Ended — {len(raw)} records extracted")

    log_progress("Transform phase Started")

    transformed = transform(raw)

    log_progress("Transform phase Ended")

    print("Transformed Data Preview:")

    print(transformed.head())

    log_progress("Load phase Started")

    load_data(target_file, transformed)

    log_progress("Load phase Ended")

    log_progress("ETL Job Ended")
 