from example_input import example_input
from puzzle_input import puzzle_input

vectors = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

target_word = "XMAS"

def is_target_word(lines, start_line_index, start_char_index, vector):
    line_direction, char_direction = vector
    for (i, target_char) in enumerate(target_word):
        line_index = start_line_index + i * line_direction
        if line_index < 0 or line_index >= len(lines):
            return False
        line = lines[line_index]
        char_index = start_char_index + i * char_direction
        if char_index < 0 or char_index >= len(line):
            return False
        if line[char_index] != target_char:
            return False
    return True

def solve_part_1(input_str):
    lines = input_str.splitlines()
    count = 0
    for (line_index, line) in enumerate(lines):
        for (char_index, _) in enumerate(line):
            for vector in vectors:
                if is_target_word(lines, line_index, char_index, vector):
                    count += 1
    return count

def is_m_and_s(a, b):
    return (a == "M" and b == "S") or (a == "S" and b == "M")

def solve_part_2(input_str):
    lines = input_str.splitlines()
    count = 0
    for line_index in range(1, len(lines) - 1):
        line = lines[line_index]
        for char_index in range(len(line) - 1):
            center = line[char_index]
            top_left = lines[line_index - 1][char_index - 1]
            top_right = lines[line_index - 1][char_index + 1]
            bottom_left = lines[line_index + 1][char_index - 1]
            bottom_right = lines[line_index + 1][char_index + 1]
            if (center == "A"
                and is_m_and_s(top_left, bottom_right)
                and is_m_and_s(top_right, bottom_left)):
                count += 1
    return count

print("Part 1 example:", solve_part_1(example_input))
print("Part 1 real:   ", solve_part_1(puzzle_input))
print("Part 2 example:", solve_part_2(example_input))
print("Part 2 real:   ", solve_part_2(puzzle_input))
