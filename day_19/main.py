def parse_input(input_lines):
    patterns = [pattern.strip() for pattern in input_lines[0].split(",")]
    designs = input_lines[2:]
    return patterns, designs

def can_create_design(patterns, design):
    if design == "":
        return True
    for pattern in patterns:
        if design.startswith(pattern) and can_create_design(
            patterns, design[len(pattern):]):
            return True
    return False

def solve_part_1(input_lines):
    patterns, designs = parse_input(input_lines)
    return sum(
        1 for design in designs if can_create_design(patterns, design))

memo = dict()
def count_ways_to_create_design(patterns, design):
    if design == "":
        return 1
    memo_key = (",".join(patterns), design)
    if memo_key in memo:
        return memo[memo_key]
    result = 0
    for pattern in patterns:
        if design.startswith(pattern):
            result += count_ways_to_create_design(
                patterns, design[len(pattern):])
    memo[memo_key] = result
    return result

def solve_part_2(input_lines):
    patterns, designs = parse_input(input_lines)
    return sum(count_ways_to_create_design(patterns, design)
               for design in designs)

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
