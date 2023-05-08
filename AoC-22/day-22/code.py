import re




facing_lookup = {(1,0) : 0, (0,1) : 1, (-1,0) : 2,  (0,-1) : 3}

class CoordIter:
    def __init__(self, start, end):
        mag_x = abs(end[0] - start[0])
        max_y = abs(end[1] - start[1])
        step_x = ((end[0] - start[0]) // mag_x) if mag_x != 0 else 0
        step_y = ((end[1] - start[1]) // max_y) if max_y != 0 else 0
        self.step = (step_x, step_y)

        self.current = start
        self.end = coords_add(end, self.step)

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.current
        self.current = coords_add(self.current, self.step)
        if temp != self.end:
            return temp
        raise StopIteration

def build_cube_wrap_lookup():
    cube_wrap_lookup = {}

    # t1 = (51,1) (100, 1) # R
    # t10 = (1, 151) (1, 200) # L
    for coord1, coord10 in zip(CoordIter((51,1), (100, 1)), CoordIter((1, 151), (1, 200))):
        cube_wrap_lookup[(coord1, (0, -1))] = (coord10, (1, 0))
        cube_wrap_lookup[(coord10, (-1, 0))] = (coord1, (0, 1))

    # t2 = (101, 1) (150, 1) # Nothing
    # t9 = (1, 200) (50, 200) # Nothing
    for coord2, coord9 in zip(CoordIter((101, 1), (150, 1)), CoordIter((1, 200), (50, 200))):
        cube_wrap_lookup[(coord2, (0, -1))] = (coord9, (0, -1))
        cube_wrap_lookup[(coord9, (0, 1))] = (coord2, (0, 1))

    # t4 = (101, 50) (150, 50) # R
    # t5 = (100, 51) (100, 100) # L
    for coord4, coord5 in zip(CoordIter((101, 50), (150, 50)), CoordIter((100, 51), (100, 100))):
        cube_wrap_lookup[(coord4, (0, 1))] = (coord5, (-1, 0))
        cube_wrap_lookup[(coord5, (1, 0))] = (coord4, (0, -1))

    # t12 = (1, 101) (50, 101) # R
    # t13 = (51, 51) (51, 100) # L
    for coord12, coord13 in zip(CoordIter((1, 101), (50, 101)), CoordIter((51, 51), (51, 100))):
        cube_wrap_lookup[(coord12, (0, -1))] = (coord13, (1, 0))
        cube_wrap_lookup[(coord13, (-1, 0))] = (coord12, (0, 1))

    # t7 = (51, 150) (100, 150) # R
    # t8 = (50, 150) (50, 200) # L
    for coord7, coord8 in zip(CoordIter((51, 150), (100, 150)), CoordIter((50, 150), (50, 200))):
        cube_wrap_lookup[(coord7, (0, 1))] = (coord8, (-1, 0))
        cube_wrap_lookup[(coord8, (1, 0))] = (coord7, (0, -1))

    # t3 = (150, 1) (150, 50) # REVERSE
    # t6 = (100, 150) (100, 101) # REVERSE
    for coord3, coord6 in zip(CoordIter((150, 1), (150, 50)), CoordIter((100, 150), (100, 101))):
        cube_wrap_lookup[(coord3, (1, 0))] = (coord6, (-1, 0))
        cube_wrap_lookup[(coord6, (1, 0))] = (coord3, (-1, 0))

    # t11 = (1, 101) (1, 150) # REVERSE
    # t14 = (51, 50) (51, 1) # REVERSE
    for coord11, coord14 in zip(CoordIter((1, 101), (1, 150)), CoordIter((51, 50), (51, 1))):
        cube_wrap_lookup[(coord11, (-1, 0))] = (coord14, (1, 0))
        cube_wrap_lookup[(coord14, (-1, 0))] = (coord11, (1, 0))

    return cube_wrap_lookup

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def coords_sub(coord1, coord2):
    return (coord1[0] - coord2[0], coord1[1] - coord2[1])

def find_password(map_data, cube = False):
    grid, pos_curr, facing, instrs = map_data

    cube_wrap_lookup = build_cube_wrap_lookup()

    for instr in instrs:
        if instr == "L":
            facing = (facing[1], -facing[0])
            continue
        elif instr == "R":
            facing = (-facing[1], facing[0])
            continue

        pos_next = pos_curr
        for _ in range(instr):

            pos_next = coords_add(pos_next, facing)
            facing_next = facing
            if pos_next not in grid:
                if cube:
                    pos_next, facing_next = cube_wrap_lookup[(pos_curr, facing)]
                else:
                    pos_next = wrap_flat(grid, pos_curr, facing)

            if grid[pos_next] == "#":
                break

            pos_curr = pos_next
            facing = facing_next

    return pos_curr[1] * 1000 + pos_curr[0] * 4 + facing_lookup[facing]

def wrap_flat(grid, pos_curr, facing):
    wrap_pos = pos_curr

    while wrap_pos in grid:
        wrap_pos = coords_sub(wrap_pos, facing)

    return coords_add(wrap_pos, facing)

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n\n")

    grid = {}
    start = None
    for y, line in enumerate(data[0].split("\n"), 1):
        for x, cell in enumerate(line, 1):
            if cell != " ":
                grid[(x,y)] = cell
                if start == None:
                    start = (x,y)
    
    moves = re.findall(r"\d+|\w", data[1])
    instrs = [int(i) if i.isdigit() else i for i in moves]

    return grid, start, (1,0), instrs

def tests():
    test1_exp = 6032
    test2_exp = None

    data = parse_data("day-22\\test_input.txt")
    test1_res = find_password(data)
    #test2_res = find_password(data, True)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    #assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-22\\input.txt")
    answer1 = find_password(data)
    answer2 = find_password(data, True)

    print(f"Part 1 -> : {answer1}")
    print(f"Part 2 -> : {answer2}")

tests()
puzzle()


# low 20214