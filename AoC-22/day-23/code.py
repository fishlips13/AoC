from itertools import cycle
from collections import defaultdict
from copy import deepcopy

# N -> S -> W -> E
directions =   [(( 0,-1), ( 1,-1), (-1,-1)),
                (( 0, 1), ( 1, 1), (-1, 1)),
                ((-1, 0), (-1, 1), (-1,-1)),
                (( 1, 0), ( 1, 1), ( 1,-1))]

adjacents = set([j for i in directions for j in i])

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def empty_after_10(elves):
    direction_it = cycle(directions)
    
    for _ in range(10):
        elves_round(elves, direction_it)

    x_min, x_max, y_min, y_max = get_bounds(elves)

    area = (x_max - x_min + 1) * (y_max - y_min + 1)

    return area - len(elves)

def total_rounds(elves):
    round_count = 1
    direction_it = cycle(directions)
    
    while True:
        if elves_round(elves, direction_it) == len(elves):
            return round_count
        
        round_count += 1

def elves_round(elves, direction_it):
    elves_done = set()
    cell_candis = defaultdict(list)

    for elf_curr in elves:
        if all([coords_add(elf_curr, adj) not in elves for adj in adjacents]):
            elves_done.add(elf_curr)

    elves_stationary = len(elves_done)

    # Python Cycle cycles all elements when the iterator is zipped with its iterable
    # But for some reason the next time it cycles around, the 2nd element is the start point
    # Perhaps this is some weird quirk with zip or maybe I'm missing something
    # I was going to discard the next cycled element to achieve this effect but this works I guess ...
    for direction, _ in zip(direction_it, directions):
        for elf_curr in elves - elves_done:
            if all([coords_add(elf_curr, direc) not in elves for direc in direction]):
                target_cell = coords_add(elf_curr, direction[0])
                elves_done.add(elf_curr)
                cell_candis[target_cell].append(elf_curr)
    
    for dest, candi_elves in cell_candis.items():
        if len(candi_elves) > 1:
            continue

        elves.remove(candi_elves[0])
        elves.add(dest)

    return elves_stationary

def get_bounds(elves):
    x_min, x_max, y_min, y_max = 0, 0, 0, 0
    for elf in elves:
        x_min = min(x_min, elf[0])
        x_max = max(x_max, elf[0])
        y_min = min(y_min, elf[1])
        y_max = max(y_max, elf[1])

    return x_min, x_max, y_min, y_max

def draw(elves):
    x_min, x_max, y_min, y_max = get_bounds(elves)
    for y in range(y_min, y_max + 1):
        line = []
        for x in range(x_min, x_max + 1):
            if (x,y) in elves:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print()

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    elves = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                elves.add((x,y))

    return elves

def tests():
    test1_exp = 110
    test2_exp = 20

    data = parse_data("day-23\\test_input.txt")
    test1_res = empty_after_10(deepcopy(data))
    test2_res = total_rounds(deepcopy(data))

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-23\\input.txt")
    answer1 = empty_after_10(deepcopy(data))
    answer2 = total_rounds(deepcopy(data))

    print(f"Part 1 -> Empty Spaces After 10 Rounds: {answer1}")
    print(f"Part 2 -> Rounds Until Complete: {answer2}")

tests()
puzzle()