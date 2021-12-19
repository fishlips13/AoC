def run(cmds, regs):
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

def parse_cmd(cmd:str, arg1:str, arg2:str = None):
    arg1 = int(arg1) if arg1.lstrip("-").isdigit() else arg1
    if arg2:
        arg2 = int(arg2) if arg2.lstrip("-").isdigit() else arg2
    return (cmd, arg1, arg2)

with open("input\\12.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]
    
cmds = []
for line in data:
    cmds.append(parse_cmd(*line))

regs1 = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
regs2 = {"a" : 0, "b" : 0, "c" : 1, "d" : 0}

print(f"'a' register final: {run(cmds, regs1)}")
print(f"'a' register final (initialised): {run(cmds, regs2)}")