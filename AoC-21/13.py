import re

with open("input\\13.txt") as f:
    data = f.read().split("\n\n")

def print_grid(grid, x_size, y_size):
    grid_strs = [["."] * (x_size) for _ in range(y_size)]
    for cell in grid:
        grid_strs[cell[1]][cell[0]] = "#"
    for grid_str in grid_strs:
        print("".join(grid_str))

dots = set()
for line in data[0].split("\n"):
    coords = line.split(",")
    dots.add((int(coords[0]), int(coords[1])))

folds = [i.split("=") for i in re.findall(r"[xy]=\d+", data[1])]

x_size = max([i[0] for i in dots]) + 1
y_size = max([i[1] for i in dots]) + 1

fold_1_count = 0

for fold in folds:
    dots_new = set()
    dots_flip = set()
    fold_point = int(fold[1])

    if fold[0] == "x":
        for dot in dots:
            if dot[0] < fold_point:
                dots_new.add(dot)
            else:
                dots_flip.add((2 * fold_point - dot[0], dot[1]))
        x_size = fold_point
    else:
        for dot in dots:
            if dot[1] < fold_point:
                dots_new.add(dot)
            else:
                dots_flip.add((dot[0], 2 * fold_point - dot[1]))
        y_size = fold_point

    dots = dots_new.union(dots_flip)
    if not fold_1_count:
        fold_1_count = len(dots)

print(f"Dots after 1 fold: {fold_1_count}")
print(f"Code:")
print_grid(dots, x_size, y_size)