with open("input/12.txt") as f:
    cmds = [(i[0], int(i[1:])) for i in f.read().split("\n")]

bad_ship_x, bad_ship_y = 0, 0
facing = 0
# 0 East  90 North  180 West  270 South

for op, value in cmds:
    if op == "E" or op == "F" and facing == 0:
        bad_ship_x += value
    elif op == "N" or op == "F" and facing == 90:
        bad_ship_y += value
    elif op == "W" or op == "F" and facing == 180:
        bad_ship_x -= value
    elif op == "S" or op == "F" and facing == 270:
        bad_ship_y -= value
    elif op == "L":
        facing = (facing + value) % 360
    elif op == "R":
        facing = (facing - value) % 360

print(f"Bad Manhattan Distance: {abs(bad_ship_x) + abs(bad_ship_y)}")

ship_x, ship_y = 0, 0
way_x, way_y = 10, 1

for op, value in cmds:
    if op == "E":
        way_x += value
    elif op == "N":
        way_y += value
    elif op == "W":
        way_x -= value
    elif op == "S":
        way_y -= value
        
    elif op == "L" or  op == "R":
        if op == "R":
            value = 360 - value

        if value == 90:
            way_x, way_y = way_y * -1, way_x
        elif value == 180:
            way_x, way_y = way_x * -1, way_y * -1
        elif value == 270:
            way_x, way_y = way_y, way_x * -1

    elif op == "F":
        ship_x += way_x * value
        ship_y += way_y * value

print(f"Good Manhattan Distance: {abs(ship_x) + abs(ship_y)}")