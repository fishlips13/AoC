import re
from itertools import combinations, chain
from copy import deepcopy
from queue import PriorityQueue

def moves_min(floors_base):
    floors_states_frontier = PriorityQueue()
    state_cache = set()
    count_min = 9999999999
    heuristic_min = 9999999999

    floors_states_frontier.put((0, (floors_base, 0, 0)))

    while floors_states_frontier:
        floors_state = floors_states_frontier.get()
        heuristic_current = floors_state[0]

        if heuristic_current >= heuristic_min:
            y = 9
            return count_min

        floors = floors_state[1][0]
        i_floor_curr = floors_state[1][1]
        move_count = floors_state[1][2]

        state = build_state(floors) + str(i_floor_curr)
        if state in state_cache:
            continue
        state_cache.add(state)

        floor_curr = floors[i_floor_curr]
        for comb in chain(combinations(floor_curr, 1), combinations(floor_curr, 2)):
            floors_curr = deepcopy(floors)
            moving = set(comb)
            floors_curr[i_floor_curr] -= moving

            for i in [j for j in [i_floor_curr - 1, i_floor_curr + 1] if j >= 0 and j <= 3]:
                if i_floor_curr == 1 and i == 0 and len(floors[0]) == 0 or \
                    i_floor_curr == 2 and i == 1 and len(floors[0]) == 0 and len(floors[1]) == 0:
                    continue
            
                floors_new = deepcopy(floors_curr)
                floors_new[i].update(moving)
                
                if is_valid(floors_new):
                    if len(floors[0]) + len(floors[1]) + len(floors[2]) == 0:
                        count_min = min(count_min, move_count)
                        heuristic_min = min(heuristic_min, heuristic_current)
                    floors_states_frontier.put((heuristic(floors), (floors_new, i, move_count + 1)))

def heuristic(floors):
    total = 0
    for i, floor in enumerate(floors):
        total += len(floor) * (-i)
    return total

def build_state(floors):
    state = ""
    for floor in floors:

        part_types = {}
        for item in floor:
            if item[0] not in part_types:
                part_types[item[0]] = []
            part_types[item[0]].append(item)
        
        floor_list = []
        for parts in part_types.values():
            if len(parts) == 2:
                floor_list.append("RTGCHP")
            else:
                floor_list.extend([i[0] + "-" + i[1] for i in parts])
        
        floor_list.sort()
        state += ",".join(floor_list) + ";"
    return state

def is_valid(floors):
    for floor in floors:

        rtgs, chips = set(), set()
        for item in floor:
            if item[1] == "RTG":
                rtgs.add(item[0])
            elif  item[1] == "CHP":
                chips.add(item[0])

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
    floors_base.append({(name_lookup[i[0]], name_lookup[i[1]]) for i in re.findall(r"a (\w+)[\w\-]* (\w+)", line)})

print(f"Minimum Moves: {moves_min(floors_base)}")

parts_new = {("El", "RTG"), ("El", "CHP"), ("Di", "RTG"), ("Di", "CHP")}
floors_base[0].update(parts_new)

print(f"Minimum Moves Extra: {moves_min(floors_base)}")