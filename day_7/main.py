def parse_input(input_lines):
    equations = []
    for line in input_lines:
        parts = line.split(": ")
        target = int(parts[0])
        operands = [int(operand) for operand in parts[1].split(" ")]
        equations.append((target, operands))
    return equations

def can_reach_target(target, operands, operators):
    if len(operands) == 0:
        print("empty?")
        return False
    if len(operands) == 1:
        return target == operands[0]
    for operator in operators:
        if can_reach_target(
            target,
            [operator(operands[0], operands[1])] + operands[2:],
            operators,
        ):
            return True
    return False

def solve(input_lines, operators):
    equations = parse_input(input_lines)
    result = 0
    for (target, operands) in equations:
        if can_reach_target(target, operands, operators):
            result += target
    return result

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def concatenate(a, b):
    # return int(str(a) + str(b))
    multiplier = 10
    while b // multiplier > 0:
        multiplier *= 10
    return a * multiplier + b

def solve_part_1(input_lines):
    return solve(input_lines, [add, multiply])

def solve_part_2(input_lines):
    return solve(input_lines, [add, multiply, concatenate])

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
