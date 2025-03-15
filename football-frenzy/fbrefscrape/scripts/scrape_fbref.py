
import requests
from bs4 import BeautifulSoup
import csv

with open("players.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        player_name = row["name"]
        player_url = row["links"]
        
        print(f"Scraping data for {player_name} - https://fbref.com{player_url}")

url = "https://fbref.com/en/players/4cd41883/Paxten-Aaronson"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"id": "stats_standard_dom_lg"})

if table:
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")
else:
    print("Table not found.")

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



