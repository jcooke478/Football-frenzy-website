import requests
from googlesearch import search
from bs4 import BeautifulSoup
import csv
import time
import sqlite3

conn = sqlite3.connect("../fbref.db")
db = conn.cursor()

# opens players.csv file and creates an iterator to read each row (reader)
with open("../data/players.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    # selects each row in the csv file and assigns name value to current search query
    for row in reader:
        for i, row in enumerate(reader): # counter to keep track of how many rows have been processed
            player_name = row["Name"]
            query = f"site:fbref.com{player_name}"
            search_results = search(query, num_results=1)
            
            if "en/players/" in search_results:
                player_url = search_results[0]
            else:
                print(f"No valid URL found for {player_name}")
                continue
                
            print(f"Scraping {player_name} at {player_url}")
            time.sleep(3.1) # Add a delay to avoid getting blocked by fbref.com (20 searches per second)
            
            response = requests.get(player_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser") # creates 'parsed' html object for searching for content

                # Finds the table with player appearances   
                table = soup.find("table", {"id": "stats_standard_dom_lg"})
                if not table:
                    print(f"failed to scrape data for {player_name}")
                    continue

                # finds body of the table with player data
                tbody = table.find("tbody")
                if not tbody:
                    print(f"failed to scrape data for {player_name}")
                    continue

                rows = tbody.find_all("tr")

                # Loops through each row to locate team, years played and number of games
                for row in rows:
                    team_cell = row.find("td", {"data-stat": "team"})
                    years_cell = row.find("th", {"data-stat": "year_id"})
                    games_cell = row.find("td", {"data-stat": "games"})

                    if team_cell and years_cell and games_cell:
                        team = team_cell.text.strip()
                        years = years_cell.text.strip()
                        appearances = games_cell.text.strip()

                        # Ensures appearances is a valid integer
                        appearances = int(appearances) if appearances.isdigit() else 0
                            
                        db.execute('''
                                INSERT OR IGNORE INTO player_appearances (player_name, season, club, appearances)
                                VALUES (?, ?, ?, ?)
                                ''', (player_name, years, team, appearances))
                    else:
                        print(f"failed to scrape data for {player_name}")

                # coomits every 10 rows to database
                if i % 10 == 0:
                    conn.commit()

conn.commit()
conn.close()

        
        





