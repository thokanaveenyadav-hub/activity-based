capacity = int(input("Enter bus capacity: "))
passengers = 0
stops = int(input("Enter number of stops: "))
for i in range(stops):
    board = int(input("Passengers boarding: "))
    exit_bus = int(input("Passengers alighting: "))
    passengers = passengers - exit_bus + board
    if passengers < 0: print("Invalid passenger count!")
    elif passengers > capacity: print("Capacity violation!")
    else: print("Stop", i+1, "Passengers:", passengers)