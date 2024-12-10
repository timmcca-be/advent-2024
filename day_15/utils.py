def parse_input(input_lines):
    walls = set()
    boxes = set()
    iterator = enumerate(input_lines)
    while True:
        line_index, line = next(iterator)
        if line == "":
            break
        width = len(line)
        for (char_index, char) in enumerate(line):
            position = (char_index, line_index)
            if char == "#":
                walls.add(position)
            if char == "O":
                boxes.add(position)
            if char == "@":
                robot = position
    height = line_index
    steps = ""
    for _, line in iterator:
        steps += line.strip()
    return robot, walls, boxes, (width, height), steps

_vectors = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

def move(position, step):
    vector = _vectors[step]
    return (
        position[0] + vector[0],
        position[1] + vector[1]
    )

def score(boxes):
    return sum(100 * y + x for x, y in boxes)
