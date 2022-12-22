import re
from copy import deepcopy

def rearrange9000_tops(stacks, instrs):
    for orig, dest, count in instrs:
        for _ in range(count):
            stacks[dest].append(stacks[orig].pop())

    return "".join([stacks[i][-1] for i in range(1, len(stacks) + 1)])

def rearrange9001_tops(stacks, instrs):
    for orig, dest, count in instrs:
        stacks[dest].extend(stacks[orig][-count:])
        stacks[orig] = stacks[orig][:-count]

    return "".join([stacks[i][-1] for i in range(1, len(stacks) + 1)])

def parse_data(path):
    with open(path) as f:
        data = f.read()

    stack_data, instr_data = data.split("\n\n")
    stack_lines = stack_data.split("\n")[:-1]

    stacks = {}
    for line in reversed(stack_lines):
        for i_char in range(1, len(line), 4):
            i_stack = i_char // 4 + 1

            if i_stack not in stacks:
                stacks[i_stack] = []

            if line[i_char] != " ":
                stacks[i_stack].append(line[i_char])

    instrs = []
    for line in instr_data.split("\n"):
        values = list(map(int, re.findall(r"\d+", line)))
        instrs.append((values[1], values[2], values[0]))

    return stacks, instrs

def tests():
    test1_exp = "CMZ"
    test2_exp = "MCD"

    stacks, instrs = parse_data("day-05\\test_input.txt")
    test1_res = rearrange9000_tops(deepcopy(stacks), instrs)
    test2_res = rearrange9001_tops(deepcopy(stacks), instrs)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    stacks, instrs = parse_data("day-05\\input.txt")
    answer1 = rearrange9000_tops(deepcopy(stacks), instrs)
    answer2 = rearrange9001_tops(deepcopy(stacks), instrs)

    print(f"Part 1 -> CrateMover 9000: {answer1}")
    print(f"Part 2 -> CrateMover 9001: {answer2}")

tests()
puzzle()