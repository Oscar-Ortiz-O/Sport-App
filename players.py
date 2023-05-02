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
        player_data = {'name': player['player']['lastname'] + ', ' + player['player']['firstname'], 'position':player['statistics'][0]['games']['position'],
                       'goals':player['statistics'][0]['goals']['total']}
        players.append(player_data)
    return players

def playerStats(headers, playerID, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"id":playerID,"season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    player_data = json.loads(response.text)

    return player_data['response'][0]['statistics']

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

# def dirtiestInTeam(players):
#     topScorers = []
#     for i in range(5):
#         newMax = max(players, key = lambda x: x['statistics'][0]['goals'])
#         topScorers.append()
        
#     return topScorers


key = getKey("api_key.json")
header = createHeader()
players = playersByTeam(header,85,2022)
# print(players)
# print(top5ScorersinLeague(header,140,2022))
# print(sortByPosition(players,"Defender"))
# print(topScorersinTeam(players))
player = playerStats(header,276,2022)
print(player)
print(playerGoals(player))


def get_team_players(team_id):
    """Retrieve data for all football players in a team using an API"""

    # Define the API endpoint and request parameters
    endpoint = f"https://api.football-data.org/v2/teams/{team_id}"
    headers = {"X-Auth-Token": "YOUR_API_KEY"}

    # Make the API request and store the response as JSON data
    response = requests.get(endpoint, headers=headers)
    team_data = response.json()

    # Extract the player data from the JSON response and store it in a list of dictionaries
    players = []
    for player in team_data['squad']:
        player_data = {'name': player['name'], 'age': player['age'], 'nationality': player['nationality'],
                       'position': player['position'], 'shirt_number': player['shirtNumber']}
        players.append(player_data)

    # Return the player data as a list of dictionaries
    return players

# def getStandings(headers, leagueID, season):
#     url = "https://api-football-v1.p.rapidapi.com/v3/standings"
#     params = {"season": season, "league": leagueID}

#     response = requests.request("GET", url, headers=headers, params=params)
#     standingInfo = json.loads(response.text)
#     return standingInfo['response'][0]['league']


# def sortByGoals(players):
#     if players == None:
#         return []
#     sortedPlayers = []

# def formatFutureGames(future_games):
#     if len(future_games) == 0 or future_games == None:
#         return []
#     unsorted_games = []
#     for games in future_games:
#         game_id = games['fixture']['id']
#         date = dt.fromtimestamp(games['fixture']['timestamp'])
#         team_one = games['teams']['home']['name']
#         team_two = games['teams']['away']['name']
#         unsorted_games.append({"id" :game_id, "date": str(date), "team_one": team_one, "team_two": team_two})
#     return sorted(
#         unsorted_games,
#         key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d')
#     )