from datetime import datetime
from datetime import date as dt

# Takes future games response from api and returns an object containing future games id, teams, and date
def formatFutureGames(future_games):
    if len(future_games) == 0 or future_games == None:
        return []
    unsorted_games = []
    for games in future_games:
        game_id = games['fixture']['id']
        date = dt.fromtimestamp(games['fixture']['timestamp'])
        team_one = games['teams']['home']['name']
        team_two = games['teams']['away']['name']
        unsorted_games.append({"id" :game_id, "date": str(date), "team_one": team_one, "team_two": team_two})
    return sorted(
        unsorted_games,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d')
    )