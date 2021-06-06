from itertools import combinations
from math import prod

with open("input/02.txt") as f:
    data = [[int(j) for j in i.split("x")] for i in f.read().split("\n")]

paper_area = 0
ribbon_length = 0

for box in data:
    min_side = None
    min_side_area = 99999
    for comb in combinations(box, 2):
        side = prod(comb)
        paper_area += 2 * side
        if side < min_side_area:
            min_side = comb
            min_side_area = prod(comb)
            
    paper_area += min_side_area
    ribbon_length += prod(box) + 2 * sum(min_side)

print("paper area: " + str(paper_area))
print("ribbon length: " + str(ribbon_length))