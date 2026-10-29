students = [
    ["Ravi", 90, 85, 92, 95, 40000],
    ["Sita", 90, 80, 88, 90, 30000],
    ["Arun", 75, 70, 65, 80, 20000],
    ["Priya", 85, 90, 95, 95, 25000]
]

eligible = []

for s in students:
    name, marks, sub1, sub2, attendance, income = s

    if (marks >= 75 and sub1 >= 60 and sub2 >= 60
            and attendance >= 75 and income <= 50000):
        eligible.append(s)

# Ranking: marks first, then attendance,
# then lower family income
eligible.sort(key=lambda s: (-s[1], -s[4], s[5]))

print("SCHOLARSHIP ELIGIBLE STUDENTS")
print("-----------------------------")
rank = 1
for s in eligible:
    print(rank, s[0], "- Marks:", s[1],
          "Attendance:", s[4], "%")
    rank += 1

print("\nTotal eligible students:", len(eligible))