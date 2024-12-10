def get_children(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        midpoint = len(stone_str) // 2
        return [int(stone_str[:midpoint]),
                int(stone_str[midpoint:])]
    return [stone * 2024]

memo = dict()
def count_descendants(stone, generations):
    if generations == 0:
        return 1
    memo_key = (stone, generations)
    if memo_key not in memo:
        memo[memo_key] = sum(count_descendants(child, generations - 1)
                             for child
                             in get_children(stone))
    return memo[memo_key]

def solve(input_str, generations):
    stones = [int(stone) for stone in input_str.strip().split(" ")]
    return sum(count_descendants(stone, generations) for stone in stones)

def solve_part_1(input_str):
    return solve(input_str, 25)

def solve_part_2(input_str):
    return solve(input_str, 75)

input_str = input("Puzzle input: ")

print("Part 1:", solve_part_1(input_str))
print("Part 2:", solve_part_2(input_str))
