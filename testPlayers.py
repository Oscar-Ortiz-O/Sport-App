import unittest
from players import *

class testPlayersByTeam(unittest.TestCase):
    def test_playersByTeam_valid(self):
        actual = playersByTeam(header,85,2022)

        expected = [{'name': 'Diallo, Abdou-Lakhad', 'id': 7, 'age': 27, 'position': 'Defender', 'goals': 0, 'image': 'https://media-2.api-sports.io/football/players/7.png'}, 
                    {'name': 'Hakimi Mouh, Achraf', 'id': 9, 'age': 25, 'position': 'Defender', 'goals': 4, 'image': 'https://media-2.api-sports.io/football/players/9.png'}, 
                    {'name': 'Alcântara do Nascimento, Rafael', 'id': 142, 'age': 31, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-1.api-sports.io/football/players/142.png'}, 
                    {'name': 'Kehrer, Jan Thilo', 'id': 261, 'age': 27, 'position': 'Defender', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/261.png'}, 
                    {'name': 'Kimpembe, Presnel', 'id': 262, 'age': 28, 'position': 'Defender', 'goals': 0, 'image': 'https://media-2.api-sports.io/football/players/262.png'}, 
                    {'name': 'Kurzawa, Layvin', 'id': 263, 'age': 31, 'position': 'Defender', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/263.png'}, 
                    {'name': 'Draxler, Julian', 'id': 267, 'age': 30, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/267.png'}, 
                    {'name': 'Paredes, Leandro Daniel', 'id': 271, 'age': 29, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-1.api-sports.io/football/players/271.png'}, 
                    {'name': 'Wijnaldum, Georginio Gregion Emile', 'id': 300, 'age': 33, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/300.png'}, 
                    {'name': 'Navas Gamboa, Keylor Antonio', 'id': 731, 'age': 37, 'position': 'Goalkeeper', 'goals': 0, 'image': 'https://media-1.api-sports.io/football/players/731.png'}, 
                    {'name': 'Donnarumma, Gianluigi', 'id': 1622, 'age': 24, 'position': 'Goalkeeper', 'goals': 0, 'image': 'https://media-1.api-sports.io/football/players/1622.png'}, 
                    {'name': 'Sarabia García, Pablo', 'id': 2056, 'age': 31, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-1.api-sports.io/football/players/2056.png'}, 
                    {'name': 'Gueye, Idrissa Gana', 'id': 2990, 'age': 34, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-2.api-sports.io/football/players/2990.png'}, 
                    {'name': 'Rico González, Sergio', 'id': 19014, 'age': 30, 'position': 'Goalkeeper', 'goals': 0, 'image': 'https://media-1.api-sports.io/football/players/19014.png'}, 
                    {'name': 'Letellier, Alexandre', 'id': 20568, 'age': 33, 'position': 'Goalkeeper', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/20568.png'}, 
                    {'name': 'Dina Ebimbe, Éric Junior', 'id': 90594, 'age': 23, 'position': 'Midfielder', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/90594.png'}, 
                    {'name': 'Lavallée, Lucas', 'id': 198398, 'age': 20, 'position': 'Goalkeeper', 'goals': 0, 'image': 'https://media-3.api-sports.io/football/players/198398.png'}, 
                    {'name': 'El Hannach, Younes', 'id': 336655, 'age': 18, 'position': 'Defender', 'goals': None, 'image': 'https://media-2.api-sports.io/football/players/336655.png'}, 
                    {'name': 'Muntu Wa Mungu, Vimoj', 'id': 336656, 'age': 18, 'position': 'Defender', 'goals': None, 'image': 'https://media-3.api-sports.io/football/players/336656.png'}, 
                    {'name': 'Adonis, Erwan', 'id': 402306, 'age': 16, 'position': 'Defender', 'goals': None, 'image': 'https://media-2.api-sports.io/football/players/402306.png'}]
        
        self.assertEqual(actual,expected)
        
    def test_playersByTeam_invalid(self):
        self.assertEqual(playersByTeam(header, 0, 2022), [])
        self.assertEqual(playersByTeam(header, 1, 2025), [])
        self.assertEqual(playersByTeam(header, 0, 2025), [])

class testPlayerStats(unittest.TestCase):
    def test_playerStats_valid(self):
        actual = playerStats(header,276,2022)

        expected = [{'team': {'id': 85, 'name': 'Paris Saint Germain', 'logo': 'https://media-2.api-sports.io/football/teams/85.png'}, 
                     'league': {'id': 61, 'name': 'Ligue 1', 'country': 'France', 'logo': 'https://media-1.api-sports.io/football/leagues/61.png', 
                                'flag': 'https://media-1.api-sports.io/flags/fr.svg', 'season': 2022}, 
                                'games': {'appearences': 20, 'lineups': 18, 'minutes': 1553, 'number': None, 'position': 'Attacker', 'rating': '7.725000', 'captain': False}, 
                                'substitutes': {'in': 2, 'out': 8, 'bench': 2}, 'shots': {'total': 30, 'on': 20}, 'goals': {'total': 13, 'conceded': 0, 'assists': 11, 'saves': None}, 
                                'passes': {'total': 1187, 'key': 49, 'accuracy': 49}, 'tackles': {'total': 22, 'blocks': 1, 'interceptions': 4}, 'duels': {'total': 242, 'won': 124}, 
                                'dribbles': {'attempts': 83, 'success': 36, 'past': None}, 'fouls': {'drawn': 65, 'committed': 25}, 'cards': {'yellow': 5, 'yellowred': 1, 'red': 0}, 
                                'penalty': {'won': None, 'commited': None, 'scored': 2, 'missed': 0, 'saved': None}}, {'team': {'id': 85, 'name': 'Paris Saint Germain', 
                                'logo': 'https://media-3.api-sports.io/football/teams/85.png'}, 'league': {'id': 2, 'name': 'UEFA Champions League', 'country': 'World', 
                                'logo': 'https://media-3.api-sports.io/football/leagues/2.png', 'flag': None, 'season': 2022}, 'games': {'appearences': 6, 'lineups': 6, 
                                'minutes': 540, 'number': None, 'position': 'Attacker', 'rating': '7.533333', 'captain': False}, 'substitutes': {'in': 0, 'out': 1, 'bench': 0}, 
                                'shots': {'total': 11, 'on': 6}, 'goals': {'total': 2, 'conceded': 0, 'assists': 2, 'saves': None}, 'passes': {'total': 366, 'key': 16, 'accuracy': 52}, 
                                'tackles': {'total': 3, 'blocks': None, 'interceptions': 2}, 'duels': {'total': 85, 'won': 36}, 'dribbles': {'attempts': 26, 'success': 14, 'past': None}, 
                                'fouls': {'drawn': 19, 'committed': 8}, 'cards': {'yellow': 4, 'yellowred': 0, 'red': 0}, 'penalty': {'won': None, 'commited': None, 'scored': 0, 
                                'missed': 0, 'saved': None}}, {'team': {'id': 6, 'name': 'Brazil', 'logo': 'https://media-1.api-sports.io/football/teams/6.png'}, 'league': {'id': 34, 
                                'name': 'World Cup - Qualification South America', 'country': 'World', 'logo': 'https://media-2.api-sports.io/football/leagues/34.png', 'flag': None, 'season': 2022}, 
                                'games': {'appearences': 10, 'lineups': 10, 'minutes': 900, 'number': None, 'position': 'Attacker', 'rating': '8.470000', 'captain': False}, 
                                'substitutes': {'in': 0, 'out': 0, 'bench': 0}, 'shots': {'total': 33, 'on': 21}, 'goals': {'total': 8, 'conceded': 0, 'assists': 8, 'saves': None}, 
                                'passes': {'total': 479, 'key': 36, 'accuracy': 38}, 'tackles': {'total': 12, 'blocks': None, 'interceptions': 5}, 'duels': {'total': 194, 'won': 119}, 
                                'dribbles': {'attempts': 83, 'success': 55, 'past': None}, 'fouls': {'drawn': 50, 'committed': 12}, 'cards': {'yellow': 4, 'yellowred': 0, 'red': 0}, 
                                'penalty': {'won': None, 'commited': None, 'scored': 4, 'missed': 0, 'saved': None}}, {'team': {'id': 6, 'name': 'Brazil', 
                                'logo': 'https://media-2.api-sports.io/football/teams/6.png'}, 'league': {'id': 1, 'name': 'World Cup', 'country': 'World', 'logo': 
                                'https://media-2.api-sports.io/football/leagues/1.png', 'flag': None, 'season': 2022}, 'games': {'appearences': 3, 'lineups': 3, 'minutes': 281, 
                                'number': None, 'position': 'Attacker', 'rating': '6.833333', 'captain': False}, 'substitutes': {'in': 0, 'out': 2, 'bench': 0}, 
                                'shots': {'total': 9, 'on': 6}, 'goals': {'total': 2, 'conceded': 0, 'assists': 1, 'saves': None}, 'passes': {'total': 143, 'key': 6, 'accuracy': 38}, 
                                'tackles': {'total': 1, 'blocks': None, 'interceptions': 1}, 'duels': {'total': 55, 'won': 23}, 'dribbles': {'attempts': 19, 'success': 6, 'past': None}, 
                                'fouls': {'drawn': 16, 'committed': 4}, 'cards': {'yellow': 0, 'yellowred': 0, 'red': 0}, 'penalty': {'won': None, 'commited': None, 'scored': 1, 'missed': 0, 'saved': None}}]

        self.assertEqual(actual,expected)

    def test_playerStats_invalid(self):
        self.assertEqual(playerStats(header, 0, 2022), [])
        self.assertEqual(playerStats(header, 1, 2025), [])
        self.assertEqual(playerStats(header, 0, 2025), [])

class testsortByPosition(unittest.TestCase):
    def test_sortByPosition_valid(self):
        actual = sortByPosition(playersByTeam(header,85,2022),"Defender")

        expected = ['Diallo, Abdou-Lakhad', 'Hakimi Mouh, Achraf', 'Kehrer, Jan Thilo', 'Kimpembe, Presnel', 
                    'Kurzawa, Layvin', 'El Hannach, Younes', 'Muntu Wa Mungu, Vimoj', 'Adonis, Erwan']
        
        self.assertEqual(actual,expected)

    def test_sortByPosition_invalid(self):
        self.assertEqual(sortByPosition(playersByTeam(header,85,2022),"Center"), [])
        self.assertEqual(sortByPosition(playersByTeam(header,0,2022),"Defender"), [])
        self.assertEqual(sortByPosition(playersByTeam(header,85,2025),"Defender"), [])

class testtop5ScorersinLeague(unittest.TestCase):
    def test_top5ScorersinLeague_valid(self):
        actual = top5ScorersinLeague(header,140,2022)

        expected = [{'name': 'Lewandowski, Robert', 'goals': 19}, {'name': 'Benzema, Karim Mostafa', 'goals': 17}, 
                    {'name': 'Sanmartín Mato, José Luis', 'goals': 14}, {'name': 'Ünal, Enes', 'goals': 14}, 
                    {'name': 'Griezmann, Antoine', 'goals': 13}]
        
        self.assertEqual(actual,expected)

    def test_top5ScorersinLeague_valid(self):
        self.assertEqual(top5ScorersinLeague(header,0,2022), [])
        self.assertEqual(top5ScorersinLeague(header,1,2025), [])
        self.assertEqual(top5ScorersinLeague(header,0,2025), [])

if __name__ == '__main__':
    unittest.main()