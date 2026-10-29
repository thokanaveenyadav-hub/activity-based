
rooms = {"101": [120, 50], "102": [200, 80], "201": [90, 40]}
for room, usage in rooms.items():
    electricity, water = usage
    charge = electricity * 5 + water * 2
    print("Room", room, "Charge: Rs.", charge)
    if electricity > 150 or water > 60:
        print("Warning: High consumption!")
    else:
        print("Normal consumption")
    print("Electricity:", electricity, "Water:", water)
