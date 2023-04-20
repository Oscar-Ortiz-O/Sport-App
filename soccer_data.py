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
        return -1
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    request = requests.request("GET", url, headers=header, params={"name": name, "country": country, "current": True})
    result = json.loads(request.text)
    if result['results'] == 0:
        return -1
    return result['response'][0]["league"]["id"]

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

