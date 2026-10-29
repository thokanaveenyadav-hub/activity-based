events = [("Cricket", 10), ("Football", 12), ("Cricket", 14)]
teams = [("Team A", 10), ("Team B", 15), ("Team C", 8)]
times = [e[1] for e in events]
for i in range(len(times)):
    for j in range(i+1, len(times)):
        if events[i][0] == events[j][0] and times[i] == times[j]:
            print("Scheduling conflict:", events[i], events[j])
ranking = sorted(teams, key=lambda x: x[1], reverse=True)
print("Final Rankings:")
for rank, team in enumerate(ranking, 1): print(rank, team[0], "Points:", team[1])