with open("input/01.txt") as f:
    moves = [(i[0], int(i[1:])) for i in f.read().split(", ")]

coords = (0, 0)
facing = (0, 1)
visited = {(0, 0)}
hq_coords = None

for move in moves:
    if move[0] == "L":
        facing = (-facing[1], facing[0])
    else:
        facing = (facing[1], -facing[0])

    for _ in range(move[1]):
        coords = (coords[0] + facing[0], coords[1] + facing[1])

        if not hq_coords:
            if coords in visited:
                hq_coords = coords
            else:
                visited.add(coords)

print(f"Instructions Distance: {abs(coords[0]) + abs(coords[1])}")
print(f"HQ Distance: {abs(hq_coords[0]) + abs(hq_coords[1])}")