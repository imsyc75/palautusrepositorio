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
