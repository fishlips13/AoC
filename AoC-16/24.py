from itertools import permutations, pairwise

adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                
with open("input\\24.txt") as f:
    data = f.read().split("\n")

grid = {}
locations = {}

for y, line in enumerate(data):
    for x, cell in enumerate(line):
        if cell != " " and cell != "#":
            grid[(x,y)] = cell
            if cell != ".":
                locations[cell] = [(x,y), {}]

for location_id, details in locations.items():
    coords, targets = details

    frontier = [coords]
    visited = set([coords])

    distance = 1
    while frontier:
        frontier_next = []

        for cell in frontier:
            for adj in adjacents:
                neigh = (cell[0] + adj[0], cell[1] + adj[1])

                if neigh not in grid or neigh in visited:
                    continue

                cell_content = grid[neigh]
                if cell_content in locations:
                    targets[cell_content] = distance

                frontier_next.append(neigh)
                visited.add(neigh)

        distance += 1
        frontier = frontier_next

locations_other = list(locations.keys())
locations_other.remove("0")

dist_term_min  = 9999999999999
dist_cycle_min = 9999999999999

for route in permutations(locations_other):
    route_term =  ["0"] + list(route)
    route_cycle = ["0"] + list(route) + ["0"]

    dist_term =  sum([locations[orig][1][dest] for orig, dest in pairwise(route_term)])
    dist_cycle = sum([locations[orig][1][dest] for orig, dest in pairwise(route_cycle)])

    dist_term_min  = min(dist_term, dist_term_min)
    dist_cycle_min = min(dist_cycle, dist_cycle_min)

print(f"Shortest Distance: {dist_term_min}")
print(f"Shortest Distance Returning: {dist_cycle_min}")