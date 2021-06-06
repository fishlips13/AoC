import math

d = []

f = open("data.txt")
d = [int(i) for i in f.read().split()]
f.close()

t = 0

for v in d:
    s = math.floor(v / 3) - 2
    t += s

    while True:
        s = math.floor(s / 3) - 2

        if s > 0:
            t += s
        else:
            break


print(t)