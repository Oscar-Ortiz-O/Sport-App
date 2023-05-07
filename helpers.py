from datetime import datetime
from datetime import date as dt

# Takes future games response from api and returns an object containing future games id, teams, and date
def formatFutureGames(future_games):
    if len(future_games) == 0 or future_games == None:
        return []
    unsorted_games = {}
    for game in future_games:
        if 'fixture' in game and 'id' in game['fixture'] and 'timestamp' in game['fixture'] and 'teams' in game and 'home' in game['teams'] and 'away' in game['teams']:
            game_id = game['fixture']['id']
            date = str(dt.fromtimestamp(game['fixture']['timestamp']))
            team_one = game['teams']['home']['name']
            team_one_logo = game['teams']['home']['logo']
            team_two = game['teams']['away']['name']
            team_two_logo = game['teams']['away']['logo']
            if (date not in unsorted_games):
                unsorted_games[date] = []
            unsorted_games[date].append({"id": game_id, "team_one": team_one, "team_one_logo": team_one_logo, "team_two": team_two, "team_two_logo": team_two_logo})
    return sorted(unsorted_games.items(), key = lambda x:datetime.strptime(x[0], '%Y-%m-%d'))

def formatIndividualGame(game):
    if (game == None or game == []):
        return None
    game_info = {
        'referee': game['fixture']['referee'],
        'date': str(dt.fromtimestamp(game['fixture']['timestamp'])),
        'city': game['fixture']['venue']['city'],
        'stadium': game['fixture']['venue']['name'],
        'league': game['league']['name'],
        'home': game['teams']['home']['name'],
        'home_logo': game['teams']['home']['logo'],
        'away': game['teams']['away']['name'],
        'away_logo': game['teams']['away']['logo'],
    }
    return game_info