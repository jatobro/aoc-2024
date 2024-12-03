from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2024, day=3)

mults = re.findall(
    r"mul\(\d{1,3},\d{1,3}\)",
    puzzle.input_data,
)

mult_tuples = list(
    map(lambda x: tuple(map(lambda x: int(x), x[4:-1].split(","))), mults)
)

solution_a = sum(X * Y for X, Y in mult_tuples)

puzzle.answer_a = solution_a

mults = re.findall(
    r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)",
    puzzle.input_data,
)

filtered_mults = list()
do = True
for mult in mults:
    if re.match(r"mul\(\d{1,3},\d{1,3}\)", mult) and do:
        filtered_mults.append(mult)
    elif mult == "do()":
        do = True
    elif mult == "don't()":
        do = False


mult_tuples = list(
    map(lambda x: tuple(map(lambda x: int(x), x[4:-1].split(","))), filtered_mults)
)

solution_b = sum(X * Y for X, Y in mult_tuples)

puzzle.answer_b = solution_b
