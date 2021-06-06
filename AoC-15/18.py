from copy import deepcopy

def neighs_on_count(x, y, grid):

    offsets = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    on_count = 0

    for offset in offsets:
        neigh_x = x + offset[0]
        neigh_y = y + offset[1]

        if neigh_x >= 0 and neigh_y >= 0 and neigh_x < len(grid[0]) and neigh_y < len(grid) and grid[neigh_y][neigh_x] == "#":
            on_count += 1

    return on_count

def grid_next(grid):

    new_grid = []
    for y in range(len(grid)):

        new_line = []
        new_grid.append(new_line)
        for x in range(len(grid[0])):

            on_count = neighs_on_count(x, y, grid)
            if grid[y][x] == "#" and on_count == 2 or on_count == 3:
                new_line.append("#")
            else:
                new_line.append(".")

    return new_grid

def count_lights_on(grid):
    on_count = 0

    for line in grid:
        for light in line:
            if light == "#":
                on_count += 1

    return on_count

def fix_corners_on(grid):
    corner_coords = [(0, 0), (0, len(grid)-1), (len(grid[0])-1, 0), (len(grid[0])-1, len(grid)-1)]
    for coord in corner_coords:
        grid[coord[1]][coord[0]] = "#"
    
    return grid

with open("input/18.txt") as f:
    grid = [[j for j in i] for i in f.read().split("\n")]


reps = 100

grid_1 = deepcopy(grid)
for _ in range(reps):
    grid_1 = grid_next(grid_1)

print(f"Lit Count: {count_lights_on(grid_1)}")
    
grid_2 = deepcopy(grid)
grid_2 = fix_corners_on(grid_2)
for _ in range(reps):
    grid_2 = grid_next(grid_2)
    grid_2 = fix_corners_on(grid_2)

print(f"Lit Count (fixed corners): {count_lights_on(grid_2)}")
