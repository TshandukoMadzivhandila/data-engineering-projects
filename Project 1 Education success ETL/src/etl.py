import pandas as pd
import mysql.connector

def extract(file_path):
    
    ##Extract data from a CSV file.
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def transform(df):
    
    ##Transform the data.

    try:
        # Add your transformation logic here
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

def load(df, db_name, db_user, db_password, db_host, db_port):
  
    ##Load data into a MySQL database.

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            unix_socket=None  # Explicitly use TCP/IP
        )
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS student_data (
                            Student_ID VARCHAR(255) PRIMARY KEY,
                            Age INT,
                            Gender VARCHAR(255),
                            High_School_GPA FLOAT,
                            SAT_Score INT,
                            University_Ranking INT,
                            University_GPA FLOAT,
                            Field_of_Study VARCHAR(255),
                            Internships_Completed INT,
                            Projects_Completed INT,
                            Certifications INT,
                            Soft_Skills_Score INT,
                            Networking_Score INT,
                            Job_Offers INT,
                            Starting_Salary FLOAT,
                            Career_Satisfaction INT,
                            Years_to_Promotion INT,
                            Current_Job_Level VARCHAR(255),
                            Work_Life_Balance INT,
                            Entrepreneurship VARCHAR(255))''')
        
        # Insert data into the table
        for index, row in df.iterrows():
            cursor.execute('''INSERT INTO student_data (Student_ID, Age, Gender, High_School_GPA, SAT_Score, University_Ranking, University_GPA, Field_of_Study, Internships_Completed, Projects_Completed, Certifications, Soft_Skills_Score, Networking_Score, Job_Offers, Starting_Salary, Career_Satisfaction, Years_to_Promotion, Current_Job_Level, Work_Life_Balance, Entrepreneurship) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                           (row['Student_ID'], row['Age'], row['Gender'], row['High_School_GPA'], row['SAT_Score'], row['University_Ranking'], row['University_GPA'], row['Field_of_Study'], row['Internships_Completed'], row['Projects_Completed'], row['Certifications'], row['Soft_Skills_Score'], row['Networking_Score'], row['Job_Offers'], row['Starting_Salary'], row['Career_Satisfaction'], row['Years_to_Promotion'], row['Current_Job_Level'], row['Work_Life_Balance'], row['Entrepreneurship']))
        
        conn.commit()
        print("Data loaded successfully into MySQL!")
    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")
    finally:
        if 'conn' in locals() and conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Example usage
    input_file_path = "c:\\Users\\T.Madzivhandila\\Downloads\\archive\\education_career_success.csv"
    
    # MySQL database connection details
    db_name = "your_db_name"
    db_user = "your_db_user"
    db_password = "your_db_password"  # Set your database password
    db_host = "127.0.0.1"  # Use 127.0.0.1 to explicitly use TCP/IP
    db_port = 3306
    
    # Extract
    data = extract(input_file_path)
    
    if data is not None:
        # Transform
        transformed_data = transform(data)
        
        if transformed_data is not None:
            # Load
            load(transformed_data, db_name, db_user, db_password, db_host, db_port)