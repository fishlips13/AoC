import math
import itertools

def pairwise(i):
    a, b = itertools.tee(i)
    next(b, None)
    return zip(a, b)

l = 240298
u = 784956

c = 0
while l <= u:
    d = [int(i) for i in str(l)]

    t = [0,0,0,0,0,0,0,0,0,0]
    for i in d:
        t[i] += 1

    p = False
    for i in pairwise(d):
        if i[0] == i[1]:
            p = True
        elif i[0] > i[1]:
            p = False
            break
    
    if p and 2 in t:
        c += 1

    l += 1

print(c)