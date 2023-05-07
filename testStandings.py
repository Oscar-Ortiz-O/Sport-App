import unittest
from standings import *

class TestGetStandings(unittest.TestCase):

    def test_getStandings_valid(self):
        actual = getStandings(140, 2022)["standings"][0][0]
        
        expected = {'rank': 1, 'team': {'id': 529, 'name': 'Barcelona',
                    'logo': 'https://media-1.api-sports.io/football/teams/529.png'},
                    'points': 82, 'goalsDiff': 49, 'group': 'Primera Division',
                    'form': 'WWLWD', 'status': 'same', 'description': 'Promotion - Champions League (Group Stage: )',
                    'all': {'played': 33, 'win': 26, 'draw': 4, 'lose': 3, 'goals': {'for': 60, 'against': 11}},
                    'home': {'played': 17, 'win': 14, 'draw': 3, 'lose': 0, 'goals': {'for': 33, 'against': 2}},
                    'away': {'played': 16, 'win': 12, 'draw': 1, 'lose': 3, 'goals': {'for': 27, 'against': 9}},
                    'update': '2023-05-04T00:00:00+00:00'}

        # Separate assertions on the values within the dictionary
        self.assertEqual(actual['rank'], expected['rank'])
        self.assertEqual(actual['status'], expected['status'])
        self.assertEqual(actual['points'], expected['points'])
        self.assertEqual(actual['goalsDiff'], expected['goalsDiff'])
        
    def test_getStandings_invalid(self):
        self.assertEqual(getStandings(0, 2022), [])
        self.assertEqual(getStandings(1, 2024), [])
        self.assertEqual(getStandings(0, 2024), [])
        

class TestFormatStandings(unittest.TestCase):

    def test_formatStandings_valid(self):

        actual = formatStandings(140, 2022)[0]
        expected = {'name': "Barcelona", 'id': 529, 'rank': 1, 'goals': 60}
        self.assertEqual(actual, expected)

                    
    def test_formatStandings_invalid(self):
        self.assertEqual(formatStandings(0, 2022), [])
        self.assertEqual(formatStandings(1, 2024), [])
        self.assertEqual(formatStandings(0, 2024), [])

# Tests for the TopFiveStandings method
class TestTopFiveStandings(unittest.TestCase):

    def test_topFiveStandings_valid(self):
        inputStandings = formatStandings(140, 2022)

        actual = topFiveStandings(inputStandings)
        expected = [{'name': 'Barcelona', 'id': 529, 'rank': 1, 'goals': 60},
                    {'name': 'Atletico Madrid', 'id': 530, 'rank': 2, 'goals': 60},
                    {'name': 'Real Madrid', 'id': 541, 'rank': 3, 'goals': 69},
                    {'name': 'Real Sociedad', 'id': 548, 'rank': 4, 'goals': 43},
                    {'name': 'Villarreal', 'id': 533, 'rank': 5, 'goals': 47}]

        self.assertEqual(actual, expected)

    def test_topFiveStandings_invalid(self):
        self.assertEqual(topFiveStandings([]), [])
        self.assertEqual(topFiveStandings([{'name': 'Barcelona'}]), [])

# Tests for the TopFiveGoals method
class TestTopFiveGoals(unittest.TestCase):

    def test_topFiveGoals_valid(self):
        inputStandings = getStandings(140, 2022)['standings'][0]

        actual = topFiveGoals(inputStandings)
        expected = [{'name': 'Real Madrid', 'goals': 69},
                    {'name': 'Barcelona', 'goals': 60},
                    {'name': 'Atletico Madrid', 'goals': 60},
                    {'name': 'Girona', 'goals': 52},
                    {'name': 'Villarreal', 'goals': 47}]

        self.assertEqual(actual, expected)

    def test_topFiveGoals_invalid(self):
        self.assertEqual(topFiveGoals([]), [])

if __name__ == '__main__':
    unittest.main()
