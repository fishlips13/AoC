from copy import deepcopy

with open("input\\05.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

instrs1 = deepcopy(data)
steps1 = 0
i = 0
while i < len(instrs1):
    jump = instrs1[i]
    instrs1[i] += 1
    i += jump
    steps1 += 1

instrs2 = deepcopy(data)
steps2 = 0
i = 0
while i < len(instrs2):
    jump = instrs2[i]
    instrs2[i] += -1 if jump >= 3 else 1
    i += jump
    steps2 += 1

print(f"Steps to Exit 1: {steps1}")
print(f"Steps to Exit 2: {steps2}")