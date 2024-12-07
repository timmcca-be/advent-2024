from example_input import example_input
from puzzle_input import puzzle_input

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

def parse_input(input_str):
    map = input_str.splitlines()
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

def solve_part_1(input_str):
    guard_position, obstacles, width, height = parse_input(input_str)
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

def solve_part_2(input_str):
    starting_position, obstacles, width, height = parse_input(input_str)
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

print("Part 1 example:", solve_part_1(example_input))
print("Part 1 real:   ", solve_part_1(puzzle_input))
print("Part 2 example:", solve_part_2(example_input))
print("Part 2 real:   ", solve_part_2(puzzle_input))
