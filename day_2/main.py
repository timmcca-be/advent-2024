import re

from example_input import example_input
from puzzle_input import puzzle_input

def parse_input(input_str):
    return [
        [int(item) for item in re.split(r'\s+', line)]
        for line in input_str.splitlines()
    ]

def solve(input_str, is_safe):
    return [
        is_safe(report) for report in parse_input(input_str)
    ].count(True)

def is_safe_part_1(report):
    if len(report) < 2:
        return True
    is_ascending = report[0] < report[1]
    for (a, b) in zip(report[:-1], report[1:]):
        if (is_ascending and a >= b) or (not is_ascending and a <= b):
            return False
        diff = abs(a - b)
        if diff < 1 or diff > 3:
            return False
    return True

def solve_part_1(input_str):
    return solve(input_str, is_safe_part_1)

def is_safe_part_2(report):
    # this is O(n^2) with respect to the length of report.
    # since the reports are short in the datasets, this isn't
    # a problem, but this could be optimized by identifying
    # just the elements that are potentially problematic
    # instead of trying removing every element.
    # that was my first attempt, but I decided the increased
    # complexity and worse readability weren't worth it.
    for i in range(len(report)):
        candidate = [level for level in report]
        candidate.pop(i)
        if is_safe_part_1(candidate):
            return True
    return False

def solve_part_2(input_str):
    return solve(input_str, is_safe_part_2)

print("Part 1 example:", solve_part_1(example_input))
print("Part 1 real:   ", solve_part_1(puzzle_input))
print("Part 2 example:", solve_part_2(example_input))
print("Part 2 real:   ", solve_part_2(puzzle_input))
