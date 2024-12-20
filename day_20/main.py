def is_in_bounds(dimensions, position):
    width, height = dimensions
    return (position[1] >= 0 and position[1] < width
            and position[0] >= 0 and position[0] < height)

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)

vectors = [
    NORTH,
    EAST,
    SOUTH,
    WEST,
]

def move(position, vector):
    return (
        position[0] + vector[0],
        position[1] + vector[1]
    )

def get_absolute_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse_input(input_lines):
    width = len(input_lines[0])
    height = len(input_lines)
    walls = set()
    for line_index, line in enumerate(input_lines):
        for char_index, char in enumerate(line):
            position = (char_index, line_index)
            if char == "#":
                walls.add(position)
            elif char == "S":
                start = position
            elif char == "E":
                end = position
    return start, end, walls, (width, height)

def solve(input_lines, max_cheat_distance):
    start, end, walls, dimensions = parse_input(input_lines)
    distances = {start: 0}
    positions_and_distances = [(0, start)]
    positions = {start}
    distance = 0
    while end not in positions:
        new_positions = set()
        distance += 1
        for position in positions:
            for vector in vectors:
                new_position = move(position, vector)
                if new_position in distances or new_position in walls:
                    continue
                new_positions.add(new_position)
                distances[new_position] = distance
                positions_and_distances.append((distance, new_position))
        positions = new_positions
    target_distance = distance - 100
    visited = {end}
    positions = {end}
    distance = 0
    result = 0
    while True:
        min_distance_from_start, _ = positions_and_distances[0]
        if min_distance_from_start + distance > target_distance:
            break
        visited |= positions
        new_positions = set()
        for position in positions:
            for distance_from_start, start_position in positions_and_distances:
                if distance_from_start + distance > target_distance:
                    break
                distance_apart = get_absolute_distance(
                    start_position, position)
                if (distance_apart <= max_cheat_distance
                    and distance_from_start + distance + distance_apart
                    <= target_distance):
                    result += 1
            for vector in vectors:
                new_position = move(position, vector)
                if new_position not in visited | walls:
                    new_positions.add(new_position)
        positions = new_positions
        distance += 1
    return result

def solve_part_1(input_lines):
    return solve(input_lines, 2)

def solve_part_2(input_lines):
    return solve(input_lines, 20)

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
