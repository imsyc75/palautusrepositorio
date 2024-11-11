import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict.get('team', 'N/A')
        self.goals = dict.get('goals', 0)
        self.assists = dict.get('assists', 0)
        self.nationality = dict.get('nationality', 'N/A')
        self.total_points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {self.total_points:3}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players
    
class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda p: p.nationality == nationality, self.players)
        sorted_players = sorted(filtered_players, key=lambda p: p.total_points, reverse=True)
        return sorted_players