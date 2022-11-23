from sympy.ntheory import isprime

def parse_cmd(cmd:str, arg1:str, arg2:str = None):
    arg1 = int(arg1) if arg1.lstrip("-").isdigit() else arg1
    if arg2:
        arg2 = int(arg2) if arg2.lstrip("-").isdigit() else arg2
    return (cmd, arg1, arg2)

def run(cmds, regs):
    i = 0
    mul_count = 0

    while True:
        if i < 0 or i >= len(cmds):
            return mul_count

        cmd, arg1, arg2 = cmds[i]

        if cmd == "set":
            if arg2 in regs:
                regs[arg1] = regs[arg2]
            else:
                regs[arg1] = arg2

        elif cmd == "sub":
            regs[arg1] -= regs[arg2] if arg2 in regs else arg2

        elif cmd == "mul":
            regs[arg1] *= regs[arg2] if arg2 in regs else arg2
            mul_count += 1

        elif cmd == "jnz":
            value1 = regs[arg1] if arg1 in regs else arg1
            value2 = regs[arg2] if arg2 in regs else arg2
            if value1 != 0:
                i += value2 - 1

        elif cmd == "nop":
            pass

        i += 1

with open("input\\23.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

cmds = []
for line in data:
    cmds.append(parse_cmd(*line))

regs = {}
for _, arg1, __ in cmds:
    if isinstance(arg1, str) and arg1 not in regs:
        regs[arg1] = 0

mul_count = run(cmds, regs)

lower = (65 * 100) + 100000
upper = lower + 17000
step = 17
non_prime_count = 0

for candi in range(lower, upper + 1, step):
    non_prime_count += 1
    if isprime(candi):
        non_prime_count -= 1

print(f"Coprosessor Mul Count: {mul_count}")
print(f"Coprosessor Non-Prime Count: {non_prime_count}")


# upper (inc) : 106500
# lower (inc) : 123500
# step size   :     17
# value count :   1001