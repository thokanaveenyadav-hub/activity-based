seats = [[101, 102, 0], [103, 104, 105], [106, 101, -1]]
reserved = [(0, 2), (2, 2)]
rolls = [x for row in seats for x in row if x > 0]
for i, row in enumerate(seats):
    for j, roll in enumerate(row):
        if (i, j) in reserved: print(roll, "Reserved position")
        elif roll == 0: print("Empty seat at", i, j)
        elif roll < 0: print("Invalid allocation at", i, j)
        elif rolls.count(roll) > 1: print("Duplicate roll number:", roll)
        else: print("Valid seat:", roll)