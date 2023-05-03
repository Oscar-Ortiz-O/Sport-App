import json

import requests


class Favorite:
    key = "25456135cemsh052881e240c8244p1c83eejsn075910996334"

    @staticmethod
    def create_header():
        header = {
            'x-rapidapi-host': "api-football-v1.p",
            'x-rapidapi-key': Favorite.key}
        return header

    @staticmethod
    def get_teams_from_api(league_id, season=2022):
        url = "https://api-football-v1.p.rapidapi.com/v3/teams"
        params = {"league": league_id, "season": season}
        response = requests.request("GET", url, headers=Favorite.create_header(), params=params)
        teams_info = json.loads(response.text)
        return teams_info['response']

    @staticmethod
    def create_teams_json():
        for id in range(90, 200):
            try:
                data = Favorite.get_teams_from_api(id, 2022)
            except KeyError:
                print("Error at " + str(id))
                data = {}
            if data:
                data = Favorite.parse_team_data(data)
                Favorite.add_to_json("teams", data)

    @staticmethod
    def parse_team_data(data):
        return {data[0]['team']['name']: data[0]}

    @staticmethod
    def add_to_json(path, new_dict):
        stored_dict = Favorite.get_json(path)
        stored_dict.update(new_dict)
        Favorite.set_json(path, stored_dict)

    @staticmethod
    def set_json(path, data):
        json_object = json.dumps(data, indent=1)
        with open("data/" + path + ".json", "w+") as file:
            file.write(json_object)

    @staticmethod
    def get_json(path):
        with open("data/" + path + ".json", 'r') as file:
            json_dict = json.load(file)
        return json_dict
