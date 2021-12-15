import re
from functools import reduce

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def solve_discs(data):
    mods = []
    rems = []
    for i, line in enumerate(data, 1):
        hits = re.findall(r"\d+", line)
        size = int(hits[1])
        start = int(hits[-1])
        mods.append(size)
        rems.append(size - (start + i) % size)

    return chinese_remainder(mods, rems)

with open("input\\15.txt") as f:
    data = f.read().split("\n")

print(f"First success time: {solve_discs(data)}")
data.append("Disc #7 has 11 positions; at time=0, it is at position 0.")
print(f"Second success time: {solve_discs(data)}")


# low 123524
# high 390008
# ??? 317371


# low 1640056