from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=1)

lines = puzzle.input_data.split("\n")

list1 = list()
list2 = list()
for line in lines:
    parts = line.split()
    list1.append(int(parts[0]))
    list2.append(int(parts[1]))


solution_a = 0

current1 = list1.copy()
current2 = list2.copy()
while len(current1) > 0:
    number1 = min(current1)
    number2 = min(current2)

    solution_a += abs(number1 - number2)

    current1.remove(number1)
    current2.remove(number2)


puzzle.answer_a = solution_a

solution_b = 0
for number in list1:
    solution_b += number * list2.count(number)

puzzle.answer_b = solution_b
