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
                
        elif cmd == "add":
            regs[arg1] += regs[arg2]

        elif cmd == "mul":
            regs[arg1] *= regs[arg2]

        elif cmd == "nop":
            pass

        elif cmd == "out":
            yield regs[arg1]
            
        i += 1

def parse_cmd(cmd:str, arg1:str, arg2:str = None):
    arg1 = int(arg1) if arg1.lstrip("-").isdigit() else arg1
    if arg2:
        arg2 = int(arg2) if arg2.lstrip("-").isdigit() else arg2
    return (cmd, arg1, arg2)

def find_lowest_clock():
    value = 0
    while True:
        regs = {"a" : value, "b" : 0, "c" : 0, "d" : 0}
        cache = set()

        program = run(cmds, regs)
        expected = 0
        while True:
            signal = next(program)
            if signal != expected:
                break

            state = ",".join([str(regs[i]) for i in regs])
            if state in cache:
                return value

            cache.add(state)
            expected = (expected + 1) % 2

        value += 1

with open("input\\25.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

cmds = []
for line in data:
    cmds.append(parse_cmd(*line))

print(f"Lowest Clock: {find_lowest_clock()}")