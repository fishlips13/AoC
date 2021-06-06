import itertools
from sys import maxsize

def gec(s, c):
    if c[0] == "R":
        return (s[0] + c[1], s[1], s[2] + abs(c[1]))
    elif c[0] == "U":
        return (s[0], s[1] + c[1], s[2] + abs(c[1]))
    elif c[0] == "L":
        return (s[0] - c[1], s[1], s[2] + abs(c[1]))
    else:
        return (s[0], s[1] - c[1], s[2] + abs(c[1]))

def pairwise(i):
    a, b = itertools.tee(i)
    next(b, None)
    return zip(a, b)

def within(v, a, b):
    if v <= a and v >= b or v >=a and v <= b:
        return True
    return False

f = open("data.txt")
w1 = [i for i in f.readline().split(",")]
w2 = [i for i in f.readline().split(",")]
w1[-1] = w1[-1].strip()
w2[-1] = w2[-1].strip()
f.close()

w1 = [(i[0], int(i[1:])) for i in w1]
w2 = [(i[0], int(i[1:])) for i in w2]

r1 = [(0, 0, 0)]
for i in w1:
    r1.append(gec(r1[-1], i))

r2 = [(0, 0, 0)]
for i in w2:
    r2.append(gec(r2[-1], i))

d = maxsize
for i in pairwise(r1):
    for j in pairwise(r2):
        if i[0][1] != 0 or j[0][1] != 0:
            if i[0][0] == i[1][0] and j[0][1] == j[1][1] and within(i[0][0], j[0][0], j[1][0]) and within(j[0][1], i[0][1], i[1][1]): # if perp, first vert
                d = min(d, j[1][2] - abs(j[1][0] - i[0][0]) + i[1][2] - abs(i[1][1] - j[0][1])) #(i[0][0], j[0][1])
            elif i[0][1] == i[1][1] and j[0][0] == j[1][0] and within(i[0][1], j[0][1], j[1][1]) and within(j[0][0], i[0][0], i[1][0]): # if perp, first hor
                d = min(d, i[1][2] - abs(i[1][0] - j[0][0]) + j[1][2] - abs(j[1][1] - i[0][1])) #(i[0][1], j[0][0])

print(d)