from itertools import permutations

adjacents = set([(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)])

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1], coord1[2] + coord2[2])

def complete_surface_area(grid):
    area = 0

    for cube in grid:
        neighs = [coords_add(cube, adj) for adj in adjacents]
        area += 6 - sum([1 for i in neighs if i in grid])

    return area

def external_surface_area(grid):
    grid_x_min = min([i[0] for i in grid]) - 1
    grid_y_min = min([i[1] for i in grid]) - 1
    grid_z_min = min([i[2] for i in grid]) - 1

    grid_x_max = max([i[0] for i in grid]) + 1
    grid_y_max = max([i[1] for i in grid]) + 1
    grid_z_max = max([i[2] for i in grid]) + 1

    grid_air = set()
    for x in range(grid_x_min, grid_x_max + 1):
        for y in range(grid_y_min, grid_y_max + 1):
            for z in range(grid_z_min, grid_z_max + 1):
                if (x, y, z) not in grid:
                    grid_air.add((x, y, z))

    frontier = {(grid_x_min, grid_y_min, grid_z_min)}
    grid_ext = set([(grid_x_min, grid_y_min, grid_z_min)])

    while frontier:
        cube = frontier.pop()

        for adj in adjacents:
            neigh = coords_add(cube, adj)            
            if neigh in grid_air and neigh not in grid_ext:
                grid_ext.add(neigh)
                frontier.add(neigh)

    area = 0

    for cube in grid:
        neighs = [coords_add(cube, adj) for adj in adjacents]
        area += sum([1 for i in neighs if i in grid_ext])

    return area

def parse_data(path):
    with open(path) as f:
        data = [list(map(int,i.split(","))) for i in f.read().split("\n")]

    return {(x, y, z) for x, y, z in data}

def tests():
    test1_exp = 64
    test2_exp = 58

    data = parse_data("day-18\\test_input.txt")
    test1_res = complete_surface_area(data)
    test2_res = external_surface_area(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-18\\input.txt")
    answer1 = complete_surface_area(data)
    answer2 = external_surface_area(data)

    print(f"Part 1 -> Complete Surface Area: {answer1}")
    print(f"Part 2 -> External Surface Area: {answer2}")

tests()
puzzle()