import requests
from bs4 import BeautifulSoup
import csv
import time

with open("../data/players.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for i, row in enumerate(reader):  # Add an index counter
        if i >= 12:  # Stop after 3 players
            break

        player_name = row["Name"]
        player_url = row["Links"]
        full_url = f"https://fbref.com{player_url}"
        
        print(f"Scraping {player_name} at {full_url}")
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        table = soup.find("table", {"id": "stats_standard_dom_lg"})

        if not table:
            print("Table not found. Trying another table.")
            continue

        tbody = table.find("tbody")
        rows = tbody.find_all("tr")

        for row in rows:
            team_cell = row.find("td", {"data-stat": "team"})
            years_cell = row.find("th", {"data-stat": "year_id"})
            games_cell = row.find("td", {"data-stat": "games"})

            if team_cell and years_cell and games_cell:
                team = team_cell.text.strip()
                years = years_cell.text.strip()
                appearences = games_cell.text.strip()
                print(f"{years} - {team} - {appearences} apps")
            else:
                print("Team not found.")
        
        print("\n")
        
        # Add a delay to avoid rate limiting
        time.sleep(5)  # Delay for 5 seconds





