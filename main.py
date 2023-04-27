from flask import Flask, render_template, request, redirect, url_for, Response
import soccer_data as sd
import helpers
import json, requests
import subprocess
from werkzeug.security import generate_password_hash
from auth import validate_email, email_in_use, same_username, valid_user_pswd_combination, create_session, valid_session, log_out
import uuid
import secretKey as sk

app = Flask(__name__)
app.secret_key = sk.secretKey

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

#Auth
@app.route('/LogIn/', methods=['GET','POST'])
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
                print("Error: Email format is not valid!")
            elif len(password) == 0:
                print("Error: No password provided")
            elif not email_in_use(email):
                print("Error: No User found in our records")
            elif not valid_user_pswd_combination(email, password):
                print("Error: No combination of credentials")
            # Else means there are no errors, so we log in
            else:
                # Check if session was created
                if create_session(email) > 0:
                    # Redirect the user to the index page
                    return redirect(url_for('index'))
                print("Error: Failure creating session")
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
                print("Error", "Email format is not valid!")
            elif email_in_use(email):
                print("Error", "Email is arleady in use by another user")
            elif same_username(username):
                print("Error", "Username is already taken")
            elif len(username) == 0:
                print("Error", "No username provided")
            elif len(username) < 5:
                print("Error", "Username is too short!")
            elif len(password1) == 0:
                print("Error", "No password provided")
            elif password1 != password2:
                print("Error", "Passwords do not match!")
            elif len(password1) < 7:
                print("Error", "Password must be more than 8 characters long")
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
