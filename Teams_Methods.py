from soccer_data import *

header = createHeader()
def getTeamIds(headers, leagueID, season=2022):
    teams = getTeams(headers, leagueID, season)
    teamIds = [team['team']['id'] for team in teams]
    return teamIds

Ids = getTeamIds(header, 140)
print(Ids)


teams = getTeams(header, 140, season=2022)
def getOldestTeams(teams, headers, leagueID, season=2022):
    if not teams:
        return []
    sortedTeams = sorted(teams, key=lambda x: x['team']['founded'])
    oldestTeams = []
    for i in range(min(5, len(sortedTeams))):
        team = sortedTeams[i]
        oldestTeams.append(team['team']['id'])

    return oldestTeams

oldest_teams = getOldestTeams(teams, header, 140)
print(oldest_teams)


teams = getTeams(header, 140, season=2022)
def getYoungestTeams(teams, headers, leagueID, season=2022):
    if not teams:
        return []
    sortedTeams = sorted(teams, key=lambda x: x['team']['founded'], reverse=True)
    youngestTeams = []
    for i in range(min(5, len(sortedTeams))):
        team = sortedTeams[i]
        youngestTeams.append(team['team']['id'])
    return youngestTeams

youngest_teams = getYoungestTeams(teams, header, 140)
print(youngest_teams)


def formatTeams(leagueID, season):
    if(not(0 < leagueID < 5160) or not(2017 < season < 2024)):
        return[]

    newTeams = []
    header = createHeader()
    teams = getTeams(header, leagueID, season)

    for team in teams:
        newFormat = {'name': team['team']['name'],
                     'id': team['team']['id'],
                     'country': team['team']['country']}
        newTeams.append(newFormat)
    return newTeams
    
format_teams = formatTeams(140, 2022)
print(format_teams)

#def test_getOldestTeams():
    # Test case 1: empty header and league ID
 #   assert getOldestTeams({}, None) == []

    # Test case 2: valid header and league ID, invalid season
  #  assert getOldestTeams(header, 140, 2020) == []

    # Test case 3: valid header, league ID and season
   # oldest_teams = getOldestTeams(header, 140)
    #assert len(oldest_teams) == 5
    #assert isinstance(oldest_teams[0], int)

    # Test case 4: valid header, league ID and season, less than 5 teams
    #teams = getTeams(header, 135)
    #for team in teams:
     #   team['team']['founded'] = 1900
    #oldest_teams = getOldestTeams(header, 135)
    #assert len(oldest_teams) == len(teams)
    #assert isinstance(oldest_teams[0], int)

    # Test case 5: valid header, league ID and season, all teams founded in the same year
    #teams = getTeams(header, 150)
    #for team in teams:
     #   team['team']['founded'] = 1900
    #oldest_teams = getOldestTeams(header, 150)
    #assert len(oldest_teams) == len(teams)
    #assert isinstance(oldest_teams[0], int)


    #def test_getTeamIds():
    # Test case 1: empty header and league ID
    #assert getTeamIds({}, None) == []

    # Test case 2: valid header and league ID, invalid season
    #assert getTeamIds(header, 140, 2020) == []

    # Test case 3: valid header, league ID and season
    #teams = [{'team': {'id': 1}}, {'team': {'id': 2}}, {'team': {'id': 3}}]
    #getTeams = lambda h, l, s: teams
#    assert getTeamIds(header, 140) == [1, 2, 3]

    # Test case 4: valid header and league ID, no teams in the league
 #   assert getTeamIds(header, 999) == []
