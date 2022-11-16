from itertools import combinations

class EachRotationFunc:
    def __init__(self) -> None:
        self.i = -1
        self.rots =  [lambda x, y, z: ( x, y, z),
                      lambda x, y, z: ( y,-x, z),
                      lambda x, y, z: (-x,-y, z),
                      lambda x, y, z: (-y, x, z),
                      
                      lambda x, y, z: ( z, x, y),
                      lambda x, y, z: ( z,-x,-y),
                      lambda x, y, z: ( z,-y, x),
                      lambda x, y, z: ( z, y,-x),

                      lambda x, y, z: ( x,-z, y),
                      lambda x, y, z: (-x,-z,-y),
                      lambda x, y, z: (-y,-z, x),
                      lambda x, y, z: ( y,-z,-x),

                      lambda x, y, z: (-z, y, x),
                      lambda x, y, z: (-z,-y,-x),
                      lambda x, y, z: (-z, x,-y),
                      lambda x, y, z: (-z,-x, y),
                      
                      lambda x, y, z: ( y, z, x),
                      lambda x, y, z: (-y, z,-x),
                      lambda x, y, z: ( x, z,-y),
                      lambda x, y, z: (-x, z, y),
                      
                      lambda x, y, z: ( y, x,-z),
                      lambda x, y, z: (-y,-x,-z),
                      lambda x, y, z: ( x,-y,-z),
                      lambda x, y, z: (-x, y,-z)]
        
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.rots):
            raise StopIteration
        return self.rots[self.i]

def coords_rotate(coords, rotation_func) -> set:
    return set(rotation_func(*i) for i in coords)

def coords_offset(coords, offset) -> set:
    return set(coord_offset(i, offset) for i in coords)

def coord_offset(coord, offset) -> tuple:
    return tuple(j + k for j, k in zip(coord, offset))

with open("input\\19.txt") as f:
    data = [i.split("\n") for i in f.read().split("\n\n")]

scanners = {}
for entry in data:
    scanner_id = entry[0][12:-4]
    points = set(tuple(map(int, i.split(","))) for i in entry[1:])
    scanners[scanner_id] = points

graph = {"0" : [lambda x, y, z: (x, y, z), (0, 0, 0)]}
tried = set()

while len(graph) < len(scanners):
    graph_new = dict(graph)

    for scanner_base_id in graph:
        base_rotation_func, base_offset = graph[scanner_base_id]
        base_coords = coords_offset(coords_rotate(scanners[scanner_base_id], base_rotation_func), base_offset)

        unplaced = scanners.keys() - graph_new.keys()
        for scanner_next_id in unplaced:
            if (scanner_base_id, scanner_next_id) in tried:
                continue

            for next_rotation_func in EachRotationFunc():
                next_coords = coords_rotate(scanners[scanner_next_id], next_rotation_func)
                
                for base_coord in base_coords:
                    for next_coord in next_coords:
                        to_base_offset = (base_coord[0] - next_coord[0],
                                          base_coord[1] - next_coord[1],
                                          base_coord[2] - next_coord[2])

                        next_coords_in_base = coords_offset(next_coords, to_base_offset)
                        overlap = base_coords.intersection(next_coords_in_base)
                        if len(overlap) >= 12:
                            graph_new[scanner_next_id] = [next_rotation_func, to_base_offset]
                            print(f"{len(graph_new)} placed")
                            break

                    if scanner_next_id in graph_new:
                        break
                
                if scanner_next_id in graph_new:
                    break

            if scanner_next_id in graph_new:
                break

        tried.add((scanner_base_id, scanner_next_id))

    graph = graph_new

points_in_base = set()
for scanner_id, transforms in graph.items():
    beacons_in_base = coords_offset(coords_rotate(scanners[scanner_id], transforms[0]), transforms[1])
    points_in_base = points_in_base.union(beacons_in_base)

manhattan_max = 0
for beacon1, beacon2 in combinations([i[1] for i in graph.values()], 2):
    manhattan = abs(beacon1[0] - beacon2[0]) + abs(beacon1[1] - beacon2[1]) + abs(beacon1[2] - beacon2[2])
    manhattan_max = max(manhattan, manhattan_max)

print(f"Total Beacon Count: {len(points_in_base)}")
print(f"Greatest Manhattan Distance: {manhattan_max}")