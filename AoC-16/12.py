with open("input\\12.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

cmds = []
for line in data:
    if line[0] == "cpy":
        arg1 = int(line[1]) if line[1].isdigit() else line[1]
        cmds.append((line[0], arg1, line[2]))
    elif line[0] == "inc" or line[0] == "dec":
        cmds.append((line[0], line[1]))
    elif line[0] == "jnz":
        cmds.append((line[0], line[1], int(line[2])))

def run(regs):
    i = 0
    while i < len(cmds):
        cmd = cmds[i][0]
        arg1 = cmds[i][1]
        if len(cmds[i]) == 3:
            arg2 = cmds[i][2]

        if cmd == "cpy":
            if arg1 in regs:
                regs[arg2] = regs[arg1]
            else:
                regs[arg2] = arg1
        elif cmd == "inc":
            regs[arg1] += 1
        elif cmd == "dec":
            regs[arg1] -= 1
        elif cmd == "jnz":
            value = regs[arg1] if arg1 in regs else arg1
            if value != 0:
                i += arg2 - 1

        i += 1
    
    return regs["a"]

regs1 = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
regs2 = {"a" : 0, "b" : 0, "c" : 1, "d" : 0}

print(f"'a' register final: {run(regs1)}")
print(f"'a' register final (initialised): {run(regs2)}")