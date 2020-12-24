def neighs_active_count(coord, cubes, offsets):
    active_count = 0

    for offset in offsets:
        neigh_coord = tuple(i + j for i, j in zip(coord, offset))
        if neigh_coord in cubes and cubes[neigh_coord]:
            active_count += 1

    return active_count

def cubes_next(cubes, offsets):
    padding_cubes = set()
    for coord, active in cubes.items():
        if not active:
            continue

        for offset in offsets:
            neigh_coord = tuple(i + j for i, j in zip(coord, offset))
            if neigh_coord not in cubes:
                padding_cubes.add(neigh_coord)

    for coord in padding_cubes:
        cubes[coord] = False

    new_cubes = {}
    for coord, active in cubes.items():
        active_count = neighs_active_count(coord, cubes, offsets)
        if active_count == 3 or active_count == 2 and active:
            new_cubes[coord] = True
        elif active_count > 0:
            new_cubes[coord] = False
            
    return new_cubes

def count_cubes_active(cubes):
    count = 0

    for active in cubes.values():
        if active:
            count += 1

    return count

with open("input/17.txt") as f:
    data = f.read().split("\n")

offsets_3d = set()
for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            if x or y or z:
                offsets_3d.add((x,y,z))

offsets_4d = set()
for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            for w in [-1, 0, 1]:
                if x or y or z or w:
                    offsets_4d.add((x,y,z,w))

cubes_3d = {}
cubes_4d = {}
reps = 6

for y in range(len(data)):
    for x in range(len(data[0])):
        cubes_3d[(x, y, 0)] = data[y][x] == "#"
        cubes_4d[(x, y, 0, 0)] = data[y][x] == "#"

for _ in range(reps):
    cubes_3d = cubes_next(cubes_3d, offsets_3d)
    cubes_4d = cubes_next(cubes_4d, offsets_4d)

print(f"Cubes Active after Init: {count_cubes_active(cubes_3d)}")
print(f"Hypercubes Active after Init: {count_cubes_active(cubes_4d)}")
