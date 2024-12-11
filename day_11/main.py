def count_descendants_unmemoized(stone, generations):
    if generations == 0:
        return 1
    next_generations = generations - 1
    if stone == 0:
        return count_descendants(1, next_generations)
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        midpoint = len(stone_str) // 2
        return (
            count_descendants(int(stone_str[:midpoint]), next_generations)
            + count_descendants(int(stone_str[midpoint:]), next_generations))
    return count_descendants(stone * 2024, next_generations)

memo = dict()
def count_descendants(stone, generations):
    memo_key = (stone, generations)
    if memo_key in memo:
        return memo[memo_key]
    result = count_descendants_unmemoized(stone, generations)
    memo[memo_key] = result
    return result

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
