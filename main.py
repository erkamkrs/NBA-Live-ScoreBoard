import nba_api
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

today = date.today()
todays_date = today.strftime("%d/%m/%Y")

# NBA GAMES Scoreboard Setup
games = scoreboard.ScoreBoard()
games_info = games.get_dict()
todays_games = games_info["scoreboard"]["games"]
num_of_games = len(todays_games)
v = "v"
print(todays_games)
quarter = "quarter"
overtime = "OT"


@app.route("/")
def home():
    return render_template("index.html", todays_date=todays_date, num_of_games=num_of_games,
                            games=games, todays_games=todays_games, v=v, quarter=quarter, overtime=overtime)

if __name__ == '__main__':
    app.run(debug=True)