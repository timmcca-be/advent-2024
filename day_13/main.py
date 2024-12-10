import re
import math

def get_number_pair(line):
    numbers = [int(number) for number in re.findall(r"\d+", line)]
    return (numbers[0], numbers[1])

def parse_input(input_lines):
    machines = []
    for i in range((len(input_lines) + 1) // 4):
        machines.append((
            get_number_pair(input_lines[4*i]),
            get_number_pair(input_lines[4*i + 1]),
            get_number_pair(input_lines[4*i + 2]),
        ))
    return machines

def get_tokens(machine):
    a_vector, b_vector, target = machine
    # an a press is an a press, you can't say it's only a half
    current_a_presses = 0
    a_x, a_y = a_vector
    b_x, b_y = b_vector
    target_x, target_y = target
    while (current_a_presses * a_x <= target_x
           and current_a_presses * a_y <= target_y):
        remaining_x = target_x - current_a_presses * a_x
        remaining_y = target_y - current_a_presses * a_y
        if (remaining_x % b_x == 0 and remaining_y % b_y == 0
            and remaining_x // b_x == remaining_y // b_y):
            num_b_presses = remaining_x // b_x
            return 3 * current_a_presses + num_b_presses
        current_a_presses += 1
    return 0

def solve_part_1(input_lines):
    machines = parse_input(input_lines)
    results = [get_tokens_2(machine) for machine in machines]
    return sum(results)

def time_to_loop(a, b):
    return b // math.gcd(a, b)

def first_match(a, b, target):
    for i in range(time_to_loop(a, b)):
        if (target - a * i) % b == 0:
            return i
    return None

# I did my best to explain my reasoning here, but really I worked through
# this in a mathematical fugue state and I can't quite explain why it all
# works.
def get_tokens_2(machine):
    a_vector, b_vector, target = machine
    a_x, a_y = a_vector
    b_x, b_y = b_vector
    target_x, target_y = target
    # first goal: find the lowest number of A presses at which
    # the remaining x distance is divisible by the x distance
    # traveled when the B button is pressed,
    # and the lowest number of A presses at which the remaining
    # y distance is divisible by the y distance traveled when the
    # B button is pressed.
    a_match_x = first_match(a_x, b_x, target_x)
    a_match_y = first_match(a_y, b_y, target_y)
    if a_match_x is None or a_match_y is None:
        return 0
    # these are the increments we can add to a_match_x and a_match_y
    # respectively while keeping the remaining distance divisible by
    # the distance traveled by pressing B
    loop_x = time_to_loop(a_x, b_x)
    loop_y = time_to_loop(a_y, b_y)
    # if the remaining diff ever repeats, we know we're trapped in
    # a cycle and it's not possible to get a_match_x to equal a_match_y.
    visited_diffs = set()
    # now we increment each until we find a point at which *both*
    # the remaining x and y distance are divisible by the distance
    # traveled in the respective direction by pressing the B button.
    while a_match_x != a_match_y:
        diff = a_match_x - a_match_y
        if diff in visited_diffs:
            return 0
        visited_diffs.add(diff)
        if a_match_x < a_match_y:
            a_match_x += loop_x
        else:
            a_match_y += loop_y
        if a_match_x * a_x > target_x or a_match_y * a_y > target_y:
            return 0
    a_match = a_match_x
    # now the remaining distances in each direction are both
    # divisible by the distance traveled in their respective
    # direction by pressing the B button, but we need that to be
    # the same number of B presses. first we find out the
    # difference between the number of B presses each requires.
    remaining_b_x = (target_x - a_match * a_x) // b_x
    remaining_b_y = (target_y - a_match * a_y) // b_y
    remaining_b_diff = remaining_b_x - remaining_b_y
    if remaining_b_diff == 0:
        return 3 * a_match + (target_x - a_match * a_x) // b_x
    # (the smallest number of a presses we can add while preserving
    # divisibility)
    match_increment = math.lcm(loop_x, loop_y)
    # then we find out how much each valid increment of A presses shrinks
    # that difference.
    b_x_drop_per_increment = match_increment * a_x // b_x
    b_y_drop_per_increment = match_increment * a_y // b_y
    b_diff_per_increment = b_x_drop_per_increment - b_y_drop_per_increment
    if (
        # first two conditions: adding more A presses will make the difference
        # in required B presses larger.
        (b_diff_per_increment < 0 and remaining_b_diff > 0)
        or (b_diff_per_increment > 0 and remaining_b_diff < 0)
        # adding more A presses will not change the difference in required
        # B presses.
        or b_diff_per_increment == 0
        # the difference will cross 0 without ever being 0
        or remaining_b_diff % b_diff_per_increment != 0):
        return 0
    # and finally we add just enough A presses to reduce the
    # difference to 0
    num_a_presses = (a_match
        + (remaining_b_diff // b_diff_per_increment) * match_increment)
    num_b_presses = (target_x - num_a_presses * a_x) // b_x
    return 3 * num_a_presses + num_b_presses

def solve_part_2(input_lines):
    machines = parse_input(input_lines)
    for i in range(len(machines)):
        a_vector, b_vector, target = machines[i]
        target_x, target_y = target
        machines[i] = (a_vector, b_vector,
                       (target_x + 10000000000000, target_y + 10000000000000))
    return sum(get_tokens_2(machine) for machine in machines)

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
