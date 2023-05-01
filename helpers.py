from datetime import datetime
from datetime import date as dt

# Takes future games response from api and returns an object containing future games id, teams, and date
def formatFutureGames(future_games):
    if len(future_games) == 0 or future_games == None:
        return []
    unsorted_games = []
    for game in future_games:
        if 'fixture' in game and 'id' in game['fixture'] and 'timestamp' in game['fixture'] and 'teams' in game and 'home' in game['teams'] and 'away' in game['teams']:
            game_id = game['fixture']['id']
            date = dt.fromtimestamp(game['fixture']['timestamp'])
            team_one = game['teams']['home']['name']
            team_two = game['teams']['away']['name']
            unsorted_games.append({"id": game_id, "date": str(date), "team_one": team_one, "team_two": team_two})
    return sorted(
        unsorted_games,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d')
    )