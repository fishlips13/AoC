data = []
with open("input/01.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

def part1():
    for i in range(len(data)):
        for j in range(len(data)):
            
            a, b = data[i], data[j]
            if data[i] + data[j] == 2020:
                print("Part 1 -> {} + {} = {}, {}".format(a, b, a+b, a*b))
                return

def part2():
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):

                a, b, c = data[i], data[j], data[k]
                if a + b + c == 2020:
                    print("Part 2 -> {} + {} + {} = {}, {}".format(a, b, c, a+b+c, a*b*c))
                    return

part1()
part2()