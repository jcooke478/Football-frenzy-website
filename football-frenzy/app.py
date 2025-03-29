from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)

app.config["DEBUG"] = True  # enables debug mode

app.config["SESSION_PERMANENT"] = False # session not permanent
app.config["SESSION_TYPE"] = "filesystem" # store session data in filesystem
Session(app) # initializes session

db = SQL("sqlite:///fbref.db") # allows us to interact with database

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
        return render_template("results.html")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)