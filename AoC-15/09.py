from itertools import permutations

class Location:

    new_location_id = 0

    def __init__(self, name):
        self.name = name
        self.id = str(Location.new_location_id)
        self.neighbours = {}

        Location.new_location_id += 1

with open("input/09.txt") as f:
    data = [[j for j in i.split(" ") if j != "to" and j != "="] for i in f.read().split("\n")]

locations = {}

for line in data:
    if line[0] not in locations:
        locations[line[0]] = Location(line[0])
    if line[1] not in locations:
        locations[line[1]] = Location(line[1])

for line in data:
    locations[line[0]].neighbours[line[1]] = int(line[2])
    locations[line[1]].neighbours[line[0]] = int(line[2])

def path_length(comparer, comparer_start):
    
    extreme = comparer_start

    for path in permutations(locations.values(), len(locations)):

        distance = 0

        origin_iter = iter(path)
        dest_iter = iter(path)
        next(dest_iter)

        for origin, destination in zip(origin_iter, dest_iter):
            distance += origin.neighbours[destination.name]
        
        extreme = comparer(extreme, distance)
    
    return extreme

print(f"Minimum Distance: {path_length(min, 999999)}")
print(f"Maximum Distance: {path_length(max, 0)}")