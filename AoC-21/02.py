with open("input\\02.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]
    data = [(i[0], int(i[1])) for i in data]

position = 0
depth = 0
depth_bad = 0
aim = 0

for command, value in data:
    if command == "up":
        depth_bad -= value
        aim -= value
    elif command == "down":
        depth_bad += value
        aim += value
    else:
        position += value
        depth += aim * value

print(f"Bad position X depth: {position * depth_bad}")
print(f"Good position X depth: {position * depth}")