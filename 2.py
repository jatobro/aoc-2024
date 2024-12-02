from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=2)

lines = puzzle.input_data.split("\n")

reports = list(map(lambda x: list(map(lambda x: int(x), x.split())), lines))

solution_a = 0


def is_safe(report):
    increasing = report.copy()
    decreasing = report.copy()
    increasing.sort()
    decreasing.sort(reverse=True)

    if increasing != report and decreasing != report:
        return False

    current = report[0]
    for i in range(1, len(report)):
        if abs(current - report[i]) > 3 or abs(current - report[i]) < 1:
            return False

        current = report[i]

    return True


for report in reports:
    if is_safe(report):
        solution_a += 1

puzzle.answer_a = solution_a

solution_b = 0

for report in reports:
    for i in range(len(report)):
        # ith element is removed
        smaller_report = report[:i] + report[i + 1 :]
        if is_safe(smaller_report):
            solution_b += 1
            break

puzzle.answer_b = solution_b
