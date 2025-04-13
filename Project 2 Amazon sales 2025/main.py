import os
from etl import extract_from_csv, transform_data, load_data_to_db

# Load database configuration from environment variables
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "amazon"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "#####"),  # Replace with a default or secure method
}

def main():
    try:
        # Extract
        file_path = os.getenv("INPUT_FILE_PATH", r"C:\Users\T.Madzivhandila\Music\amazon_sales_data_2025.csv")
        data = extract_from_csv(file_path)

        if data is not None:
            # Transform
            transformed_data = transform_data(data)

            # Load
            load_data_to_db(transformed_data, db_config)
        else:
            print("No data to process.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()