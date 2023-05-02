from flask import Flask, render_template, request, redirect, url_for, Response, flash
import soccer_data as sd
from Teams_Methods import *
from standings import *
import helpers
import json, requests
import subprocess
from werkzeug.security import generate_password_hash
from auth import *
import uuid
import secretKey as sk

app = Flask(__name__)
app.secret_key = sk.secretKey

@app.route('/Home', methods=['GET','POST'])
def index():
    # Check if there is a valid session
    if valid_session():
        # Get the username
        username = get_username()
        # Return the view with the respective username
        return render_template('splash.html', username=username)
    # Return to login since no current session
    return redirect(url_for('login'))


@app.route('/teams/')
def teamsPage():
    
    teams = formatTeams(140, 2022)
    rankStanding = topFiveStandings(formatStandings(140, 2022))

    standingTeams = getStandings(createHeader(), 140, 2022)['standings'][0]
    goalStanding = topFiveGoals(standingTeams)
    
    return render_template('teams.html', teams = teams, rankStanding = rankStanding, goalStanding = goalStanding)


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
        all_games.append({"league_name": league["league_name"], "games": future_games})
    return render_template('games.html', all_games=all_games)

@app.route('/game/<id>')
def individualGamePage(id):
    return render_template('game.html', id=id)

@app.route('/search_favorite/', methods=['GET', 'POST'])
def search_favorite_page():
    if request.method == 'POST':
        lid = request.form.get("lid")
        year = request.form.get("year")
        return redirect(url_for(".favorite_page", year=year, lid=lid))
    return render_template('search_favorite.html')

@app.route('/favorite/')
def favorite_page():
    lid = request.args.get('lid')
    year = request.args.get('year')
    team_list = sd.parse_team_list(sd.get_team(lid, year))
    print(sd.get_team(lid, year))
    return render_template('favorite.html', data=team_list)


@app.route('/favorite_confirm/', methods=['GET'])
def favorite_conf_page():
    team_name = request.args.get('team_name')
    sd.set_favorite_team(team_name)
    return render_template('favorite_confirm.html')

#Auth
@app.route('/', methods=['GET','POST'])
def login():
    # Check if there is a valid session
    if valid_session():
        # If so, redirect to index page
        return redirect(url_for('index'))
    # Otherwise, continue with the logging in
    else:
        # Check type of method when loading the page
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            # Check if fields are valid inputs
            if not validate_email(email):
                flash("Error: Email format is not valid!", category='error')
            elif len(password) == 0:
                flash("Error: No password provided", category='error')
            elif not email_in_use(email):
                flash("Error: No User found in our records", category='error')
            elif not valid_user_pswd_combination(email, password):
                flash("Error: No combination of credentials", category='error')
            # Else means there are no errors, so we log in
            else:
                # Check if session was created
                if create_session(email) > 0:
                    # Redirect the user to the index page
                    return redirect(url_for('index'))
                flash("Error: Failure creating session", category='error')
    # Display the original template
    return render_template('login.html')

@app.route('/SignUp/', methods=['GET','POST'])
def signup():
    # Check if there is a valid session
    if valid_session():
        # If so, redirect to the index page
        return redirect(url_for('index'))
    # Otherwise continue signing up
    else:
        # Check type of method used when loading the page
        if request.method == 'POST':
            # Getting the information as request
            email = request.form.get('email')
            username = request.form.get('username')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            # Check if fields are valid inputs
            if not validate_email(email):
                flash("Error: Email format is not valid!", category='error')
            elif email_in_use(email):
                flash("Error: Email is arleady in use by another user", category='error')
            elif same_username(username):
                flash("Error: Username is already taken", category='error')
            elif len(username) == 0:
                flash("Error: No username provided", category='error')
            elif len(username) < 5:
                flash("Error: Username is too short!", category='error')
            elif len(password1) == 0:
                flash("Error: No password provided", category='error')
            elif password1 != password2:
                flash("Error: Passwords do not match!", category='error')
            elif len(password1) < 7:
                flash("Error: Password must be more than 8 characters long", category='error')
            # Else means there are no errors, so we add into the database
            else:
                # Create a unique id for each user
                id = uuid.uuid4()
                # Assigning all values to each user
                new_user = {
                    str(id) : {
                        'email' : email,
                        'username' : username,
                        'password' : generate_password_hash(password1,method='sha256')
                    }
                }
                # open the file that will be overwritten
                with open("data/database.json", "r") as openfile:
                    users = json.load(openfile)
                # updating the data inside the file
                users['user'].update(new_user)
                # overwrite the file with the correct data
                with open("data/database.json", "w") as outfile:
                    json.dump(users, outfile)
                # Redirecting the user to log in after creating their account
                return redirect(url_for('login'))
    # Displaying original template
    return render_template('sign_up.html')

@app.route('/Logout/')
def logout():
    log_out()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
