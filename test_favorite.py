import unittest
from favorite import Favorite as f


class TestAddToJSON(unittest.TestCase):

    def test1_add_to_json(self):
        fav_team = "Mexico"
        f.set_json("favorite", fav_team)
        self.assertEqual(f.get_json("favorite"), fav_team)

    def test2_add_to_json(self):
        fav_team = ""
        f.set_json("favorite", fav_team)
        self.assertEqual(f.get_json("favorite"), fav_team)

    def test3_add_to_json(self):
        fav_team = ["Mexico", "USA"]
        f.set_json("favorite", fav_team)
        self.assertEqual(f.get_json("favorite"), fav_team)


class TestGetTeamNamesList(unittest.TestCase):

    def test1_get_team_names_list(self):
        self.assertEqual(f.get_team_names_list()[3], "Internacional")

    def test2_get_team_names_list(self):
        self.assertEqual(f.get_team_names_list()[20], "APOEL U19")

    def test3_get_team_names_list(self):
        self.assertEqual(len(f.get_team_names_list()), 96)


class TestParseTeamData(unittest.TestCase):

    def test1_parse_team_data(self):
        team_data = [{"team": {"name": "Mexico", "country": "Mexico"}}]
        parsed_data = {"Mexico": {"team": {"country": "Mexico", "name": "Mexico"}}}
        self.assertEqual(f.parse_team_data(team_data), parsed_data)

    def test2_parse_team_data(self):
        team_data = [{"team": {"name": "USA", "country": "USA"}}]
        parsed_data = {"USA": {"team": {"country": "USA", "name": "USA"}}}
        self.assertEqual(f.parse_team_data(team_data), parsed_data)

    def test3_parse_team_data(self):
        team_data = [{"team": {"name": "La Liga", "country": "Japan"}}]
        parsed_data = {"La Liga": {"team": {"country": "Japan", "name": "La Liga"}}}
        self.assertEqual(f.parse_team_data(team_data), parsed_data)


if __name__ == '__main__':
    unittest.main()
