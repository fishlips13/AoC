from copy import deepcopy

sand_moves = [(0,1), (-1,1), (1,1)]

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def find_rest_count(grid_data):
    grid, _ = grid_data
    rest_count = 0

    while True:
        sand = (500,0)

        while True:
            placed = True
            for move in sand_moves:
                dest = coords_add(sand, move)
                if dest not in grid:
                    return rest_count
                
                if grid[dest] == ".":
                    sand = dest
                    placed = False
                    break
            
            if placed:
                grid[sand] = "o"
                rest_count += 1
                break

def find_rest_count_floor(grid_data):
    grid, grid_y_max = grid_data
    rest_count = 0

    while True:
        sand = (500,0)

        while True:
            placed = True
            for move in sand_moves:
                dest = coords_add(sand, move)
                if dest[1] == grid_y_max + 2:
                    grid[dest] = "#"
                elif dest not in grid:
                    grid[dest] = "."
                
                if grid[dest] == ".":
                    sand = dest
                    placed = False
                    break
            
            if placed:
                grid[sand] = "o"
                rest_count += 1

                if sand == (500,0):
                    return rest_count

                break

def print_grid(grid, x_min, x_max, y_min, y_max):
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            if (x,y) in grid:
                row += grid[(x,y)]
            else:
                row += "."
        print("".join(row))

def parse_data(path):
    with open(path) as f:
        data = [[list(map(int, j.split(","))) for j in i.split(" -> ")] for i in f.read().split("\n")]

    grid_x_min, grid_x_max = 9999999, 0
    grid_y_min, grid_y_max = 0, 0

    grid = {}
    for line in data:
        for coord1, coord2 in zip(line, line[1:]):
            x_min, x_max = min(coord1[0], coord2[0]), max(coord1[0], coord2[0])
            y_min, y_max = min(coord1[1], coord2[1]), max(coord1[1], coord2[1])

            grid_x_min, grid_x_max = min(x_min, grid_x_min), max(x_max, grid_x_max)
            
            grid_y_max = max(y_max, grid_y_max)

            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    grid[(x,y)] = "#"

    for x in range(grid_x_min, grid_x_max + 1):
        for y in range(grid_y_min, grid_y_max + 1):
            if (x,y) not in grid:
                grid[(x,y)] = "."

    return grid, grid_y_max

def tests():
    test1_exp = 24
    test2_exp = 93

    data = parse_data("puzzles\\day-14\\test_input.txt")
    test1_res = find_rest_count(deepcopy(data))
    test2_res = find_rest_count_floor(deepcopy(data))

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("puzzles\\day-14\\input.txt")
    answer1 = find_rest_count(deepcopy(data))
    answer2 = find_rest_count_floor(deepcopy(data))

    print(f"Part 1 -> Rest Count: {answer1}")
    print(f"Part 2 -> Rest Count with Floor: {answer2}")

tests()
puzzle()