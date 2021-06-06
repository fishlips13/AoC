f = open("data.txt")
d = f.read().split()
f.close()

b = {}
p = {}

for i in d:
    b1 = i[:3]
    b2 = i[4:]

    if (not b1 in b):
        b[b1] = []
    if (not b2 in b):
        b[b2] = []
    if (not b2 in b[b1]):
        b[b1].append(b2)
    
    p[b2] = b1

v = {"COM"}
o = 1
t = 0

while v:
    u = set()
    while v:
        c = v.pop()
        for i in b[c]:
            u.add(i)
            b[c] = (b[c], o)
    v.update(u)
    o += 1

s = set()
y = set()

c = "SAN"
while c != "COM":
    a = p[c]
    s.add(c)
    c = a

c = "YOU"
while c != "COM":
    a = p[c]
    y.add(c)
    c = a

z = s.intersection(y)

smol = -1
for i in z:
    smol = max(smol, b[i][1])

total = b[p["SAN"]][1] + b[p["YOU"]][1] - (2 * smol ) - 2

count = 0
yo = "SAN"
while yo != "YC9":
    yo = p[yo]
    count += 1

print(total)