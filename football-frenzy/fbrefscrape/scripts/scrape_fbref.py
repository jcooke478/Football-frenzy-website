import requests
from bs4 import BeautifulSoup
import csv
import time
import sqlite3

conn = sqlite3.connect("../fbref.db")
db = conn.cursor()

with open("../data/players.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:

        player_name = row["Name"]
        player_url = row["Links"]
        full_url = f"https://fbref.com{player_url}"
        
        print(f"Scraping {player_name} at {full_url}")
        # Add a delay to avoid getting blocked by fbref.com
        time.sleep(5)  # Delay for 5 seconds (20 requests per minute)
        
        response = requests.get(full_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            table = soup.find("table", {"id": "stats_standard_dom_lg"})
            if not table:
                print(f"failed to scrape data for {player_name}")
                continue

            tbody = table.find("tbody")
            if not tbody:
                print(f"failed to scrape data for {player_name}")
                continue

            rows = tbody.find_all("tr")

            for row in rows:
                team_cell = row.find("td", {"data-stat": "team"})
                years_cell = row.find("th", {"data-stat": "year_id"})
                games_cell = row.find("td", {"data-stat": "games"})

                if team_cell and years_cell and games_cell:
                    team = team_cell.text.strip()
                    years = years_cell.text.strip()
                    appearances = games_cell.text.strip()

                    # Ensure appearances is a valid integer
                    appearances = int(appearances) if appearances.isdigit() else 0
                    
                    db.execute('''
                               INSERT OR IGNORE INTO player_appearances (player_name, season, club, appearances)
                               VALUES (?, ?, ?, ?)
                               ''', (player_name, years, team, appearances))
                else:
                    print(f"failed to scrape data for {player_name}")

            if i % 10 == 0:
            conn.commit()

conn.commit()
conn.close()

        
        





