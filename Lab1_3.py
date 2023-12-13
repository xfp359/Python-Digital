players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8"]

total_players = len(players)
team1 = players[:total_players // 2]
team2 = players[total_players // 2:]

print(f"Команда 1: {team1}")
print(f"Команда 2: {team2}")