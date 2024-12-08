from example_input import example_input
from puzzle_input import puzzle_input

# it's like the slidey ice puzzles in pokemon!

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def rotate(direction):
    return (direction + 1) % 4

direction_vectors = {
    NORTH: (-1, 0),
    EAST: (0, 1),
    SOUTH: (1, 0),
    WEST: (0, -1),
}

def move(position, direction):
    vector = direction_vectors[direction]
    return (position[0] + vector[0], position[1] + vector[1])

def is_in_bounds(map, position):
    return (
        position[0] >= 0 and position[0] < len(map)
        and position[1] >= 0 and position[1] < len(map[position[0]])
    )

def solve_part_1(input_str):
    map = input_str.splitlines()
    for (line_index, line) in enumerate(map):
        if "^" in line:
            position = (line_index, line.index("^"))
            break
    visited = set()
    direction = NORTH
    while True:
        visited.add(position)
        candidate_position = move(position, direction)
        if not is_in_bounds(map, candidate_position):
            break
        if map[candidate_position[0]][candidate_position[1]] != "#":
            position = candidate_position
            continue
        direction = rotate(direction)
        candidate_position = move(position, direction)
        if not is_in_bounds(map, candidate_position):
            break
        position = candidate_position
    return len(visited)

def solve_part_2(input_str):
    return 0

print("Part 1 example:", solve_part_1(example_input))
print("Part 1 real:   ", solve_part_1(puzzle_input))
print("Part 2 example:", solve_part_2(example_input))
print("Part 2 real:   ", solve_part_2(puzzle_input))
