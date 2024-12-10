from utils import parse_input, move, score

def _clear_space(position, step, boxes, walls):
    if position in walls:
        return False
    if position not in boxes:
        return True
    next_position = move(position, step)
    if not _clear_space(next_position, step, boxes, walls):
        return False
    boxes.remove(position)
    boxes.add(next_position)
    return True

def solve_part_1(input_lines):
    robot, walls, boxes, _, steps = parse_input(input_lines)
    for step in steps:
        next_position = move(robot, step)
        if _clear_space(next_position, step, boxes, walls):
            robot = next_position
    return score(boxes)
