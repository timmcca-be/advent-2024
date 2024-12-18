def parse_input(input_lines):
    size = int(input_lines[0])
    num_bytes_fallen = int(input_lines[1])
    byte_locations = []
    for line in input_lines[2:]:
        parts = line.split(",")
        byte_locations.append((int(parts[0]), int(parts[1])))
    return size, num_bytes_fallen, byte_locations

def is_in_bounds(size, position):
    return (position[1] >= 0 and position[1] < size
            and position[0] >= 0 and position[0] < size)

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

def solve_part_1_parsed(size, num_bytes_fallen, byte_locations):
    fallen_bytes = set(byte_locations[:num_bytes_fallen])
    visited = set()
    positions = {(0, 0)}
    target_position = (size - 1, size - 1)
    distance = 0
    while len(positions) > 0:
        visited |= positions
        distance += 1
        new_positions = set()
        for position in positions:
            for vector in vectors:
                new_position = move(position, vector)
                if (is_in_bounds(size, new_position)
                    and new_position not in fallen_bytes | visited):
                    new_positions.add(new_position)
        if target_position in new_positions:
            return distance
        positions = new_positions
    return None

def solve_part_1(input_lines):
    size, num_bytes_fallen, byte_locations = parse_input(input_lines)
    result = solve_part_1_parsed(size, num_bytes_fallen, byte_locations)
    if result is None:
        raise Exception("unsolvable")
    return result

def binary_search(min, max, evaluate):
    while min != max:
        test = min + (max - min) // 2
        if evaluate(test):
            max = test
        else:
            min = test + 1
    return min

def solve_part_2(input_lines):
    size, _, byte_locations = parse_input(input_lines)
    first_unsolvable_num_bytes = binary_search(0, len(byte_locations) - 1,
            lambda num_fallen_bytes: solve_part_1_parsed(
                size, num_fallen_bytes, byte_locations) is None)
    return byte_locations[first_unsolvable_num_bytes - 1]

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
