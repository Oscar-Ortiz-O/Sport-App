from soccer_data import *
import requests
import json


# Performs an API request for gathering data on league standings
# La Liga ID is 140 and the most recent season is 2022
def getStandings(headers, leagueID, season):
    try:
        url = "https://api-football-v1.p.rapidapi.com/v3/standings"
        params = {"season": season, "league": leagueID}

        response = requests.request("GET", url, headers=headers, params=params)
        standingInfo = json.loads(response.text)
        standings = standingInfo['response'][0]['league']
        
    except requests.ConnectionError:
        standings = []

    finally:
        return standings


# Formats the original API request data into a simpler array of dictionaries
def formatStandings(leagueID, season):
    if (not (0 < leagueID < 5160) or not(2017 < season < 2024)):
        return []
    
    newTeams = []
    header = createHeader()
    standings = getStandings(header, leagueID, season)['standings'][0]
    
    for team in standings:
        newFormat = {'name': team['team']['name'],
                     'id': team['team']['id'],
                     'rank': team['rank'],
                     'goals': team['all']['goals']['for']}
        newTeams.append(newFormat)
    return newTeams
        


# Gets the top 5 ranked teams from the league's standings
def topFiveStandings(standings):
    topNTeams = []
    for team in standings:
        if (team['rank'] <= 5):
            topNTeams.append(team)
    return topNTeams

# Gets the top 5 teams that have scored the most goals across the season
def topFiveGoals(standings):
    
    topFive = []
    for i in range(5):
        newMax = max(standings, key = lambda x: x['all']['goals']['for'])
        maxID = newMax['team']['id']
        topFive.append({'name': newMax['team']['name'], 'goals': newMax['all']['goals']['for']})

        newStandings = []
        for team in standings:
            if (team['team']['id'] != maxID):
                newStandings.append(team)
        standings = newStandings
        
    return topFive
    
