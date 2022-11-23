from copy import deepcopy
import re

def pair_in_set(pair, group):
    return pair in group or (pair[1], pair[0]) in group

def strength(bridge):
    return sum([sum(i) for i in bridge])

def used_to_str(bridge):
    bridge_lists = [list(i) for i in bridge]

    for bridge_list in bridge_lists:
        bridge_list.sort()
    bridge_lists.sort()

    return "-".join([",".join([str(j) for j in i]) for i in bridge_lists])

def strongest_bridge(base, used, lookup, cache):
    used_next = deepcopy(used)
    used_next.add(base)

    used_str = used_to_str(used_next)
    if used_str in cache:
        return base[0] + base[1] + cache[used_str]

    sub_max = 0
    start = base[1]

    for end in lookup[start]:
        pair = (start, end)

        if pair_in_set(pair, used_next):
            continue

        sub_max = max(strongest_bridge(pair, used_next, lookup, cache), sub_max)

    cache[used_str] = sub_max

    return base[0] + base[1] + sub_max

with open("input\\24.txt") as f:
    data = {tuple(int(j) for j in i.split("/")) for i in f.read().split("\n")}

lookup = {}
for comp1, comp2 in data:
    if comp1 not in lookup:
        lookup[comp1] = set()
    
    if comp2 not in lookup:
        lookup[comp2] = set()

    lookup[comp1].add(comp2)
    lookup[comp2].add(comp1)

strength_max = 0
cache = {}
for other in lookup[0]:
    strength_max = max(strongest_bridge((0, other), set(), lookup, cache), strength_max)

cache_longest_len = 0
for cache_entry in cache:
    cache_longest_len = max(len(cache_entry), cache_longest_len)

long_max = 0
for cache_entry in cache:
    if len(cache_entry) != cache_longest_len:
        continue

    digits = re.findall(r"\d+", cache_entry)
    long_max = max(sum([int(i) for i in digits]), long_max)

print(f"Strongest Bridge: {strength_max}")
print(f"Strongest Long Bridge: {long_max}")