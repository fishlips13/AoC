from itertools import cycle

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def coords_sub(coord1, coord2):
    return (coord1[0] - coord2[0], coord1[1] - coord2[1])

def tower_height_smol(jets, rocks):
    jet_it = cycle(jets)
    rock_it = cycle(rocks)

    tower = set()
    height = 0
    for _ in range(2022):
        curr_offset = (2, height + 3)
        rock = next(rock_it)

        while True:
            jet = next(jet_it)
            jet_offset = coords_add(curr_offset, (1, 0) if jet == ">" else (-1, 0))
            rock_after_jet = [coords_add(part, jet_offset) for part in rock]
            if all([part[0] >= 0 and part[0] <= 6 and part not in tower for part in rock_after_jet]):
                curr_offset = jet_offset
            
            grav_offset = coords_add(curr_offset, (0, -1))
            rock_after_grav = [coords_add(part, grav_offset) for part in rock]
            if any([part_dest[1] < 0 or part_dest in tower for part_dest in rock_after_grav]):
                for part in rock:
                    part_freeze = coords_add(part, curr_offset)
                    tower.add(part_freeze)
                    height = max(part_freeze[1] + 1, height)
                break
            
            curr_offset = grav_offset

    return height

def tower_height_lorge(jets, rocks):
    rocks_count = 1000000000000
    jet_it = cycle(enumerate(jets))
    rock_it = cycle(enumerate(rocks))

    tower = set()
    height = 0

    # You can do it!

def parse_data(path):
    with open(path) as f:
        data = f.read()

    return data

def parse_rocks():
    with open("day-17\\rocks_input.txt") as f:
        rock_data = [i.split("\n") for i in f.read().split("\n\n")]

    rocks = []
    for rock_entry in rock_data:
        rock = {(x,y) for y, line in enumerate(reversed(rock_entry)) \
                      for x, char in enumerate(line) if char == "#"}
        rocks.append(rock)    
        
    return rocks

def tests():
    test1_exp = 3068
    test2_exp = 1514285714288

    rocks = parse_rocks()
    data = parse_data("day-17\\test_input.txt")
    test1_res = tower_height_smol(data, rocks)
    test2_res = tower_height_lorge(data, rocks)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    rocks = parse_rocks()
    data = parse_data("day-17\\input.txt")
    answer1 = tower_height_smol(data, rocks)
    answer2 = tower_height_lorge(data, rocks)

    print(f"Part 1 -> : {answer1}")
    print(f"Part 2 -> : {answer2}")

#tests()
puzzle()


#low 1525252525553