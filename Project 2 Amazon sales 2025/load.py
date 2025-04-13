import psycopg2

def load_data_to_db(data, db_config):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        
        # Create a table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS your_table_name (
                Id SERIAL PRIMARY KEY,
                Order_ID INT,
                Date DATE,
                Product_Category VARCHAR(50),
                Price DECIMAL,
                Quantity INT,    
                Total_Sales DECIMAL,
                Customer_Name VARCHAR(100),
                Customer_Location VARCHAR(100),
                Payment_Method VARCHAR(50),
                Status VARCHAR(50)
            )
        """)
        
        # Insert data into the table
        for _, row in data.iterrows():
            cur.execute("""
                INSERT INTO your_table_name (Order_ID, Date, Product_Category, Price, Quantity, Total_Sales, Customer_Name, Customer_Location, Payment_Method, Status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))
        
        conn.commit()
        cur.close()
        conn.close()
        
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data to the database: {e}")
        if 'conn' in locals() and conn:
            conn.close()