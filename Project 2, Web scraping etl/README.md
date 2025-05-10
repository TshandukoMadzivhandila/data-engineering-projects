# Top 50 Highly Ranked Films Scraper

This project is a Python script that scrapes the top 50 most highly ranked films from an archived *EverybodyWiki* page, then saves the data to both a CSV file and a SQLite database.

---

## Features

- Web scraping using `requests` and `BeautifulSoup`
- Data parsing and cleaning with `pandas`
- Saves results to:
  - CSV file: `data/top_50_films.csv`
  - SQLite database: `data/Movies.db`, table: `Top_50`
- Basic error handling for connection and data issues

---

## Project Structure

Project_2-Web scraping etl/
│
├── top_50_films_scraper.py # Main script
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── data/ # Output files (auto-created)
├── top_50_films.csv # Scraped film data in CSV format
└── Movies.db # SQLite database with film data


---

## Requirements

- Python 3.x
- Install dependencies with:

```bash
pip install -r requirements.txt
requirements.txt contains:

requests
beautifulsoup4
pandas
