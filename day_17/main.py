import re

def get_number(line):
    return int(re.search(r"\d+", line).group())

def parse_input(input_lines):
    a = get_number(input_lines[0])
    b = get_number(input_lines[1])
    c = get_number(input_lines[2])
    program = [int(value) for value in re.findall(r"\d+", input_lines[4])]
    return [a, b, c], program

def dereference_combo_operand(combo_operand, registers):
    if combo_operand <= 3:
        return combo_operand
    return registers[combo_operand - 4]

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

A = 0
B = 1
C = 2

def solve_part_1_parsed(registers, program):
    program_counter = 0
    output = []
    while program_counter < len(program):
        instruction = program[program_counter]
        literal_operand = program[program_counter + 1]
        combo_operand = dereference_combo_operand(literal_operand, registers)

        did_jump = False
        if instruction == ADV:
            registers[A] //= 2 ** combo_operand
        elif instruction == BXL:
            registers[B] ^= literal_operand
        elif instruction == BST:
            registers[B] = combo_operand % 8
        elif instruction == JNZ:
            if registers[A] != 0:
                program_counter = literal_operand
                did_jump = True
        elif instruction == BXC:
            registers[B] ^= registers[C]
        elif instruction == OUT:
            output.append(combo_operand % 8)
        elif instruction == BDV:
            registers[B] = registers[A] // (2 ** combo_operand)
        elif instruction == CDV:
            registers[C] = registers[A] // (2 ** combo_operand)

        if not did_jump:
            program_counter += 2
    return ",".join([str(value) for value in output])

def solve_part_1(input_lines):
    registers, program = parse_input(input_lines)
    return solve_part_1_parsed(registers, program)

def get_printed_value(A):
    p = (A % 8) ^ 1
    q = A // (2 ** p)
    return (p ^ q ^ 4) % 8

def solve_part_2(input_lines):
    _, program = parse_input(input_lines)
    outputs = list(program)
    outputs.reverse()
    candidates = {0}
    for i, output in enumerate(outputs):
        new_candidates = set()
        for candidate in candidates:
            for i in range(8):
                new_candidate = candidate * 8 + i
                if get_printed_value(new_candidate) == output:
                    new_candidates.add(new_candidate)
        candidates = new_candidates
    if len(candidates) == 0:
        raise Exception("unsolvable")
    return min(candidates)

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
