from math import gcd, atan2
from copy import deepcopy

def in_map(x, y, m):
    if x < 0 or y < 0 or x >= len(m[0]) or y >= len(m):
        return False
    return True

f = open("data.txt")
orig = [[j for j in i] for i in f.read().split()]
f.close()

base = (20, 21)
xb = 20
yb = 21

line = {}

# count_max = 0
# for yb in range(len(orig)):
#     for xb in range(len(orig[0])):
# if m[yb][xb] == "#":

m = orig

rmax = max(xb - 0, yb - 0, len(m[0]) - xb - 1, len(m) - yb - 1)
count = 0

for r in range(1, rmax+1):
    xc = xb - r
    yc = yb - r
    colls = []

    for i in range(2 * r):
        yc += 1
        if not in_map(xc, yc, m):
            continue
        if m[yc][xc] == "#":
            colls.append((xc, yc))
            count += 1
    for i in range(2 * r):
        xc += 1
        if not in_map(xc, yc, m):
            continue
        if m[yc][xc] == "#":
            colls.append((xc, yc))
            count += 1
    for i in range(2 * r):
        yc -= 1
        if not in_map(xc, yc, m):
            continue
        if m[yc][xc] == "#":
            colls.append((xc, yc))
            count += 1
    for i in range(2 * r):
        xc -= 1
        if not in_map(xc, yc, m):
            continue
        if m[yc][xc] == "#":
            colls.append((xc, yc))
            count += 1
    
    for c in colls:
        cb = ((c[1] - yb) * -1.0, c[0] - xb)

        angle = atan2(cb[1], cb[0]) * 57.295779513
        if angle < 0.0:
            angle = 360.0 + angle

        line[angle] = [c]

        g = gcd(c[0] - xb, c[1] - yb)
        step = ((c[0] - xb) // g, (c[1] - yb) // g)

        xf = c[0] + step[0]
        yf = c[1] + step[1]

        while in_map(xf, yf, m):
            if m[yf][xf] == "#":
                line[angle].append((xf, yf))
            m[yf][xf] = "X"
            xf += step[0]
            yf += step[1]

final = None
lasered = 0
while not final:
    for i in sorted(line):
        if lasered == 199:
            final = line[i][0]
            break
        else:
            del(line[i][0])
            lasered += 1
        if len(line[i]) == 0:
            del(line[i])

print(final)

# list of string data structure
# iterate all positions
# if asteroid
#   check all positions in square circles by radius
#       if asteroid (not blocked, not empty)
#           count
#           find minimum step to position
#           project blocked from position by step to map edge

# for r to furthest edge of map (from c(0,0))
#   make empty list
#   go to corner bottom left arbitary
#   scan up 2r, right 2r, down 2r, left 2r
#       if asteroid
#           add coord to list
#           count
#   resolve collisions

# for collison in list
#   gcd(x,y)
#   x,y /= gcd -> smallest step
#   while on the map
#       (x,y) + smallest step -> blocked vision