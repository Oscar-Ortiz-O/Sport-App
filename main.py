from flask import Flask, render_template, request, redirect, url_for, Response
import soccer_data as sd
import helpers
import json, requests
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('splash.html')


@app.route('/teams/')
def teamsPage():
    return render_template('teams.html')


@app.route('/players/')
def playersPage():
    return render_template('players.html')


@app.route('/games/')
def gamesPage():
    leagues_information = [
        {"league_name": "La Liga", "id": sd.getLeagueID(headers=sd.header, country="Spain", name="La Liga")},
        {"league_name":"Premier League", "id":sd.getLeagueID(headers=sd.header, country="England", name="Premier League")},
        {"league_name":"Bundesliga", "id":sd.getLeagueID(headers=sd.header, country="Germany", name="Bundesliga")},
        {"league_name":"Serie A", "id":sd.getLeagueID(headers=sd.header, country="Italy", name="Serie A")},
        {"league_name":"Ligue 1", "id":sd.getLeagueID(headers=sd.header, country="France", name="Ligue 1")},
    ]
    all_games = []
    for league in leagues_information:
        future_games = sd.getFutureGames(sd.header, league["id"])
        future_games = helpers.formatFutureGames(future_games)
        all_games.append({"league_name": league["league_name"], "games": future_games})
    print(all_games)
    return render_template('games.html', all_games=all_games)

@app.route('/game/<id>')
def individualGamePage(id):
    return render_template('game.html', id=id)

@app.route('/favorite/')
def favorite_page():
    team_list = sd.getTeams(sd.header, 140)
    return render_template('favorite.html', team_list=team_list)


@app.route('/favorite_confirm/', methods=['GET'])
def favorite_conf_page():
    team_name = request.args.get('team_name')
    sd.set_favorite_team(team_name)
    return render_template('favorite_confirm.html')


if __name__ == "__main__":
    app.run(debug=True)
