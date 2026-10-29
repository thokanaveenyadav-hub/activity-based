
material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))
cost = material + labour + wastage + machine
profit = selling - cost
print("Total Cost:", cost, "Profit:", profit)
print("Target Achieved" if profit >= target else "Target Not Achieved")

