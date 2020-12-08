def test_run(program):
    accumulator = 0
    index = 0
    visited_indicies = set()

    while True:
        if index in visited_indicies:
            return accumulator, False
        elif index == len(program):
            return accumulator, True

        instruction = program[index]
        visited_indicies.add(index)

        if instruction[0] == "acc":
            accumulator += instruction[1]

        index += instruction[1] if instruction[0] == "jmp" else 1

def swap_jmp_nop(instruction):
    if instruction[0] == "jmp":
        instruction[0] = "nop"
    elif instruction[0] == "nop":
        instruction[0] = "jmp"

with open("input/08.txt") as f:
    program = [[i.split(" ")[0], int(i.split(" ")[1])] for i in f.read().split("\n")]

print(f"Original Final Accumulator: {test_run(program)[0]}")

for instruction in program:
    swap_jmp_nop(instruction)

    acc, success = test_run(program)

    swap_jmp_nop(instruction)

    if success:
        print(f"Modded Final Accumulator: {acc}")
        break