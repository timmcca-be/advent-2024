# it's like the slidey ice puzzles in pokemon!

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

STARTING_DIRECTION = NORTH
NUM_DIRECTIONS = 4

def rotate(direction):
    return (direction + 1) % NUM_DIRECTIONS

direction_vectors = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0),
}

def move(position, direction):
    vector = direction_vectors[direction]
    return (position[0] + vector[0], position[1] + vector[1])

def is_in_bounds(position, width, height):
    return (
        position[0] >= 0 and position[0] < width
        and position[1] >= 0 and position[1] < height
    )

def parse_input(map):
    obstacles = set()
    for (line_index, line) in enumerate(map):
        for (char_index, char) in enumerate(line):
            position = (char_index, line_index)
            if char == "^":
                guard_position = position
            if char == "#":
                obstacles.add(position)
    height = len(map)
    width = len(map[0])
    return (guard_position, obstacles, width, height)

def guard_step(guard_position, direction, obstacles):
    for i in range(NUM_DIRECTIONS):
        candidate_position = move(guard_position, direction)
        if candidate_position not in obstacles:
            return candidate_position, direction
        direction = rotate(direction)
    return None

def solve_part_1(input_lines):
    guard_position, obstacles, width, height = parse_input(input_lines)
    visited = set()
    direction = STARTING_DIRECTION
    while is_in_bounds(guard_position, width, height):
        visited.add(guard_position)
        step_result = guard_step(guard_position, direction, obstacles)
        if step_result is None:
            print("trapped in loop!")
            break
        guard_position, direction = step_result
    return len(visited)

def will_guard_loop(guard_position, obstacles, width, height):
    direction = STARTING_DIRECTION
    # a set of (direction_entering_turn, guard_position_before_turn) tuples
    visited_turns = set()
    while is_in_bounds(guard_position, width, height):
        step_result = guard_step(guard_position, direction, obstacles)
        if step_result is None:
            return True
        new_position, new_direction = step_result
        if direction != new_direction:
            turn = (direction, guard_position)
            if turn in visited_turns:
                return True
            visited_turns.add(turn)
        guard_position, direction = new_position, new_direction
    return False

def solve_part_2(input_lines):
    starting_position, obstacles, width, height = parse_input(input_lines)
    guard_position = starting_position
    direction = STARTING_DIRECTION
    new_obstacle_positions = set()
    while is_in_bounds(guard_position, width, height):
        step_result = guard_step(guard_position, direction, obstacles)
        if step_result is None:
            print("trapped in loop!")
            break
        new_position, new_direction = step_result
        if (new_position != starting_position
            and new_position not in new_obstacle_positions
            and will_guard_loop(
                starting_position,
                obstacles | {new_position},
                width,
                height,
            )):
            new_obstacle_positions.add(new_position)
        guard_position, direction = new_position, new_direction
    return len(new_obstacle_positions)

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
