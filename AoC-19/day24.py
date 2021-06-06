def in_map(cell, grid):
    if cell[0] < 0 or cell[0] > 4 or cell[1] < 0 or cell[1] > 4 or (cell[0] == 2 and cell[1] == 2):
        return False
    return True

def bug_count(grid):
    count = 0
    for line in grid:
        for cell in line:
            if cell == "#":
                count += 1
    return count

def get_row(x, grid):
    return grid[x]

def get_col(y, grid):
    col = []
    for row in grid:
        col.append(row[y])
    return col

def get_adjacent(x, y, grid_main, grid_below, grid_above):

    if x == 2 and y == 2:
        raise Exception("2 and 2 = NOPE")

    a_candis = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

    a_cells = []
    for a_candi in a_candis:
        # Main
        if in_map((a_candi[0], a_candi[1]), grid_main):
            a_cells.append(grid_main[a_candi[1]][a_candi[0]])
            continue
        
        # Above
        if grid_above:
            if a_candi[0] == -1:
                a_cells.append(grid_above[2][1])
            elif a_candi[0] == 5:
                a_cells.append(grid_above[2][3])
            elif a_candi[1] == -1:
                a_cells.append(grid_above[1][2])
            elif a_candi[1] == 5:
                a_cells.append(grid_above[3][2])

        # Below
        if grid_below and a_candi[0] == 2 and a_candi[1] == 2:
            if x == 1:
                a_cells.extend(get_col(0, grid_below))
            elif x == 3:
                a_cells.extend(get_col(4, grid_below))
            elif y == 1:
                a_cells.extend(get_row(0, grid_below))
            elif y == 3:
                a_cells.extend(get_row(4, grid_below))

    return a_cells

# def bio_div(bio_grid):
#     total = 0
#     pow_of_2 = 1
#     for line in bio_grid:
#         for cell in line:
#             total += pow_of_2 if cell == "#" else 0
#             pow_of_2 *= 2
#     return total

grids = [([["."] * 5 for i in range(5)], 0) for j in range(201)]

for grid in grids:
    grid[0][2][2] = "?"

f = open("data.txt")
grid_input = [[j for j in i] for i in f.read().split()]
grids[100] = (grid_input, bug_count(grid_input))
f.close()

for _ in range(200):
    new_grids = []

    for grid_id in range(len(grids)):
        grid_main = grids[grid_id]
        grid_below = grids[grid_id + 1] if grid_id + 1 <= 200 else None
        grid_above = grids[grid_id - 1] if grid_id - 1 >= 0 else None

        if grid_main[1] == 0 and (grid_below and grid_below[1] == 0) and (grid_above and grid_above[1] == 0):
            new_grids.append(grid_main)
            continue
        else:
            new_grid = []

        for y in range(5):
            new_grid_row = []
            
            for x in range(5):
                if x ==2 and y == 2:
                    new_grid_row.append("?")
                    continue

                bugs_adjacent = 0
                adjacent_cells = get_adjacent(x, y, grid_main[0], \
                                                    grids[grid_id + 1][0] if grid_id + 1 <= 200 else None, \
                                                    grids[grid_id - 1][0] if grid_id - 1 >= 0 else None)

                for adjacent_cell in adjacent_cells:
                    bugs_adjacent += 1 if adjacent_cell == "#" else 0
                
                if grid_main[0][y][x] == "#":
                    if bugs_adjacent == 1:
                        new_grid_row.append("#")
                    else:
                        new_grid_row.append(".")
                elif grid_main[0][y][x] == ".":
                    if bugs_adjacent == 1 or bugs_adjacent == 2:
                        new_grid_row.append("#")
                    else:
                        new_grid_row.append(".")
            
            new_grid.append(new_grid_row)

        new_grids.append((new_grid, bug_count(new_grid)))

    grids = new_grids

total = 0
for grid in grids:
    total += grid[1]

print(total)