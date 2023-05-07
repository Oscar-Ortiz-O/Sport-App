import unittest
from Teams_Methods import*

class TestGetTeamsIds(unittest.TestCase):
    def test_getTeamIds(self):
        #Test case 1: Invalid league ID
        self.assertEqual(getTeamIds(None), [])

        #Test case 2: Valid league ID, Invalid season
        self.assertEqual(getTeamIds(140, 2025), [])

        #Test case 3: Valid league ID and season
        teams = [529, 530, 531, 532, 533, 536, 538, 540, 541, 543, 546, 547, 548, 720, 723, 724, 727, 728, 797, 798]
        self.assertEqual(getTeamIds(140), teams)

        #Test case 4: Valid league ID, no teams in the league
        self.assertEqual(getTeamIds(999), [])
        
class TestGetOldestTeams(unittest.TestCase):
    def test_getOldestTeams(self):
        #Test case 1: Invalid league ID
        self.assertEqual(getOldestTeams(None), [])

        #Test case 2: Valid league ID, Invalid season
        self.assertEqual(getOldestTeams(140, 2025), [])

        #Test case 3: Valid league ID and season
        oldest_teams = getOldestTeams(140)
        self.assertEqual(len(oldest_teams), 5)
        self.assertTrue(isinstance(oldest_teams[0], int))

        #Test case 4: Valid league ID and season, less than 5 teams
        header = createHeader()
        teams = getTeams(header, 140)
        for team in teams:
            team['team']['founded'] = 1900
        oldest_teams = getOldestTeams(140)
        self.assertEqual(len(oldest_teams), 5)
        self.assertTrue(isinstance(oldest_teams[0], int))

        #Test case 5: Valid league ID and season, all teams founded in the same year
        teams = getTeams(header, 140)
        for team in teams:
            team['team']['founded'] = 1900
        oldest_teams = getOldestTeams(140)
        self.assertEqual(len(oldest_teams), 5)
        self.assertTrue(isinstance(oldest_teams[0], int))

class TestGetYoungestTeams(unittest.TestCase):
    def test_getYoungestTeams(self):
        #Test case 1: Invalid league ID
        self.assertEqual(getYoungestTeams(None), [])

        #Test case 2: Valid league ID, Invalid season
        self.assertEqual(getYoungestTeams(140, 2025), [])

        #Test case 3: Valid league ID and season
        oldest_teams = getYoungestTeams(140)
        self.assertEqual(len(oldest_teams), 5)
        self.assertTrue(isinstance(oldest_teams[0], int))

        #Test case 4: Valid league ID and season, less than 5 teams
        header = createHeader()
        teams = getTeams(header, 140)
        for team in teams:
            team['team']['founded'] = 1900
        youngest_teams = getYoungestTeams(140)
        self.assertEqual(len(youngest_teams), 5)
        self.assertTrue(isinstance(youngest_teams[0], int))

        #Test case 5: Valid league ID and season, all teams founded in the same year
        teams = getTeams(header, 140)
        for team in teams:
            team['team']['founded'] = 1900
        youngest_teams = getYoungestTeams(140)
        self.assertEqual(len(youngest_teams), 5)
        self.assertTrue(isinstance(youngest_teams[0], int))

class TestFormatTeams(unittest.TestCase):
    def test_formatTeams_valid(self):
        actual = formatTeams(140, 2022)[0]
        expected = {'name': "Barcelona",
                    'id': 529,
                    'country': "Spain",
                    'image': "https://media-1.api-sports.io/football/teams/529.png",
                    'founded': 1899,
                    'venue': "Spotify Camp Nou"}
        self.assertEqual(actual, expected)

    def test_formatTeams_invalid(self):
        self.assertEqual(formatTeams(0, 2022), [])
        self.assertEqual(formatTeams(1, 2024), [])
        self.assertEqual(formatTeams(0, 2024), [])

if __name__ == '__main__':
    unittest.main()
