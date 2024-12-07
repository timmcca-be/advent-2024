import re

from example_input import example_input
from puzzle_input import puzzle_input

def parse_input(input_str):
    first_list = []
    second_list = []
    for line in input_str.splitlines():
        [first, second] = re.split(r"\s+", line)
        first_list.append(int(first))
        second_list.append(int(second))
    return (first_list, second_list)

def solve_part_1(input_str):
    (first_list, second_list) = parse_input(input_str)
    first_list.sort()
    second_list.sort()

    result = 0
    for (first, second) in zip(first_list, second_list):
        result += abs(first - second)
    return result

def solve_part_2(input_str):
    (first_list, second_list) = parse_input(input_str)
    multipliers = dict()
    for item in second_list:
        if item in multipliers:
            multipliers[item] += 1
        else:
            multipliers[item] = 1

    result = 0
    for item in first_list:
        if item in multipliers:
            result += item * multipliers[item]
    return result

print("part 1 example:", solve_part_1(example_input))
print("part 1 real:   ", solve_part_1(puzzle_input))
print("part 2 example:", solve_part_2(example_input))
print("part 2 real:   ", solve_part_2(puzzle_input))
