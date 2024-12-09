import itertools

def parse_input(map):
    antennae = dict()
    for (line_index, line) in enumerate(map):
        for (char_index, char) in enumerate(line):
            if char == ".":
                continue
            location = (char_index, line_index)
            if char in antennae:
                antennae[char].append(location)
            else:
                antennae[char] = [location]
    width = len(map[0])
    height = len(map)
    return antennae, width, height

def flip_location(reference_location, location_to_flip):
    return (
        2 * reference_location[0] - location_to_flip[0],
        2 * reference_location[1] - location_to_flip[1],
    )

def is_in_bounds(position, width, height):
    return (
        position[0] >= 0 and position[0] < width
        and position[1] >= 0 and position[1] < height
    )

def solve_part_1(input_lines):
    antennae, width, height = parse_input(input_lines)
    antinodes = set()
    for locations in antennae.values():
        for pair in itertools.permutations(locations, 2):
            antinode = flip_location(pair[0], pair[1])
            if is_in_bounds(antinode, width, height):
                antinodes.add(antinode)
    return len(antinodes)

def solve_part_2(input_lines):
    antennae, width, height = parse_input(input_lines)
    antinodes = set()
    for locations in antennae.values():
        for pair in itertools.permutations(locations, 2):
            head = pair[0]
            tail = pair[1]
            while is_in_bounds(head, width, height):
                antinodes.add(head)
                head, tail = flip_location(head, tail), head
    return len(antinodes)

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
