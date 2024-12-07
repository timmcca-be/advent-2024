import re

def solve_part_1(input_str):
    result = 0
    for match in re.finditer(
        r"mul\((?P<multiplicand>\d+),(?P<multiplier>\d+)\)", input_str
    ):
        result += (int(match.group("multiplicand"))
                   * int(match.group("multiplier")))
    return result

# trying to save the puzzle input for this puzzle as part of the program
# will get you IP banned. ask me how I know.
eof_indicator = "<<eof>>"
print(f"Enter the puzzle input, followed by {eof_indicator} on its own line:")
lines = []
while True:
    line = input()
    if line == eof_indicator:
        break
    lines.append(line)

print(solve_part_1("\n".join(lines)))
