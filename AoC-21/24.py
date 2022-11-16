with open("input\\24.txt") as f:
    cmds = [i.split(" ") for i in f.read().split("\n")]

    it_digits = iter([int(i) for i in "18113181571611"])

    regs = {"w" : 0, "x" : 0, "y" : 0, "z" : 0}
    for i, cmd in enumerate(cmds):
        i += 1
        val1 = int(cmd[1]) if cmd[1].lstrip('-').isnumeric() else regs[cmd[1]]
        if len(cmd) == 3:
            val2 = int(cmd[2]) if cmd[2].lstrip('-').isnumeric() else regs[cmd[2]]

        if cmd[0] == "inp":
            regs[cmd[1]] = next(it_digits)
        elif cmd[0] == "add":
            regs[cmd[1]] = val1 + val2
        elif cmd[0] == "mul":
            regs[cmd[1]] = val1 * val2
        elif cmd[0] == "div":
            regs[cmd[1]] = val1 // val2
        elif cmd[0] == "mod":
            regs[cmd[1]] = val1 % val2
        elif cmd[0] == "eql":
            regs[cmd[1]] = 1 if val1 == val2 else 0

print(f"Regs: {regs}")

# Part 1 (manual)
# 99429795993929

# Part 2 (manual)
# 11617518131181

# 123 44 55 6776 321 <- Pairs
# ||| || || |||| |||
# 005 06 40 7020 070 <- Key
# ||| || || |||| |||
# 929 39 95 9792 499 <- Part 1
# 116 17 51 8131 181 <- Part 2

#  2
#  |  4
#  |  |  8
#  |  |  |   7
#  |  |  |   |  12
#  |  |  |   | -14
#  |  |  |  -0
#  |  |  |      14
#  |  |  |     -10
#  |  |  |   6
#  |  |  | -12
#  |  | -3
#  |-11
# -2
