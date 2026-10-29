fares = {"City": 20, "Long": 50}
discount = {"Adult": 1.0, "Student": 0.5, "Senior": 0.7}
expected = 0
for i in range(3):
    route = input("Enter route (City/Long): ")
    category = input("Enter category (Adult/Student/Senior): ")
    passengers = int(input("Enter passengers: "))
    expected += fares[route] * discount[category] * passengers
collected = float(input("Enter collected revenue: "))
print("Expected Revenue:", expected)
print("Discrepancy:", collected - expected)