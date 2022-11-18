directions = {"n" : (0,1), "s" : (0,-1), "nw" : (-1,1), "ne" : (1,0), "sw" : (-1,0), "se" : (1,-1)}

with open("input\\11.txt") as f:
    data = f.read().split(",")

coords = (0, 0)
manhattan_max = 0

for step in data:
    move = directions[step]
    coords = (coords[0] + move[0], coords[1] + move[1])

    if coords[0] >= 0 and coords[1] >= 0 or coords[0] <= 0 and coords[1] <= 0:
        manhattan = abs(coords[0] + coords[1])
    else:
        manhattan = max(abs(coords[0]), abs(coords[1]))
    
    manhattan_max = max(manhattan, manhattan_max)

print(f"Distance Final: {manhattan}")
print(f"Distance Max: {manhattan_max}")