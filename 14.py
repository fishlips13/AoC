with open("input/14.txt") as f:
    data = [[j if not j.startswith("mem[") else int(j[4:-1]) for j in i.split(" = ")] for i in f.read().split("\n")]

mask = ""
memory = {}

for cmd, value in data:

    if cmd == "mask":
        mask = cmd
        continue

    if value not in memory:
        memory[value] = 0

    temp = memory[value]