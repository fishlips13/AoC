with open("input\\08.txt") as f:
    data = [i.split() for i in f.read().split("\n")]

for cmd in data:
    cmd[2] = int(cmd[2])
    cmd[-1] = int(cmd[-1])

regs = {}
reg_max_ever = -1

for reg1, op, val1, _, reg2, comp, val2 in data:
    if reg1 not in regs:
        regs[reg1] = 0

    if reg2 not in regs:
        regs[reg2] = 0

    if not (comp == ">"  and regs[reg2] >  val2 or \
            comp == "<"  and regs[reg2] <  val2 or \
            comp == ">=" and regs[reg2] >= val2 or \
            comp == "<=" and regs[reg2] <= val2 or \
            comp == "==" and regs[reg2] == val2 or \
            comp == "!=" and regs[reg2] != val2):
        continue
    
    if op == "inc":
        regs[reg1] += val1
    else:
        regs[reg1] -= val1

    reg_max_ever = max(reg_max_ever, max(regs.values()))
    
reg_max_end = max(regs.values())

print(f"Largest Register End: {reg_max_end}")
print(f"Largest Register Ever: {reg_max_ever}")