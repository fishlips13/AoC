from copy import deepcopy

def run(cmds, regs):
    i = 0
    while i < len(cmds):
        cmd, arg1, arg2 = cmds[i]

        if cmd == "cpy" and arg2 in regs:
            if arg1 in regs:
                regs[arg2] = regs[arg1]
            else:
                regs[arg2] = arg1

        elif cmd == "inc":
            regs[arg1] += 1

        elif cmd == "dec":
            regs[arg1] -= 1

        elif cmd == "jnz":
            value1 = regs[arg1] if arg1 in regs else arg1
            value2 = regs[arg2] if arg2 in regs else arg2
            if value1 != 0:
                i += value2 - 1

        elif cmd == "tgl":
            i_tgl = i + regs[arg1]
            if i_tgl < len(cmds):
                tgl_cmd, tgl_arg1, tgl_arg2 = cmds[i_tgl]

                if not tgl_arg2:
                    if tgl_cmd == "inc":
                        cmd_new = "dec"
                    else:
                        cmd_new = "inc"
                else:
                    if tgl_cmd == "jnz":
                        cmd_new = "cpy"
                    else:
                        cmd_new = "jnz"

                cmds[i_tgl] = (cmd_new, tgl_arg1, tgl_arg2)
            
        i += 1
    
    return regs["a"]

def parse_cmd(cmd:str, arg1:str, arg2:str = None):
    arg1 = int(arg1) if arg1.lstrip("-").isdigit() else arg1
    if arg2:
        arg2 = int(arg2) if arg2.lstrip("-").isdigit() else arg2
    return (cmd, arg1, arg2)

with open("input\\23.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

regs1 = {"a" : 7, "b" : 0, "c" : 0, "d" : 0}
regs2 = {"a" : 12, "b" : 0, "c" : 0, "d" : 0}

cmds1 = []
for line in data:
    cmds1.append(parse_cmd(*line))
cmds2 = deepcopy(cmds1)

print(f"Safe Value: {run(cmds1, regs1)}")
print(f"Safe Value: {run(cmds2, regs2)}")

# low   8777