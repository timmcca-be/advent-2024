from heapq import heappush, heappop

# anybody who has taken an algorithms class read 1/8 of today's
# challenge and immediately started trying to remember how to spell
# dijkstra.
# sadly we don't have content about dijkstra's algorithm on khan
# yet! maybe i should make some.

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

STARTING_DIRECTION = EAST
NUM_DIRECTIONS = 4

def rotate_clockwise(direction):
    return (direction + 1) % 4

def rotate_counterclockwise(direction):
    return (direction - 1) % 4

direction_vectors = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0),
}

def move(position, direction):
    vector = direction_vectors[direction]
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

ROTATE_PENALTY = 1000

def get_optimal_states(
    reverse_optimal_path_lookup, current, visited = None):
    if visited is None:
        visited = set()
    if current in visited:
        return visited
    visited.add(current)
    for prior in reverse_optimal_path_lookup.get(current, set()):
        visited = get_optimal_states(
            reverse_optimal_path_lookup, prior, visited)
    return visited

def get_char_at_position(position, walls, optimal_locations):
    if position in walls:
        return "#"
    if position in optimal_locations:
        return "O"
    return "."

def print_result(walls, optimal_locations, dimensions):
    width, height = dimensions
    for y in range(height):
        print("".join(
            get_char_at_position((x, y), walls, optimal_locations)
            for x in range(width)
        ))

def solve(input_lines):
    start, end, walls, dimensions = parse_input(input_lines)
    priority_queue = [(0, ((start, STARTING_DIRECTION), None))]
    visited = set()
    optimal_distances = {start: 0}
    reverse_optimal_path_lookup = dict()
    shortest_distance_to_end = None
    while len(priority_queue) > 0:
        distance, state = heappop(priority_queue)
        if state in visited:
            continue
        visited.add(state)
        current, prior = state
        if current == prior:
            raise Exception(current)
        position, direction = current
        if (shortest_distance_to_end is not None
            and distance > shortest_distance_to_end):
            break
        if position == end:
            shortest_distance_to_end = distance
        if prior is not None and current not in optimal_distances:
            optimal_distances[current] = distance
            reverse_optimal_path_lookup[current] = {prior}
        elif prior is not None and distance == optimal_distances[current]:
            reverse_optimal_path_lookup[current].add(prior)
        rotated_clockwise = ((position, rotate_clockwise(direction)), current)
        if rotated_clockwise not in visited:
            heappush(priority_queue,
                (distance + ROTATE_PENALTY, rotated_clockwise))
        rotated_counterclockwise = (
            (position, rotate_counterclockwise(direction)), current)
        if rotated_counterclockwise not in visited:
            heappush(priority_queue,
                (distance + ROTATE_PENALTY, rotated_counterclockwise))
        next_position = move(position, direction)
        next_state = ((next_position, direction), current)
        if next_position not in walls and next_state not in visited:
            heappush(priority_queue, (distance + 1, next_state))
    print("Part 1:", min(
        optimal_distances[end, direction]
        for direction in range(NUM_DIRECTIONS)
        if (end, direction) in optimal_distances))
    optimal_locations = set()
    for direction in range(NUM_DIRECTIONS):
        optimal_locations |= set(
            position
            for position, _ in get_optimal_states(
                reverse_optimal_path_lookup, (end, direction)))
    # print_result(walls, optimal_locations, dimensions)
    print("Part 2:", len(optimal_locations))

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

solve(input_lines)