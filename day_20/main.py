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

def get_distance_without_cheating(start, end, walls):
    visited = set()
    positions = {start}
    distance = 0
    while end not in positions:
        visited |= positions
        new_positions = set()
        for position in positions:
            for vector in vectors:
                new_position = move(position, vector)
                if new_position not in walls | visited:
                    new_positions.add(new_position)
        positions = new_positions
        distance += 1
    return distance

def solve_part_1(input_lines):
    start, end, walls, dimensions = parse_input(input_lines)
    cheats = set()
    cheat_distances = dict()
    cheats_and_distances = []
    visited = set()
    positions = {start}
    distance = 0
    while end not in positions:
        visited |= positions
        new_positions = set()
        for position in positions:
            for vector in vectors:
                new_position = move(position, vector)
                if new_position in visited:
                    continue
                if new_position not in walls:
                    new_positions.add(new_position)
                    continue
                cheat_position = move(new_position, vector)
                cheat = (position, new_position)
                cheat_distance = distance + 2
                if (not is_in_bounds(dimensions, cheat_position)
                    or cheat_position in walls
                    or cheat in cheats):
                    continue
                cheats.add(cheat)
                cheats_and_distances.append(
                    (cheat_distance, cheat_position))
                if cheat_position in cheat_distances:
                    cheat_distances[cheat_position].append(cheat_distance)
                else:
                    cheat_distances[cheat_position] = [cheat_distance]
        positions = new_positions
        distance += 1
    target_distance = distance - 100
    visited = set()
    positions = {end}
    distance = 0
    result = 0
    while len(cheats_and_distances) > 0:
        min_cheat_distance, _ = cheats_and_distances[0]
        if min_cheat_distance + distance > target_distance:
            break
        visited |= positions
        new_positions = set()
        for position in positions:
            if position in cheat_distances:
                for cheat_distance in cheat_distances[position]:
                    if cheat_distance + distance <= target_distance:
                        result += 1
                    cheats_and_distances.remove((cheat_distance, position))
            for vector in vectors:
                new_position = move(position, vector)
                if new_position not in visited | walls:
                    new_positions.add(new_position)
        positions = new_positions
        distance += 1
    return result

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
