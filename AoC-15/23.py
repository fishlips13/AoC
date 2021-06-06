with open("input/23.txt") as f:
    data = f.read().split("\n")

insts = []

for line in data:
    parts = line.replace(",", "").split(" ")

    if parts[0] == "jmp":
        parts[1] = int(parts[1])
    elif len(parts) == 3:
        parts[2] = int(parts[2])

    insts.append(parts)

a, b = 1, 0
i = 0

while i < len(insts):
    inst = insts[i]

    if inst[0] == "jmp":
        i += inst[1]
        continue

    value = a if inst[1] == "a" else b

    if inst[0] == "jio" and value == 1:
        i += inst[2]
        continue
    elif inst[0] == "jie" and value % 2 == 0:
        i += inst[2]
        continue

    if inst[0] == "hlf":
        value //= 2
    elif inst[0] == "tpl":
        value *= 3
    elif inst[0] == "inc":
        value += 1

    if inst[1] == "a":
        a = value
    else:
        b = value

    i += 1

print(f"b final value: {b}")