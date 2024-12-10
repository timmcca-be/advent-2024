import re

def parse_input(input_lines):
    dimensions = [
        int(dimension) for dimension in re.findall(r"\d+", input_lines[0])]
    width = dimensions[0]
    height = dimensions[1]
    guards = []
    for line in input_lines[1:]:
        numbers = [int(number) for number in re.findall(r"-?\d+", line)]
        position = (numbers[0], numbers[1])
        velocity = (numbers[2], numbers[3])
        guards.append((position, velocity))
    return ((width, height), guards)

def get_result_positions(dimensions, guards, num_iterations):
    width, height = dimensions
    results = []
    for guard in guards:
        position, velocity = guard
        position_x, position_y = position
        velocity_x, velocity_y = velocity
        result_x = (position_x + velocity_x * num_iterations) % width
        result_y = (position_y + velocity_y * num_iterations) % height
        results.append((result_x, result_y))
    return results

def solve_part_1(input_lines):
    dimensions, guards = parse_input(input_lines)
    width, height = dimensions
    center_x = width // 2
    center_y = height // 2
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for result_x, result_y in get_result_positions(dimensions, guards, 100):
        x_dist_from_center = result_x - center_x
        y_dist_from_center = result_y - center_y
        if x_dist_from_center > 0 and y_dist_from_center < 0:
            q1 += 1
        elif x_dist_from_center > 0 and y_dist_from_center > 0:
            q2 += 1
        elif x_dist_from_center < 0 and y_dist_from_center > 0:
            q3 += 1
        elif x_dist_from_center < 0 and y_dist_from_center < 0:
            q4 += 1
    return q1 * q2 * q3 * q4

# what does this even mean??
# after a few iterations, I landed on "christmas trees are symmetrical",
# which got me the answer, despite not *quite* being correct since the
# tree isn't centered.
def looks_like_christmas_tree(dimensions, result_positions):
    width, height = dimensions
    result_positions_set = set(result_positions)
    num_symmetrical = 0
    for result_x, result_y in result_positions:
        if (width - 1 - result_x, result_y) in result_positions_set:
            num_symmetrical += 1
    symmetry_threshold = 0.3
    symmetry = num_symmetrical / len(result_positions)
    return symmetry > symmetry_threshold

def print_result(dimensions, result_positions):
    width, height = dimensions
    lines_to_print = ["." * (width + 1)] * (height + 1)
    for result_x, result_y in result_positions:
        line = lines_to_print[result_y]
        lines_to_print[result_y] = (
            line[:result_x] + "#" + line[result_x+1:])
    for line in lines_to_print:
        print(line)

def solve_part_2(input_lines):
    dimensions, guards = parse_input(input_lines)
    width, height = dimensions
    i = 0
    while True:
        result_positions = get_result_positions(dimensions, guards, i)
        if looks_like_christmas_tree(dimensions, result_positions):
            print_result(dimensions, result_positions)
            input_str = input(
                "press enter to continue or a + enter to accept: ")
            if input_str == "a":
                return i
        i += 1

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
