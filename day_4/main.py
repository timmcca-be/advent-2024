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

def solve_part_1(lines):
    count = 0
    for (line_index, line) in enumerate(lines):
        for (char_index, _) in enumerate(line):
            for vector in vectors:
                if is_target_word(lines, line_index, char_index, vector):
                    count += 1
    return count

def is_m_and_s(a, b):
    return (a == "M" and b == "S") or (a == "S" and b == "M")

def solve_part_2(lines):
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
