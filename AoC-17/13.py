with open("input\\13.txt") as f:
    data = [[int(j) for j in i.split(": ")] for i in f.read().split("\n")]

dumb_cost = 0
for depth, range in data:
    if depth % (2 * (range - 1)) == 0:
        dumb_cost += depth * range

delay = 0
while True:
    valid = True

    for depth, range in data:
        if (depth + delay) % (2 * (range - 1)) == 0:
            valid = False
            break
    
    if valid:
        break

    delay += 1

print(f"Dumb Cost: {dumb_cost}")
print(f"Earliest Delay: {delay}")