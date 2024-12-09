import re

def parse_input(input_lines):
    return [
        [int(item) for item in re.split(r'\s+', line)]
        for line in input_lines
    ]

def solve(input_lines, is_safe):
    return [
        is_safe(report) for report in parse_input(input_lines)
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

def solve_part_1(input_lines):
    return solve(input_lines, is_safe_part_1)

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

def solve_part_2(input_lines):
    return solve(input_lines, is_safe_part_2)

fake_newline = "$"
eof_indicator = "<<eof>>"
print("Note: newlines will be ignored due to limitations in the platform, "
      + f"but the {fake_newline} character will be treated as a newline.")
print(f"Enter the puzzle input, followed by {eof_indicator} "
      + "on its own (real) line:")
input_str = ""
while True:
    line = input()
    if line.strip() == eof_indicator:
        break
    input_str += line

input_lines = [line.strip() for line in input_str.split(fake_newline)]

print("Part 1:", solve_part_1(input_lines))
print("Part 2:", solve_part_2(input_lines))
