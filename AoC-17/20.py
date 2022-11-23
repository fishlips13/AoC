import re
from copy import deepcopy
from itertools import permutations
from math import copysign

def add_triples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])

with open("input\\20.txt") as f:
    data = f.read().split("\n")

parts = {}
name_min = None
total_mins = (999999999999, 999999999999, 999999999999)

for i, line in enumerate(data):
    values = [int(i) for i in re.findall(r"[-\d]+", line)]
    p = (values[0], values[1], values[2])
    v = (values[3], values[4], values[5])
    a = (values[6], values[7], values[8])
    parts[i] = ([p, v, a])

    p_total = sum([abs(i) for i in p])
    v_total = sum([abs(i) for i in v])
    a_total = sum([abs(i) for i in a])

    if a_total > total_mins[2] or \
        a_total == total_mins[2] and v_total > total_mins[1] or \
        a_total == total_mins[2] and v_total == total_mins[1] and p_total > total_mins[0]:
        continue

    total_mins = (p_total, v_total, a_total)
    name_min = i

for _ in range (100):
    for part in parts.values():
        part[1] = add_triples(part[1], part[2])
        part[0] = add_triples(part[0], part[1])

    part_colls = set()
    for p1, p2 in permutations(parts.keys(), 2):

        p1_pos, p2_pos = parts[p1][0], parts[p2][0]
        if p1_pos[0] == p2_pos[0] and p1_pos[1] == p2_pos[1] and p1_pos[2] == p2_pos[2]:
            part_colls.add(p1)
            part_colls.add(p2)
            continue

    for part in part_colls:
        del parts[part]

print(f"Closest Long Term: {name_min}")
print(f"Particles Left: {len(parts)}")


# ----------------------
# Attempts to determine if a particle will ever collide again. Fruitless
# ----------------------


# ignores = {i : set() for i in parts.keys()}
# free = []

        # for i in range(3):
        #     p1_p_axis, p1_v_axis, p1_a_axis = parts[p1][0][i], parts[p1][1][i], parts[p1][2][i]
        #     p2_p_axis, p2_v_axis, p2_a_axis = parts[p2][0][i], parts[p2][1][i], parts[p2][2][i]

        #     p1_p_rel = copysign(1, p2_p_axis - p1_p_axis)
        #     p1_v_rel = copysign(1, p2_v_axis - p1_v_axis)
        #     p1_a_rel = copysign(1, p2_a_axis - p1_a_axis)

        #     if (p1_v_rel == 0 and p1_a_rel == 0) or \
        #         p1_p_rel != p1_v_rel and p1_p_rel != p1_a_rel:
        #         ignores[p1].add(p2)
        #         ignores[p2].add(p1)

        # del ignores[part]
        # for part_ignores in ignores.values():
        #     if part in part_ignores:
        #         part_ignores.remove(part)

    # for part, part_ignores in ignores.items():
    #     if len(part_ignores) == len(parts) - 1:
    #         free.append(part)
    #         del parts[part]
    #         print(str(len(parts))+ " " + str(len(free)))
    #         for part_ignores in ignores.values():
    #             if part in part_ignores:
    #                 part_ignores.remove(part)
