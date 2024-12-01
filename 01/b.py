lines = list()

with open("./input.txt") as f:
    for line in f:
        lines.append(line.rstrip())

# separate the lists
list1 = list()
list2 = list()
for line in lines:
    parts = line.split()
    list1.append(int(parts[0]))
    list2.append(int(parts[1]))

solution = 0

for number in list1:
    solution += number * list2.count(number)

print("solution", solution)
