import sqlite3

# Create database for storing scraped data
conn = sqlite3.connect("../fbref.db")
db = conn.cursor()

# Create a table for storing player appearances
db.execute('''
CREATE TABLE IF NOT EXISTS player_appearances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    season TEXT NOT NULL,
    club TEXT NOT NULL,
    appearances INTEGER NOT NULL,
    UNIQUE(player_name, season, club)
)
''')

conn.commit()
conn.close()

print("Database and table created successfully!")
