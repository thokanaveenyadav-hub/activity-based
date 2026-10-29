data = [[45, 60, 70], [80, 90, 55], [30, 40, 65]]
readings = [x for row in data for x in row]
avg = sum(readings) / len(readings)
print("Average reading:", round(avg, 2))
print("Highest reading:", max(readings))
print("Lowest reading:", min(readings))
for i, row in enumerate(data):
    for value in row:
        if value > 75: print("Row", i+1, value, "- High")
        else: print("Row", i+1, value, "- Normal")