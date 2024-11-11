from rich.console import Console
from rich.table import Table
from player import PlayerReader, PlayerStats

def main():
    console = Console()

    # get the season and nationality
    season = console.input("Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/]: ")
    nationality = console.input("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/]: ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    # use the rich to show the result
    table = Table(title=f"Top scorers of {nationality} season {season}")

    table.add_column("name", justify="left")
    table.add_column("team", justify="center")
    table.add_column("goals", justify="center")
    table.add_column("assists", justify="center")
    table.add_column("points", justify="center")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.total_points))

    console.print(table)

if __name__ == "__main__":
    main()