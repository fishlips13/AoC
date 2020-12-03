from math import prod

def slope_trees(shift):

    x, y = 0, 0
    trees = 0

    while y < len(data):
        if data[y][x] == "#":
            trees += 1
        
        x = (x + shift[0]) % len(data[0])
        y += shift[1]
    
    return trees

with open("input/03.txt") as f:
    data = f.read().split("\n")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(f"Trees {slopes[1]}: {slope_trees(slopes[1])}")
print(f"Trees All: {prod(slope_trees(i) for i in slopes)}")