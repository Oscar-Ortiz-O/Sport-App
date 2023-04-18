import requests
import json


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

