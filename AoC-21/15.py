from queue import PriorityQueue

def not_even_ayyy_star(grid):
    cave_map = {(x, y) : risk for y, line in enumerate(grid) for x, risk in enumerate(line)}
    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid) - 1)
    adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    lowest = 99999999999999

    frontier = PriorityQueue()
    frontier.put((0, start))
    visited = {start : 0}
    while not frontier.empty():
        _, curr = frontier.get()

        for adjacent in adjacents:
            next_ = (curr[0] + adjacent[0], curr[1] + adjacent[1])

            if next_[0] < 0 or next_[0] > end[0] or next_[1] < 0 or next_[1] > end[1]:
                continue

            risk = visited[curr] + cave_map[next_]

            if next_ in visited and risk >= visited[next_]:
                continue

            if next_ == end:
                lowest = min(lowest, risk)
            else:
                frontier.put((risk, next_))

            visited[next_] = risk
    
    return lowest

def slide(original):
    return [i for i in map(lambda x: x + 1 if x < 9 else 1, original)]

with open("input\\15.txt") as f:
    grid = [[int(j) for j in i] for i in f.read().split("\n")]

grid_5 = [[] for _ in range(len(grid) * 5)]

for grid_row, grid_5_row in zip(grid, grid_5):
    new_row = grid_row
    for _ in range(5):
        grid_5_row.extend(new_row)
        new_row = slide(new_row)

for grid_5_row, grid_5_row_10 in zip(grid_5, grid_5[len(grid):]):
    grid_5_row_10.extend(slide(grid_5_row))

print(f"Lowest Risk Path (1): {not_even_ayyy_star(grid)}")
print(f"Lowest Risk Path (5): {not_even_ayyy_star(grid_5)}")