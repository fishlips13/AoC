from collections import deque

def print_grid(grid):
    x_max = max(i[0] for i in grid)
    y_max = max(i[1] for i in grid)

    grid_print = [["_"] * (x_max + 1) for _ in range(y_max + 1)]
    
    for coord, value in grid.items():
        grid_print[coord[1]][coord[0]] = value

    for line in grid_print:
        print("".join(line))
    print("")

with open("input\\25.txt") as f:
    data = f.read().split("\n")

adjacent = {">" : (1, 0), "v" : (0, 1)}

grid = {}
for y, line in enumerate(data):
    for x, cell in enumerate(line):
        grid[(x,y)] = cell

move_count = 0
while True:

    moved = False
    for cell_type in [">", "v"]:
        cell_moves = []

        for coords, value in grid.items():
            if value != cell_type:
                continue

            adj_x, adj_y = adjacent[grid[coords]]
            coords_adj = (coords[0] + adj_x, coords[1] + adj_y)

            coords_adj = (coords_adj[0] % len(data[0]), coords_adj[1] % len(data))

            if grid[coords_adj] != ".":
                continue

            cell_moves.append((coords, coords_adj))

        moved = moved or len(cell_moves) > 0

        for coords, coords_adj in cell_moves:
            grid[coords_adj] = grid[coords]
            grid[coords] = "."

    move_count += 1
    if not moved:
        break

print(f"First Static Step: {move_count}")