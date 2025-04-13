def transform_data(df):
   
   try:
       df = df.dropna()
       df = df.drop_duplicates()
       
       print("Data transformed successfully.")
       return df
   except Exception as e:
       print(f"Error transforming the data: {e}")
       return df
