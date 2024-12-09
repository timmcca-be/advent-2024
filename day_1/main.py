import re

def parse_input(input_lines):
    first_list = []
    second_list = []
    for line in input_lines:
        [first, second] = re.split(r"\s+", line)
        first_list.append(int(first))
        second_list.append(int(second))
    return (first_list, second_list)

def solve_part_1(input_lines):
    (first_list, second_list) = parse_input(input_lines)
    first_list.sort()
    second_list.sort()

    result = 0
    for (first, second) in zip(first_list, second_list):
        result += abs(first - second)
    return result

def solve_part_2(input_lines):
    (first_list, second_list) = parse_input(input_lines)
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
