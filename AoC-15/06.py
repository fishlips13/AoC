from itertools import permutations

class LightOp:
    def __init__(self, bottom_left, top_right, _type):
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.type = _type

    def collides(self, coord):
        if coord[0] >= self.bottom_left[0] and coord[1] >= self.bottom_left[1] and \
            coord[0] <= self.top_right[0] and coord[1] <= self.top_right[1]:
            return True

        return False

with open("input/06.txt") as f:
    data = [[j for j in i.split(" ") if j != "turn" and j != "through"] for i in f.read().split("\n")]

ops = []
for item in data:
    bottom_left = tuple([int(i) for i in item[1].split(",")])
    top_right = tuple([int(i) for i in item[2].split(",")])
    ops.append(LightOp(bottom_left, top_right, item[0]))

def part1():
    print("part1")
    on_count = 0
    for x in range(1000):

        if x % 100 == 0:
            print(str(x/10) + "%")

        for y in range(1000):
            coord = (x, y)

            toggle_count = 0
            lit = False
            for op in reversed(ops):
                if op.collides(coord):
                    if op.type == "toggle":
                        toggle_count += 1
                    else:
                        lit = op.type == "on"
                        break

            if toggle_count % 2 == 1:
                lit = not lit

            if lit:
                on_count += 1

    print("lit count: " + str(on_count))

def part2():
    print("part2")

    total = 0
    for x in range(1000):

        if x % 100 == 0:
            print(str(x/10) + "%")
            
        for y in range(1000):
            coord = (x, y)

            brightness = 0
            for op in ops:
                if op.collides(coord):
                    if op.type == "toggle":
                        brightness += 2
                    elif op.type == "on":
                        brightness += 1
                    else:
                        brightness = max(0, brightness - 1)

            total += brightness

    print("total brightness: " + str(total))

part1()
part2()