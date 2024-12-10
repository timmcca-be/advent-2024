from utils import move, parse_input, score

def _transform_position(position):
    x, y = position
    return 2 * x, y

def _at(position, map):
    if position in map:
        return position
    prior_position = move(position, "<")
    if prior_position in map:
        return prior_position
    return None

def _get_affected_boxes_if_moveable(position, step, boxes, walls):
    if _at(position, walls) is not None:
        return None
    box = _at(position, boxes)
    if box is None:
        return set()
    left = box
    right = move(box, ">")
    if step == "<":
        candidates = [left]
    elif step == ">":
        candidates = [right]
    else:
        candidates = [left, right]
    affected = {box}
    for candidate in candidates:
        downstream = _get_affected_boxes_if_moveable(
            move(candidate, step), step, boxes, walls)
        if downstream is None:
            return None
        affected |= downstream
    return affected

def _char_to_print(position, robot, boxes, walls):
    if position == robot:
        return "@"
    if _at(position, walls) is not None:
        return "#"
    box = _at(position, boxes)
    if box is None:
        return "."
    if box == position:
        return "["
    return "]"

def _print_map(robot, boxes, walls, dimensions):
    width, height = dimensions
    for y in range(height):
        print("".join(
            _char_to_print((x, y), robot, boxes, walls)
            for x in range(width)))

def solve_part_2(input_lines):
    robot, walls, boxes, dimensions, steps = parse_input(input_lines)
    robot = _transform_position(robot)
    walls = set(_transform_position(position) for position in walls)
    boxes = set(_transform_position(position) for position in boxes)
    dimensions = _transform_position(dimensions)
    # _print_map(robot, boxes, walls, dimensions)
    for step in steps:
        next_position = move(robot, step)
        affected_boxes = _get_affected_boxes_if_moveable(
            next_position, step, boxes, walls)
        if affected_boxes is not None:
            for box in affected_boxes:
                boxes.remove(box)
            for box in affected_boxes:
                boxes.add(move(box, step))
            robot = next_position
        # print(step)
        # _print_map(robot, boxes, walls, dimensions)
        # input("press enter to continue: ")
    # _print_map(robot, boxes, walls, dimensions)
    return score(boxes)
