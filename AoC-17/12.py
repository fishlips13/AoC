import re

with open("input\\12.txt") as f:
    data = f.read().split("\n")

vills = {}

for line in data:
    vill = re.findall(r"\d+", line)
    vills[vill[0]] = vill[1:]

vills_all = set(vills.keys())
zero_count = 0
groups_total = 0

while vills_all:
    frontier = [vills_all.pop()]
    visited = set()

    while frontier:
        vill = frontier.pop()
        visited.add(vill)

        for pipe in vills[vill]:
            if pipe not in visited:
                frontier.append(pipe)

    if "0" in visited:
        zero_count = len(visited)
    
    vills_all.difference_update(visited)
    groups_total += 1

print(f"Connected to '0': {zero_count}")
print(f"Groups Total: {groups_total}")