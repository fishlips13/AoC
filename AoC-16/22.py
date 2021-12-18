
import re
from queue import PriorityQueue
from copy import deepcopy

def compress_state(grid):
    return "-".join(["".join(i) for i in grid])

def decompress_state(state):
    grid = []
    goal, empty = None, None

    rows = state.split("-")
    for y, row in enumerate(rows):
        grid.append([])
        for x, cell in enumerate(row):
            grid[y].append(cell)
            if cell == "G":
                goal = (x, y)
            elif cell == "_":
                empty = (x, y)

    return grid, goal, empty

def heuristic(curr, end):
    return abs(end[0] - curr[1]) + abs(end[0] - curr[1])

def fewest_steps(grid):
    frontier = PriorityQueue()
    frontier.put((0, 0, 0, compress_state(grid)))
    state_cache = set()
    adjacents = {(0, 1), (1, 0), (0, -1), (-1, 0)}

    while not frontier.empty():
        move_count, _, _, state = frontier.get()
        
        grid, goal, empty = decompress_state(state)
        move_count += 1
        
        for adj in adjacents:
            nx, ny = empty[0] + adj[0], empty[1] + adj[1]
            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid) or grid[ny][nx] == "#":
                continue

            if (nx, ny) == goal and empty == (0, 0):
                return move_count

            grid_new = deepcopy(grid)
            grid_new[empty[1]][empty[0]] = grid_new[ny][nx]
            grid_new[ny][nx] = "_"

            state = compress_state(grid_new)
            if state in state_cache:
                continue
            state_cache.add(state)

            if grid_new[empty[1]][empty[0]] == "G":
                goal_new = empty
            else:
                goal_new = goal

            frontier.put((move_count, heuristic(goal_new, (0, 0)), heuristic(goal_new, empty), state))

with open("input\\22.txt") as f:
    data = [[j for j in map(int, re.findall(r"\d+", i))] for i in f.read().split("\n")[2:]]

x_max = max([i[0] for i in data])
y_max = max([i[1] for i in data])
grid = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

valid_total = 0
for line in data:
    if line[3] == 0:
        value = "_"
    elif line[3] > 100:
        value = "#"
    elif line[0] == x_max and line[1] == 0:
        value = "G"
        valid_total += 1
    else:
        value = "."
        valid_total += 1
    grid[line[1]][line[0]] = value

print(f"Valid Pairs: {valid_total}")
print(f"Fewest Steps: {fewest_steps(grid)}")


# Slow AF, ~ 10 mins
# Hand solvable, lul