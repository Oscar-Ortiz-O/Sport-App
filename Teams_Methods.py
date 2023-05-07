from soccer_data import *

def getTeamIds(leagueID, season=2022):
    header = createHeader()
    teams = getTeams(header, leagueID, season)
    teamIds = [team['team']['id'] for team in teams]
    return teamIds


def getOldestTeams(leagueID, season=2022):
    header = createHeader()
    teams = getTeams(header, leagueID, season)
    if not teams:
        return []
    sortedTeams = sorted(teams, key=lambda x: x['team']['founded'])
    oldestTeams = []
    for i in range(min(5, len(sortedTeams))):
        team = sortedTeams[i]
        oldestTeams.append(team['team']['id'])

    return oldestTeams


def getYoungestTeams(leagueID, season=2022):
    header = createHeader()
    teams = getTeams(header, leagueID, season)
    if not teams:
        return []
    sortedTeams = sorted(teams, key=lambda x: x['team']['founded'], reverse=True)
    youngestTeams = []
    for i in range(min(5, len(sortedTeams))):
        team = sortedTeams[i]
        youngestTeams.append(team['team']['id'])
    return youngestTeams



def formatTeams(leagueID, season):
    if(not(0 < leagueID < 5160) or not(2017 < season < 2024)):
        return[]

    newTeams = []
    header = createHeader()
    teams = getTeams(header, leagueID, season)

    for team in teams:
        newFormat = {'name': team['team']['name'],
                     'id': team['team']['id'],
                     'country': team['team']['country'],
                     'image':team['team']['logo'],
                     'founded': team['team']['founded'],
                     'venue': team['venue']['name']}
        newTeams.append(newFormat)
    return newTeams
