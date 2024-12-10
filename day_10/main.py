def is_in_bounds(map, position):
    return (position[1] >= 0 and position[1] < len(map)
            and position[0] >= 0 and position[0] < len(map[0]))

def at(map, position):
    if not is_in_bounds(map, position):
        return None
    return map[position[1]][position[0]]

vectors = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

def move(position, vector):
    return (
        position[0] + vector[0],
        position[1] + vector[1]
    )

def solve(input_lines, score):
    map = [[int(char) for char in line] for line in input_lines]
    result = 0
    for (line_index, line) in enumerate(map):
        for (num_index, num) in enumerate(line):
            if num == 0:
                result += score(map, (num_index, line_index))
    return result

def get_end_positions(map, position):
    current = at(map, position)
    if current == 9:
        return {position}
    next_positions = [move(position, vector) for vector in vectors]
    end_positions = set()
    for next_position in next_positions:
        if at(map, next_position) != current + 1:
            continue
        end_positions |= get_end_positions(map, next_position)
    return end_positions

def solve_part_1(input_lines):
    return solve(
        input_lines,
        lambda map, position: len(get_end_positions(map, position)))

def rate(map, position):
    current = at(map, position)
    if current == 9:
        return 1
    next_positions = [move(position, vector) for vector in vectors]
    return sum(rate(map, next_position)
               for next_position in next_positions
               if at(map, next_position) == current + 1)

def solve_part_2(input_lines):
    return solve(input_lines, rate)

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
