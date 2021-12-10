import re

def moves_min(floors_base):
    pass

with open("input/11.txt") as f:
    data = f.read().split("\n")

name_lookup = {"generator" : "RTG", "microchip" : "CHP",
                "thulium" : "Tm", "plutonium" : "Pu", "promethium" : "Pm",
                "strontium" : "Sr", "ruthenium" : "Ru"}

floors_base = []

for line in data:
    floors_base.append({(name_lookup[i[0]], name_lookup[i[1]]) for i in re.findall(r"a (\w+)[\w\-]* (\w+)", line)})
    
print(f"Minimum Moves: {moves_min(floors_base)}")

parts_new = {("El", "RTG"), ("El", "CHP"), ("Di", "RTG"), ("Di", "CHP")}
floors_base[0].update(parts_new)

print(f"Minimum Moves Extra: {moves_min(floors_base)}")