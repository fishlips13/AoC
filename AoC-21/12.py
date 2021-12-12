with open("input\\12.txt") as f:
    data = [i.split("-") for i in f.read().split("\n")]

def path_count(caves, visit_small_twice):
    frontier_paths = [("start", "start", False)]
    full_paths = []
    path_cache = set()

    while frontier_paths:
        frontier_new_paths = []

        for frontier_path in frontier_paths:
            for cave_path in caves[frontier_path[1]]:
                new_path = frontier_path[0] + cave_path
                if new_path in path_cache:
                    continue
                path_cache.add(new_path)

                if cave_path == "end":
                    full_paths.append(new_path)
                    continue
                elif cave_path == "start":
                    continue

                if cave_path.islower() and cave_path in frontier_path[0]:
                    if visit_small_twice and not frontier_path[2]:
                        frontier_new_paths.append((new_path, cave_path, True))
                else:
                    frontier_new_paths.append((new_path, cave_path, frontier_path[2]))

        frontier_paths = frontier_new_paths
    
    return len(full_paths)

caves = {}
for line in data:
    if line[0] not in caves:
        caves[line[0]] = []

    if line[1] not in caves:
        caves[line[1]] = []

    caves[line[0]].append(line[1])
    caves[line[1]].append(line[0])

print(f"Total Valid Paths: {path_count(caves, False)}")
print(f"Total Valid Paths: {path_count(caves, True)}")