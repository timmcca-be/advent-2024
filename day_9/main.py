# a lesson in premature optimization: I wrote this function thinking
# "oh there's no way this is doable with the whole expanded filesystem
# in memory." well, there is, it runs in about the same amount of time,
# and it's way easier to read and reason about.
# def solve_part_1(input_str):
#     # character pointers are the index of the character in the string
#     # we're looking at. block pointers are the index of the "block"
#     # on the filesystem within the character in the string.
#     front_character_pointer = 0
#     while input_str[front_character_pointer] == "0":
#         front_character_pointer += 1
#     front_block_pointer = 0
#     front_absolute_pointer = 0
#     # starting at the last character that maps to a file
#     back_character_pointer = ((len(input_str) - 1) // 2) * 2
#     while input_str[back_character_pointer] == "0":
#         back_character_pointer -= 2
#     back_block_pointer = int(input_str[back_character_pointer]) - 1
#     result = 0
#     while (front_character_pointer < back_character_pointer
#            or (front_character_pointer == back_character_pointer
#                and front_block_pointer <= back_block_pointer)):
#         if front_character_pointer % 2 == 0:
#             id = front_character_pointer // 2
#         else:
#             id = back_character_pointer // 2
#             if back_block_pointer == 0:
#                 back_character_pointer -= 2
#                 while input_str[back_character_pointer] == "0":
#                     back_character_pointer -= 2
#                 back_block_pointer = int(
#                     input_str[back_character_pointer]) - 1
#             else:
#                 back_block_pointer -= 1
#         result += front_absolute_pointer * id
#         if front_block_pointer == int(
#             input_str[front_character_pointer]) - 1:
#             front_character_pointer += 1
#             while input_str[front_character_pointer] == "0":
#                 front_character_pointer += 1
#             front_block_pointer = 0
#         else:
#             front_block_pointer += 1
#         front_absolute_pointer += 1
#     return result

def solve_part_1(input_str):
    filesystem = []
    for (i, char) in enumerate(input_str):
        id = i // 2 if i % 2 == 0 else None
        filesystem += [id] * int(char)
    front_pointer = 0
    back_pointer = len(filesystem) - 1
    while filesystem[back_pointer] is None:
        back_pointer -= 1
    while front_pointer < back_pointer:
        if filesystem[front_pointer] is None:
            filesystem[front_pointer], filesystem[back_pointer] = (
                filesystem[back_pointer], filesystem[front_pointer])
            back_pointer -= 1
            while filesystem[back_pointer] is None:
                back_pointer -= 1
        front_pointer += 1
    result = 0
    for (i, id) in enumerate(filesystem):
        if id is not None:
            result += i * id
    return result

# I want to return to this and clean it up. it's pretty spaghetti-ish
# right now, but I think I need to step away so I can get a fresh
# perspective to make it better.
def solve_part_2(input_str):
    segments = []
    for (i, char) in enumerate(input_str):
        size = int(char)
        if size == 0:
            continue
        id = i // 2 if i % 2 == 0 else None
        if len(segments) > 0:
            last_segment_index = len(segments) - 1
            last_id, last_size = segments[last_segment_index]
        else:
            last_id = None
        if id == last_id:
            segments[last_segment_index] = (id, size + last_size)
        else:
            segments.append((id, size))
    pointer = len(segments) - 1
    while pointer > 0:
        id, size = segments[pointer]
        if id is None:
            pointer -= 1
            continue
        for i in range(pointer):
            candidate_id, candidate_size = segments[i]
            if candidate_id is not None or candidate_size < size:
                continue
            segments[i] = (id, size)
            # we don't care about keeping later segments contiguous
            segments[pointer] = (None, size)
            if candidate_size > size:
                next_id, next_size = segments[i + 1]
                if next_id is None:
                    segments[i + 1] = (None, next_size + candidate_size - size)
                else:
                    segments.insert(i + 1, (None, candidate_size - size))
                    pointer += 1
            break
        pointer -= 1
    absolute_pointer = 0
    result = 0
    for (i, segment) in enumerate(segments):
        id, size = segment
        if id is None:
            absolute_pointer += size
            continue
        for i in range(size):
            result += id * absolute_pointer
            absolute_pointer += 1
    return result

eof_indicator = "<<eof>>"
print(f"Enter the puzzle input, followed by {eof_indicator} "
      + "on its own line:")
input_str = ""
while True:
    line = input()
    if line.strip() == eof_indicator:
        break
    input_str += line.strip().replace(" ", "")

print("Part 1:", solve_part_1(input_str))
print("Part 2:", solve_part_2(input_str))
