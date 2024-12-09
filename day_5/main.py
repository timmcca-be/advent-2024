def get_rules_and_advance_iterator(iterator):
    rules = dict()
    for line in iterator:
        if line == "":
            break
        parts = line.split("|")
        prereq = int(parts[0])
        page = int(parts[1])
        if page in rules:
            rules[page].add(prereq)
        else:
            rules[page] = {prereq}
    return rules

def is_update_valid(rules, pages):
    unvisited = set(pages)
    for page in pages:
        prereqs = rules.get(page, set())
        if not unvisited.isdisjoint(prereqs):
            return False
        unvisited.remove(page)
    return True

def solve_part_1(input_lines):
    iterator = iter(input_lines)
    rules = get_rules_and_advance_iterator(iterator)
    result = 0
    for line in iterator:
        pages = [int(page) for page in line.split(",")]
        if is_update_valid(rules, pages):
            result += pages[len(pages) // 2]
    return result

def solve_part_2(input_lines):
    iterator = iter(input_lines)
    rules = get_rules_and_advance_iterator(iterator)
    result = 0
    for line in iterator:
        pages = [int(page) for page in line.split(",")]
        if is_update_valid(rules, pages):
            continue
        unvisited = set(pages)
        for i in range(len(pages) // 2 + 1):
            for page in unvisited:
                if unvisited.isdisjoint(rules.get(page, set())):
                    unvisited.remove(page)
                    break
        result += page
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
print("Part 2:", solve_part_2(input_lines))
