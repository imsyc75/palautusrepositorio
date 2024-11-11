class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict.get('team', 'N/A')
        self.goals = dict.get('goals', 0)
        self.assists = dict.get('assists', 0)
        self.nationality = dict.get('nationality', 'N/A')
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"

