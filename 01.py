from itertools import combinations
from math import prod

data = []
with open("input/01.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

def willItBlend2020(data, count):
    for comb in combinations(data, count):
        if sum(comb) == 2020:
            return "{} = {} -> {}".format(" + ".join(map(str, comb)), str(sum(comb)), str(prod(comb)))
    return "Nope"

print("Part 1: " + willItBlend2020(data, 2))
print("Part 2: " + willItBlend2020(data, 3))