from flask import Flask, render_template, request, redirect, url_for, Response
import soccer_data as sd
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
    return render_template('games.html')


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
