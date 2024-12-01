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

while len(list1) > 0:
    number1 = min(list1)
    number2 = min(list2)

    solution += abs(number1 - number2)

    list1.remove(number1)
    list2.remove(number2)


print("solution", solution)
