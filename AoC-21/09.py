from collections import deque
from math import prod

with open("input\\09.txt") as f:
    data = [[int(k) for k in i] for i in f.read().split("\n")]

cells = {}
cells_low = deque()
offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for x, line in enumerate(data):
    for y, height in enumerate(line):
        cells[(x,y)] = height

for coord, height in cells.items():
    
    is_low = True
    for offset in offsets:
        neighbour = (coord[0] + offset[0], coord[1] + offset[1])
        if neighbour in cells and cells[neighbour] <= height:
            is_low = False
            break
    
    if is_low:
        cells_low.append(coord)

risk_level_sum = sum([1 + cells[i] for i in cells_low])

basin_sizes = []

while cells_low:
    frontier = deque([cells_low.pop()])
    visited = set()

    basin_size = 0
    while frontier:
        coord = frontier.pop()
        visited.add(coord)

        if cells[coord] == 9:
            continue

        basin_size += 1

        for offset in offsets:
            neighbour = (coord[0] + offset[0], coord[1] + offset[1])
            if neighbour in cells and neighbour not in frontier and neighbour not in visited:
                frontier.append(neighbour)

    basin_sizes.append(basin_size)

basin_sizes.sort()

largest_basin_mult_3 = prod(basin_sizes[-3:])

print(f"Risk level Sum: {risk_level_sum}")
print(f"3 Largest Basin Mutliple: {largest_basin_mult_3}")