def is_in_bounds(map, position):
    return (position[1] >= 0 and position[1] < len(map)
            and position[0] >= 0 and position[0] < len(map[0]))

def at(map, position):
    if not is_in_bounds(map, position):
        return None
    return map[position[1]][position[0]]

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

def enumerate_region(map, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    at_start = at(map, start)
    for vector in vectors:
        new_position = move(start, vector)
        if new_position not in visited and at(map, new_position) == at_start:
            visited.add(new_position)
            visited = enumerate_region(map, new_position, visited)
    return visited

def solve(map, get_region_multiplier):
    unvisited = {(x, y) for y in range(len(map)) for x in range(len(map[0]))}
    result = 0
    while len(unvisited) > 0:
        region = enumerate_region(map, unvisited.pop())
        unvisited -= region
        result += len(region) * get_region_multiplier(region)
    return result

def measure_perimeter(region):
    perimeter = 0
    for position in region:
        for vector in vectors:
            if move(position, vector) not in region:
                perimeter += 1
    return perimeter

def solve_part_1(map):
    return solve(map, measure_perimeter)

corners = [
    (NORTH, EAST),
    (SOUTH, EAST),
    (SOUTH, WEST),
    (NORTH, WEST),
]

def count_corners(region):
    num_corners = 0
    for position in region:
        for corner in corners:
            vertical_vector, horizontal_vector = corner
            diagonal_vector = move(vertical_vector, horizontal_vector)
            matches_vertically = move(position, vertical_vector) in region
            matches_horizontally = move(position, horizontal_vector) in region
            matches_diagonally = move(position, diagonal_vector) in region
            if ((not matches_vertically and not matches_horizontally)
                or (matches_vertically and matches_horizontally
                    and not matches_diagonally)):
                num_corners += 1
    return num_corners

def solve_part_2(map):
    # a polygon always has as many sides as it has corners,
    # so since corners are easy to count we count them instead of sides
    return solve(map, count_corners)

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
