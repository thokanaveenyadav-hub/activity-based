
teams = {"Team A": [3, 10], "Team B": [3, 15], "Team C": [1, 8]}
for i in range(3):
    name = input("Enter team name: ")
    win = int(input("Enter wins: "))
    score = int(input("Enter tie-break score: "))
    teams[name] = [win * 3, score]
ranking = sorted(teams.items(), key=lambda x: (-x[1][0], -x[1][1]))
print("Tournament Rankings:")
for rank, (name, values) in enumerate(ranking, 1): print(rank, name, "Points:", values[0], "Tie-break:", values[1])

