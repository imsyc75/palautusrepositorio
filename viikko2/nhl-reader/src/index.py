import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        if player_dict.get('nationality') == 'FIN': #finnish player
            player = Player(player_dict)
            players.append(player)
    
    #sort by total points
    players.sort(key=lambda p: p.total_points, reverse=True)

    print("\nPlayers from FIN:")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
