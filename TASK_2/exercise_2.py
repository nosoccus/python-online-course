def change_positions(players: list):
    players[0], players[-1] = players[-1], players[0]
    print(players)


if __name__ == "__main__":
    change_positions(
    players = ['Ashleigh Barty', 'Simona Halep', 'Naomi Osaka', 'Karolina Pliskova', 'Elina Svitolina']
    )
    
