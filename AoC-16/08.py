import re

def fill(x, y, grid):
    for j in range(y):
        for i in range(x):
            grid[j][i] = "#"

    return grid

def rotate_row(i_row, count, grid):
    count = count % len(grid[0])
    grid[i_row] = grid[i_row][-count:] + grid[i_row][:-count]
    return grid

def rotate_column(i_col, count, grid):
    count = count % len(grid)
    column = [row[i_col] for row in grid]
    column = column[-count:] + column[:-count]
    for row, value in zip(grid, column):
        row[i_col] = value
    return grid

with open("input/08.txt") as f:
    data = f.read().split("\n")

screen_x, screen_y = 50, 6
grid = [[" "] * screen_x for _ in range(screen_y)]

for line in data:
    values = [int(i) for i in re.findall("\d+", line)]
    if "rect" in line:
        grid = fill(values[0], values[1], grid)
    elif "row" in line:
        grid = rotate_row(values[0], values[1], grid)
    elif "column" in line:
        grid = rotate_column(values[0], values[1], grid)

pixels_lit = sum(i == "#" for row in grid for i in row)

print(f"Pixels Lit: {pixels_lit}")
print("Code:")

for row in grid:
    print("".join(row))