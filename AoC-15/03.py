def next_coord(current, op):
    if op == "^": # up
        return (current[0], current[1] + 1)
    elif op == "v": # down
        return (current[0], current[1] - 1)
    elif op == "<": # left
        return (current[0] - 1, current[1])
    else: # right
        return (current[0] + 1, current[1])

with open("input/03.txt") as f:
    data = f.read()

houses = set()
houses.add((0,0))
santa = (0,0)
robo_santa = (0,0)
santas_turn = True
robo_enabled = True

for op in data:
    current = santa if santas_turn else robo_santa
    current = next_coord(current, op)

    houses.add(current)
    
    if santas_turn:
        santa = current
    else:
        robo_santa = current

    if robo_enabled:
        santas_turn = not santas_turn

print("visited: " + str(len(houses)))