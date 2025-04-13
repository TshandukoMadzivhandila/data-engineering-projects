import pandas as pd

def extract_from_csv(file_path):

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None