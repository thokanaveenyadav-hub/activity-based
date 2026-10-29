
ordered = int(input("Enter ordered quantity: "))
dispatched = int(input("Enter dispatched quantity: "))
returned = int(input("Enter returned quantity: "))
stock = int(input("Enter current inventory: "))
if ordered < 0 or dispatched < 0 or returned < 0 or stock < 0:
    print("Invalid record")
elif dispatched > ordered or returned > dispatched:
    print("Inconsistent records")
else:
    print("Outstanding orders:", ordered - dispatched)
    print("Updated inventory:", stock + returned)
    print("Valid order records")
