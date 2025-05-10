import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'

try:
    html_page = requests.get(url).text
except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    exit()

data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
if not tables:
    print("No tables found on the webpage.")
    exit()

rows = tables[0].find_all('tr')
if not rows:
    print("No rows found in the table.")
    exit()

rows_data = []
count = 0
for row in rows:
    if count < 50:
        col = row.find_all('td')
        if len(col) >= 3 and col[0].contents and col[1].contents and col[2].contents:
            try:
                rows_data.append({
                    "Average Rank": int(col[0].contents[0]),
                    "Film": str(col[1].contents[0]),
                    "Year": int(col[2].contents[0])
                })
                count += 1
            except ValueError as e:
                print(f"Error processing row data: {e}")
    else:
        break

df = pd.DataFrame(rows_data)
print(df)

# Save to CSV
df.to_csv(csv_path, index=False)
print(f"Data saved to {csv_path}")

# Save to SQLite database
try:
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data saved to SQLite database: {db_name}, table: {table_name}")
except sqlite3.DatabaseError as e:
    print(f"Error saving to database: {e}")