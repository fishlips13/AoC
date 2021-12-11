import re
from itertools import combinations, chain
from copy import deepcopy

def moves_min(floors_base):
    frontier_states = [(floors_base, 0)]
    next_states = []
    state_cache = {build_state(floors_base) + "0"}
    move_count = 0

    while True:
        for frontier_state in frontier_states:
            floors = frontier_state[0]
            i_curr = frontier_state[1]

            floor_curr = floors[i_curr]
            for comb in chain(combinations(floor_curr, 1), combinations(floor_curr, 2)):
                floors_curr = deepcopy(floors)
                moving = set(comb)
                floors_curr[i_curr] -= moving

                for i in [j for j in [i_curr - 1, i_curr + 1] if j >= 0 and j <= 3]:
                    floors_new = deepcopy(floors_curr)
                    floors_new[i].update(moving)

                    if not floors_valid(floors_new):
                        continue

                    if len(floors[0]) + len(floors[1]) + len(floors[2]) == 0:
                        return move_count

                    state_new = build_state(floors_new) + str(i)
                    if state_new in state_cache:
                        continue
                    state_cache.add(state_new)

                    next_states.append((floors_new, i))

        frontier_states = next_states
        next_states = []
        move_count += 1
                        
def build_state(floors):
    state = ""
    part_types = {}
    id_ord = ord("a")

    for floor in floors:
        floor_list = list(floor)
        floor_list.sort()

        found = set()
        for item in floor_list:
            if item[1] not in part_types:
                part_types[item[1]] = id_ord
                id_ord += 1
                found.add(item[1])
            elif item[1] in found:
                part_types[item[1]] = ord("#")

    for floor in floors:
        floors_list = [chr(part_types[item[1]]) if item[0] == "CHP" or part_types[item[1]] == ord("#") else chr(part_types[item[1]] - 32) for item in floor]
        floors_list.sort()
        state += "".join(floors_list) + ";"
        
    return state

def floors_valid(floors):
    for floor in floors:

        rtgs, chips = set(), set()
        for item in floor:
            if item[0] == "RTG":
                rtgs.add(item[1])
            elif  item[0] == "CHP":
                chips.add(item[1])

        chips -= rtgs

        if rtgs and chips:
            return False

    return True

with open("input/11.txt") as f:
    data = f.read().split("\n")

name_lookup = {"generator" : "RTG", "microchip" : "CHP",
                "thulium" : "Tm", "plutonium" : "Pu", "promethium" : "Pm",
                "strontium" : "Sr", "ruthenium" : "Ru"}

floors_base = []

for line in data:
    floors_base.append({(name_lookup[i[1]], name_lookup[i[0]]) for i in re.findall(r"a (\w+)[\w\-]* (\w+)", line)})
    
print(f"Minimum Moves: {moves_min(floors_base)}")

parts_new = {("RTG", "El"), ("CHP", "El"), ("RTG", "Di"), ("CHP", "Di")}
floors_base[0].update(parts_new)

print(f"Minimum Moves Extra: {moves_min(floors_base)}")