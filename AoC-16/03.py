import re

with open("input/03.txt") as f:
    data = f.read().split("\n")

def count_valid(triangles):
    count = 0

    for edges in triangles:
        edges.sort()
        if edges[0] + edges[1] > edges[2]:
            count += 1
    return count

edge_lengths_bad = []
edge_lengths_good = []
edge_lengths_good_parts = [[], [], []]

for line in data:
    edges = [int(i) for i in re.findall(r"\d+", line)]

    edge_lengths_bad.append(edges)

    edge_lengths_good_parts[0].append(edges[0])
    edge_lengths_good_parts[1].append(edges[1])
    edge_lengths_good_parts[2].append(edges[2])

    if len(edge_lengths_good_parts[0]) == 3:
        edge_lengths_good.extend(edge_lengths_good_parts)
        edge_lengths_good_parts = [[], [], []]

print(f"Valid Triangles (bad relation): {count_valid(edge_lengths_bad)}")
print(f"Valid Triangles: {count_valid(edge_lengths_good)}")