def solve_part_1(input_str):
    return 0

def solve_part_2(input_str):
    return 0

print("Note that line breaks will be ignored in inputs due to limitations of "
     + "the platform. If you need them to be respected, work out another "
     + "solution, like adding a particular character to the end of every line "
     + "before pasting the input into the terminal. Delete this warning once "
     + "you've worked out a solution.")
eof_indicator = "<<eof>>"
print(f"Enter the puzzle input, followed by {eof_indicator} on its own line:")
input_str = ""
while True:
    line = input()
    if line == eof_indicator:
        break
    input_str += line

print("Part 1:", solve_part_1(input_str))
print("Part 2:", solve_part_2(input_str))
