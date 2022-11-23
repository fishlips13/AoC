from itertools import permutations
from copy import deepcopy

def flip(grid:dict):
    grid_new = {}
    size = int(len(grid) ** 0.5)
    for coord, content in grid.items():
        grid_new[coord[0], size - coord[1]] = content
    return grid_new

def rotate(grid:dict):
    grid_new = {}
    size = int(len(grid) ** 0.5)
    for coord, content in grid.items():
        grid_new[size - coord[1], coord[0]] = content
    return grid_new

def grid_to_str(grid:dict):
    grid_list = list(grid.keys())
    grid_list.sort()
    return "".join([grid[i] for i in grid_list])

def add_coords(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

twos   = ((0,0), (0,1),
          (1,0), (1,1))
threes = ((0,0), (0,1), (0,2),
          (1,0), (1,1), (1,2),
          (2,0), (2,1), (2,2))
fours  = ((0,0), (0,1), (0,2), (0,3),
          (1,0), (1,1), (1,2), (1,3),
          (2,0), (2,1), (2,2), (2,3),
          (3,0), (3,1), (3,2), (3,3))

transforms = [lambda x : rotate(x), lambda x : rotate(x), lambda x : rotate(x),
              lambda x : flip(x),
              lambda x : rotate(x), lambda x : rotate(x), lambda x : rotate(x)]

with open("input\\21.txt") as f:
    data = [i.split(" => ") for i in f.read().replace("/", "").split("\n")]

rules = {i[0] : i[1] for i in data}
grid_base = {(0,0) : ".", (0,1) : "#", (0,2) : ".",
        (1,0) : ".", (1,1) : ".", (1,2) : "#",
        (2,0) : "#", (2,1) : "#", (2,2) : "#"}

def do_art(iterations):
    grid = deepcopy(grid_base)

    for _ in range(iterations):
        grid_new = {}
        grid_size = int(len(grid) ** 0.5)

        if grid_size % 2 == 0:
            chunk_size = 2
            offset_orig = twos
            offset_new = threes
        else:
            chunk_size = 3
            offset_orig = threes
            offset_new = fours

        chunk_row_count = grid_size // chunk_size
        for x in range(chunk_row_count):
            for y in range(chunk_row_count):
                anchor_orig = (x * chunk_size, y * chunk_size)
                chunk_grid = {i : grid[add_coords(i, anchor_orig)] for i in offset_orig}

                rule_match = None
                for transform in transforms:

                    chunk_str = grid_to_str(chunk_grid)
                    if chunk_str in rules:
                        rule_match = rules[chunk_str]
                        break

                    chunk_grid = transform(chunk_grid)

                anchor_new = add_coords(anchor_orig, (x, y))

                for offset, state in zip(offset_new, rule_match):
                    grid_new[add_coords(offset, anchor_new)] = state

        grid = grid_new

    return grid

art_5  = do_art(5)
art_18 = do_art(18)

on_count_5  = sum([1 if i == "#" else 0 for i in art_5.values()])
on_count_18 = sum([1 if i == "#" else 0 for i in art_18.values()])

print(f"On Count (5): {on_count_5}")
print(f"On Count (18): {on_count_18}")