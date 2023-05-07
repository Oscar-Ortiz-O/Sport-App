import unittest
import soccer_data as sd
import helpers as h
from pprint import pprint


class TestGetFutureGames(unittest.TestCase):
    def testGetFutureGamesValid(self):
        futureGames = sd.getFutureGames(sd.header, 140)
        singleGame = futureGames[0]

        self.assertIsNotNone(singleGame['fixture']['id'])
        self.assertIsNotNone(singleGame['fixture']['timezone'])
        self.assertIsNotNone(singleGame['fixture']['date'])
        self.assertIsNotNone(singleGame['fixture']['timestamp'])
        self.assertIsNotNone(singleGame['fixture']['periods'])
        self.assertIsNotNone(singleGame['fixture']['venue'])
        self.assertIsNotNone(singleGame['fixture']['status'])

        self.assertIsNotNone(singleGame['goals'])
        self.assertIsNotNone(singleGame['league'])
        self.assertIsNotNone(singleGame['teams'])
        self.assertIsNotNone(singleGame['score'])

    def testGetFutureGamesInvalid(self):
        self.assertEqual(sd.getFutureGames(sd.header, -1), None)
        self.assertEqual(sd.getFutureGames(None, []), None)


class TestFormatFutureGames(unittest.TestCase):
    def testFormatFutureGamesValid(self):
        futureGames = [
            {
                "fixture": {
                    "id": 18,
                    "timezone": "UTC",
                    "date": "2020-11-21T15:00:00+00:00",
                    "timestamp": 1605978000,
                    "periods": {
                        "first": 1605978000,
                        "second": 1605981600
                    },
                    "venue": {
                        "id": 550,
                        "name": "Stamford Bridge",
                        "city": "London"
                    },
                    "status": {
                        "long": "Match Finished",
                        "short": "FT",
                        "elapsed": 90
                    }
                },
                "goals": {
                    "home": 2,
                    "away": 0
                },
                "league": {
                    "id": 140,
                    "name": "Premier League",
                    "country": "England",
                    "logo": "https://media.api-sports.io/football/leagues/39.png",
                    "flag": "https://media.api-sports.io/flags/gb.svg",
                    "season": 2020,
                    "round": "Regular Season - 9"
                },
                "teams": {
                    "home": {
                        "id": 49,
                        "name": "Newcastle",
                        "logo": "newcastle.png",
                        "winner": False
                    },
                    "away": {
                        "id": 46,
                        "name": "Chelsea",
                        "logo": "chelsea.png",
                        "winner": True
                    }
                },
                "score": {
                    "halftime": {
                        "home": 0,
                        "away": 0
                    },
                    "fulltime": {
                        "home": 2,
                        "away": 0
                    },
                    "extratime": {
                        "home": None,
                        "away": None
                    },
                    "penalty": {
                        "home": None,
                        "away": None
                    }
                }
            },
            {
                "fixture": {
                    "id": 14,
                    "timezone": "UTC",
                    "date": "2020-11-21T15:00:00+00:00",
                    "timestamp": 1805978000,
                    "periods": {
                        "first": 1605978000,
                        "second": 1605981600
                    },
                    "venue": {
                        "id": 550,
                        "name": "Stamford Bridge",
                        "city": "London"
                    },
                    "status": {
                        "long": "Match Finished",
                        "short": "FT",
                        "elapsed": 90
                    }
                },
                "goals": {
                    "home": 2,
                    "away": 0
                },
                "league": {
                    "id": 140,
                    "name": "La Liga",
                    "country": "Spain",
                    "logo": "https://media.api-sports.io/football/leagues/39.png",
                    "flag": "https://media.api-sports.io/flags/gb.svg",
                    "season": 2020,
                    "round": "Regular Season - 9"
                },
                "teams": {
                    "home": {
                        "id": 49,
                        "name": "Barcelona",
                        "logo": "barcelona.png",
                        "winner": False
                    },
                    "away": {
                        "id": 46,
                        "name": "Real Madrid",
                        "logo": "real_madrid.png",
                        "winner": True
                    }
                },
                "score": {
                    "halftime": {
                        "home": 0,
                        "away": 0
                    },
                    "fulltime": {
                        "home": 2,
                        "away": 0
                    },
                    "extratime": {
                        "home": None,
                        "away": None
                    },
                    "penalty": {
                        "home": None,
                        "away": None
                    }
                }
            }
        ]
        formattedGames = h.formatFutureGames(futureGames)
        gameOne = formattedGames[0][1][0]
        gameTwo = formattedGames[1][1][0]

        self.assertEqual(gameOne['id'], 18)
        self.assertEqual(gameOne['team_one'], 'Newcastle')
        self.assertEqual(gameOne['team_two'], 'Chelsea')
        self.assertEqual(gameOne['team_one_logo'], 'newcastle.png')
        self.assertEqual(gameOne['team_two_logo'], 'chelsea.png')

        self.assertEqual(gameTwo['id'], 14)
        self.assertEqual(gameTwo['team_one'], 'Barcelona')
        self.assertEqual(gameTwo['team_two'], 'Real Madrid')
        self.assertEqual(gameTwo['team_one_logo'], 'barcelona.png')
        self.assertEqual(gameTwo['team_two_logo'], 'real_madrid.png')

    def testFormatFutureGamesInvalid(self):
        formattedGames = h.formatFutureGames([])
        self.assertEqual(formattedGames, [])

class TestGetGameInfo(unittest.TestCase):
    def testGetGameInfoValid(self):
        gameInfo = sd.getGameInfo(sd.header, 878317)
        gameInfo = gameInfo[0]
        self.assertIsNotNone(gameInfo)
        self.assertIsNotNone(gameInfo['fixture'])
        self.assertIsNotNone(gameInfo['goals'])
        self.assertIsNotNone(gameInfo['league'])
        self.assertIsNotNone(gameInfo['teams'])
        self.assertIsNotNone(gameInfo['score'])
        
        self.assertEqual(gameInfo['teams']['away']['name'], 'Barcelona')
        self.assertEqual(gameInfo['teams']['home']['name'], 'Celta Vigo')

    def testGetGameInfoInvalid(self):
        self.assertEqual(sd.getGameInfo(sd.header, -1), None)
        self.assertEqual(sd.getGameInfo(None, []), None)

class TestFormatIndividualGame(unittest.TestCase):
    def testFormatIndividualGameValid(self):
        gameInfo = {'events': [],
                    'fixture': {'date': '2023-06-04T00:00:00+00:00',
                                'id': 878317,
                                'periods': {'first': None, 'second': None},
                                'referee': 'Test Referee',
                                'status': {'elapsed': None,
                                           'long': 'Time to be defined',
                                           'short': 'TBD'},
                                'timestamp': 1685836800,
                                'timezone': 'UTC',
                                'venue': {'city': 'Vigo', 'id': 1467, 'name': 'Abanca-Balaídos'}},
                    'goals': {'away': None, 'home': None},
                    'league': {'country': 'Spain',
                               'flag': 'https://media-3.api-sports.io/flags/es.svg',
                               'id': 140,
                               'logo': 'https://media-1.api-sports.io/football/leagues/140.png',
                               'name': 'La Liga',
                               'round': 'Regular Season - 38',
                               'season': 2022},
                    'lineups': [],
                    'players': [],
                    'score': {'extratime': {'away': None, 'home': None},
                              'fulltime': {'away': None, 'home': None},
                              'halftime': {'away': None, 'home': None},
                              'penalty': {'away': None, 'home': None}},
                    'statistics': [],
                    'teams': {'away': {'id': 529,
                                       'logo': 'https://media-1.api-sports.io/football/teams/529.png',
                                       'name': 'Barcelona',
                                       'winner': None},
                              'home': {'id': 538,
                                       'logo': 'https://media-3.api-sports.io/football/teams/538.png',
                                       'name': 'Celta Vigo',
                                       'winner': None}}}
        formattedGameInfo = h.formatIndividualGame(gameInfo)
        self.assertEqual(formattedGameInfo['date'], '2023-06-03')
        self.assertEqual(formattedGameInfo['city'], 'Vigo')
        self.assertEqual(formattedGameInfo['stadium'], 'Abanca-Balaídos')
        self.assertEqual(formattedGameInfo['league'], 'La Liga')
        self.assertEqual(formattedGameInfo['home'], 'Celta Vigo')
        self.assertEqual(formattedGameInfo['home_logo'], 'https://media-3.api-sports.io/football/teams/538.png')
        self.assertEqual(formattedGameInfo['away'], 'Barcelona')
        self.assertEqual(formattedGameInfo['away_logo'], 'https://media-1.api-sports.io/football/teams/529.png')
        self.assertEqual(formattedGameInfo['referee'], 'Test Referee')
    
    def testFormatIndividualGameInvalid(self):
        self.assertEqual(h.formatIndividualGame(None), None)
        self.assertEqual(h.formatIndividualGame([]), None)


if __name__ == '__main__':
    unittest.main()

