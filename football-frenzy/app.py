from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)

app.config["DEBUG"] = True  # enables debug mode

app.config["SESSION_PERMANENT"] = False # session not permanent
app.config["SESSION_TYPE"] = "filesystem" # store session data in filesystem
Session(app) # initializes session

db = SQL("sqlite:///fbrefscrape/fbref.db") # allows us to interact with database

# sets headers to prevent caching, decorator function does this for every request
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form submission
        team_name1 = request.form.get("team1input")
        team_name2 = request.form.get("team2input")

        player_data = db.execute("""
                SELECT player_name, season, club, appearances
                FROM player_appearances
                WHERE player_name IN (
                    SELECT player_name
                    FROM player_appearances
                    WHERE club = ?
                    INTERSECT
                    SELECT player_name
                    FROM player_appearances
                    WHERE club = ?
                )
                AND club IN (?, ?)    
                """, team_name1, team_name2, team_name1, team_name2)
                                    
        return render_template("results.html", player_data=player_data, team_name1=team_name1, team_name2=team_name2)
    
    if request.method == "GET":
        clubs = db.execute("""
                SELECT DISTINCT club
                FROM player_appearances
                ORDER BY club
                """)
    
        # create list of club names from clubs dictionary
        club_names = [club["club"] for club in clubs]

        return render_template("index.html", club_names=club_names)

if __name__ == "__main__":
    app.run(debug=True)