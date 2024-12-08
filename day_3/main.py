import re

def solve_part_1(input_str):
    result = 0
    for match in re.finditer(
        r"mul\((?P<multiplicand>\d+),(?P<multiplier>\d+)\)", input_str
    ):
        result += (int(match.group("multiplicand"))
                   * int(match.group("multiplier")))
    return result

def solve_part_2(input_str):
    result = 0
    is_enabled = True
    for match in re.finditer(
        r"mul\((?P<multiplicand>\d+),(?P<multiplier>\d+)\)|do\(\)|don't\(\)",
        input_str
    ):
        text = match.group()
        if text == "do()":
            is_enabled = True
            continue
        if text == "don't()":
            is_enabled = False
            continue
        if not is_enabled:
            continue
        result += (int(match.group("multiplicand"))
                   * int(match.group("multiplier")))
    return result

# trying to save the puzzle input for this puzzle as part of the program
# will get you IP banned. ask me how I know.
eof_indicator = "<<eof>>"
print(f"Enter the puzzle input, followed by {eof_indicator} on its own line:")
input_str = ""
while True:
    line = input()
    if line == eof_indicator:
        break
    input_str += line

print("Part 1:", solve_part_1(input_str))
print("Part 2:", solve_part_2(input_str))
