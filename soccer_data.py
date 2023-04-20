import requests
import json
from datetime import datetime

# Retrieves the API key
def getKey(fileName):
    file = open(fileName, encoding='utf-8-sig')
    keys = json.load(file)
    return keys['api_key']

# Returns the header which allows access to the API calls
def createHeader(key):
    header = {
        'x-rapidapi-host': "api-football-v1.p",
        'x-rapidapi-key': key}
    return header

# Returns an array of dictionaries containing all teams within a league
# Example: La Liga has ID of 140 
def getTeams(headers, leagueID, season = 2022):

    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    params = {"league": leagueID, "season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    teamsInfo = json.loads(response.text)
    return teamsInfo['response']

# Returns an array of dictionaries containing all teams within a league
# Example: Barcelona has ID of 529
def getTeamInfo(headers, teamID):
    
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    params = {"id": teamID}

    response = requests.request("GET", url, headers=headers, params=params)
    teamsInfo = json.loads(response.text)
    return teamsInfo['response']   

# Returns an array of dictionaries containing all teams within a league
# Example: Barcelona has ID of 529
def getPlayers(headers, teamID, season = 2022):

    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"team": teamID, "season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    playerInfo = json.loads(response.text)
    return playerInfo['response']

# Returns containing all teams within a league
# Example: Jordi Alba Ramos has ID of 128
def getPlayerInfo(headers, playerID, season = 2022):
    
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"id": playerID, "season": season}

    response = requests.request("GET", url, headers=headers, params=params)
    playerInfo = json.loads(response.text)
    return playerInfo['response']

# Returns array containing the last 'n' games within a league
def getGames(headers, leagueID, season = 2022, last = 5):
    
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    params = {"league": leagueID, "season": season, "last": last}

    response = requests.request("GET", url, headers=headers, params=params)
    gameInfo = json.loads(response.text)
    return gameInfo['response']

# Returns future games for current season within a league
def getFutureGames(headers, leagueID):
    if headers == None or leagueID == -1 or leagueID == None:
        return None
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    params = {"league": leagueID, "season": 2022,
              'from': datetime.today().strftime('%Y-%m-%d'), "to": "2023-10-10"}

    response = requests.request("GET", url, headers=headers, params=params)
    gameInfo = json.loads(response.text)
    return gameInfo['response']

# Returns id of a league given the league name and country
def getLeagueID(headers, name, country):
    if headers == None or name == "" or name == None or country == "" or country == None:
        return
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    request = requests.request("GET", url, headers=header, params={"name": name, "country": country, "current": True})
    result = json.loads(request.text)
    if result['results'] == 0:
        return -1
    return result['response'][0]["league"]["id"]

# Gets league ids from La Liga, Premier League, Bundesliga, Serie A, League One
# def getTopLeagues():
#     league_ids = []
#     header = {
#     'x-rapidapi-host': "api-football-v1.p",
#     'x-rapidapi-key': "b77d0337b9msh4fa982621746974p1b0214jsn7f4cb841ecf2"}
#     url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
#     spain = json.loads(requests.request("GET", url, headers=header, params={
#                        "name": "La Liga", "country": "Spain", "current": True}).text)
#     england = json.loads(requests.request("GET", url, headers=header, params={
#                          "name": "Premier League", "country": "England", "current": True}).text)
#     germany = json.loads(requests.request("GET", url, headers=header, params={
#                          "name": "Bundesliga", "country": "Germany", "current": True}).text)
#     italy = json.loads(requests.request("GET", url, headers=header, params={
#                        "name": "Serie A", "country": "Italy", "current": True}).text)
#     france = json.loads(requests.request("GET", url, headers=header, params={
#                         "name": "Ligue 1", "country": "France", "current": True}).text)
#     if spain['results'] == 0:
#         league_ids.append(-1)
#     else:
#         league_ids.append(spain['response'][0]["league"]["id"])

#     if england['results'] == 0:
#         league_ids.append(-1)
#     else:
#         league_ids.append(england['response'][0]["league"]["id"])

#     if germany['results'] == 0:
#         league_ids.append(-1)
#     else:
#         league_ids.append(germany['response'][0]["league"]["id"])

#     if italy['results'] == 0:
#         league_ids.append(-1)
#     else:
#         league_ids.append(italy['response'][0]["league"]["id"])

#     if france['results'] == 0:
#         league_ids.append(-1)
#     else:
#         league_ids.append(france['response'][0]["league"]["id"])

#     return league_ids

# Returns array containing game information
def getGameInfo(headers, gameID):
    
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    params = {"id": gameID}

    response = requests.request("GET", url, headers=headers, params=params)
    gameInfo = json.loads(response.text)
    return gameInfo['response']


# USE THIS TO GET THE HEADER
key = getKey("api_key.json")
header = createHeader(key)

