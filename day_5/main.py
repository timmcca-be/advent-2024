from example_input import example_input
from puzzle_input import puzzle_input

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

def solve_part_1(input_str):
    iterator = iter(input_str.splitlines())
    rules = get_rules_and_advance_iterator(iterator)
    result = 0
    for line in iterator:
        pages = [int(page) for page in line.split(",")]
        if is_update_valid(rules, pages):
            result += pages[len(pages) // 2]
    return result

def solve_part_2(input_str):
    iterator = iter(input_str.splitlines())
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

print("Part 1 example:", solve_part_1(example_input))
print("Part 1 real:   ", solve_part_1(puzzle_input))
print("Part 2 example:", solve_part_2(example_input))
print("Part 2 real:   ", solve_part_2(puzzle_input))
