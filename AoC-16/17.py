from hashlib import md5

def find_paths(vault_code):
    open_chars = {"b", "c", "d", "e", "f"}
    directions = [("U", (0, -1)), ("D", (0, 1)), ("L", (-1, 0)), ("R", (1, 0))]

    start = (0, 0)
    end = (3, 3)

    shortest_path = ""
    longest_length = 0

    frontier = [("", start)]
    path_cache = set()
    while frontier:
        frontier_new = []

        for path in frontier:
            if path in path_cache:
                continue
            path_cache.add(path)

            hash_code = md5((vault_code + path[0]).encode()).hexdigest()

            for i, direction in enumerate(directions):
                if hash_code[i] in open_chars:
                    path_new = path[0] + direction[0]
                    coords = (direction[1][0] + path[1][0], direction[1][1] + path[1][1])

                    if coords == end:
                        successful_path = path_new
                        if not shortest_path:
                            shortest_path = successful_path
                        if len(successful_path) > longest_length:
                            longest_length = len(successful_path)
                    elif coords[0] < 0 or coords[1] < 0 or coords[0] > 3 or coords[1] > 3:
                        continue
                    else:
                        frontier_new.append((path_new, coords))

        frontier = frontier_new

    return shortest_path, longest_length

with open("input\\17.txt") as f:
    vault_code = f.read()

shortest, longest = find_paths(vault_code)

print(f"Shortest Path: {shortest}")
print(f"Longest Path Length: {longest}")