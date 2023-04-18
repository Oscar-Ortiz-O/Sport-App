from flask import Flask, render_template, request, redirect, url_for, Response
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


if __name__ == "__main__":
    app.run(debug = True)
