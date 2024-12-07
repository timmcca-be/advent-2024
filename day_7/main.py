from example_input import example_input
from puzzle_input import puzzle_input

def parse_input(input_str):
    equations = []
    for line in input_str.splitlines():
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

def solve(input_str, operators):
    equations = parse_input(input_str)
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

def solve_part_1(input_str):
    return solve(input_str, [add, multiply])

def solve_part_2(input_str):
    return solve(input_str, [add, multiply, concatenate])

print("Part 1 example:", solve_part_1(example_input))
print("Part 1 real:   ", solve_part_1(puzzle_input))
print("Part 2 example:", solve_part_2(example_input))
print("Part 2 real:   ", solve_part_2(puzzle_input))
