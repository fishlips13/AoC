import re

def tower_weight(name, tower):
    data = tower[name]

    weights = []
    for sub_name in data[1]:
        weights.append((sub_name, tower_weight(sub_name, tower)))

    if not all([i[1] == weights[0][1] for i in weights]):
        print(f"Discrepency: {weights}")

    return data[0] + sum([i[1] for i in weights])

with open("input\\07.txt") as f:
    data = f.read().split("\n")

tower = {}
sub_towers = set()

for line in data:
    hits = re.findall(r"\w+", line)
    tower[hits[0]] = [int(hits[1]), hits[2:]]
    sub_towers.update(hits[2:])

base_tower = (tower.keys() - sub_towers).pop()

print(f"Base Tower Name: {base_tower}")
tower_weight(base_tower, tower)