from soccer_data import *
import requests
import json


def playersByTeam(headers, teamID, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"team": teamID,"season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    player_data = json.loads(response.text)

    # print(player_data)
    players = []
    for player in player_data['response']:
        player_data = {'name': player['player']['lastname'] + ', ' + player['player']['firstname'],
                       'id': player['player']['id'],
                       'age': player['player']['age'],
                       'position':player['statistics'][0]['games']['position'],
                       'goals': player['statistics'][0]['goals']['total'],
                       'image': player['player']['photo']}
        players.append(player_data)
    return players

def playerStats(headers, playerID, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"id":playerID,"season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    player_data = json.loads(response.text)

    if(player_data['results']!=0):
        return player_data['response'][0]['statistics']
    else:
        return []

def sortByPosition(players,position):
    positionPlayers = []
    for player in players:
        if(player['position']==position):
            positionPlayers.append(player['name'])
    return positionPlayers

def playerGoals(player):
    goals = player[0]['goals']
    return goals


def playersBypopularity(headers, leagueID, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"league":leagueID, "season": season,"order":"popularity"}

    response = requests.request("GET", url, headers=headers, params=params)
    player_data = json.loads(response.text)

    print(player_data)

    players = []
    for player in player_data['response']:
        player_data = {'name': player['player']['lastname'] + ', ' + player['player']['firstname']}
        players.append(player_data)
    return players

def top5ScorersinLeague(headers, leagueID, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
    params = {"league":leagueID, "season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    player_data = json.loads(response.text)

    players = []
    if(player_data!=None):
        for player in player_data['response'][:5]:
            player_data = {'name': player['player']['lastname'] + ', ' + player['player']['firstname'], 'goals':player['statistics'][0]['goals']['total']}
            players.append(player_data)
    return players


# def get_team_players(team_id):
#     """Retrieve data for all football players in a team using an API"""

#     # Define the API endpoint and request parameters
#     endpoint = f"https://api.football-data.org/v2/teams/{team_id}"
#     headers = {"X-Auth-Token": "YOUR_API_KEY"}

#     # Make the API request and store the response as JSON data
#     response = requests.get(endpoint, headers=headers)
#     team_data = response.json()

#     # Extract the player data from the JSON response and store it in a list of dictionaries
#     players = []
#     for player in team_data['squad']:
#         player_data = {'name': player['name'], 'age': player['age'], 'nationality': player['nationality'],
#                        'position': player['position'], 'shirt_number': player['shirtNumber']}
#         players.append(player_data)

#     # Return the player data as a list of dictionaries
#     return players

