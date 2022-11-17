from itertools import cycle

def add_coords(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
adjacents = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

with open("input\\03.txt") as f:
    data = int(f.read())

grid = {(0, 0) : 1}
left, right, top, bottom = 0, 0, 0, 0
placed = 1

direction_iter = cycle(directions)
direction = next(direction_iter)

current = (0, 0)
stress_value = 0
while placed < data:
    current = (current[0] + direction[0], current[1] + direction[1])

    if not stress_value:
        value = sum([grid[add_coords(current, i)] for i in adjacents if add_coords(current, i) in grid])

        if value > data:
            stress_value = value

    grid[current] = value
    placed += 1

    if current[0] > left:
        left += 1
        direction = next(direction_iter)
    elif current[0] < right:
        right -= 1
        direction = next(direction_iter)
    elif current[1] > top:
        top += 1
        direction = next(direction_iter)
    elif current[1] < bottom:
        bottom -= 1
        direction = next(direction_iter)

print(f"Checksum: {abs(current[0]) + abs(current[1])}")
print(f"Stress Value: {stress_value}")