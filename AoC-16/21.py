with open("input\\21.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

password1 = "abcdefgh"
password2 = "fbgdceah"

cmds = []
for line in data:
    if line[0] == "swap":
        if line[1] == "position":
            cmds.append(("swap_pos", int(line[2]), int(line[5])))
        else:
            cmds.append(("swap_let", line[2], line[5]))
    elif line[0] == "rotate":
        if line[1] != "based":
            cmds.append(("rotate_stp", int(line[2]) * (1 if line[1] == "left" else -1), None))
        else:
            cmds.append(("rotate_pos", line[6], None))
    elif line[0] == "reverse":
        cmds.append(("reverse", int(line[2]), int(line[4])))
    elif line[0] == "move":
        cmds.append(("move", int(line[2]), int(line[5])))

def scramble(password):
    base = [i for i in password]
    print("".join(base))
    for cmd, arg1, arg2 in cmds:
        if cmd == "swap_pos":
            temp = base[arg1]
            base[arg1] = base[arg2]
            base[arg2] = temp
        elif cmd == "swap_let":
            i1 = base.index(arg1)
            i2 = base.index(arg2)
            temp = base[i1]
            base[i1] = base[i2]
            base[i2] = temp
        elif cmd == "rotate_stp":
            i = arg1 % len(base)
            base = base[i:] + base[:i]
        elif cmd == "rotate_pos":
            i = base.index(arg1)
            i = ((1 + i + (1 if i >= 4 else 0)) * -1) % len(base)
            base = base[i:] + base[:i]
        elif cmd == "reverse":
            sub = base[arg1:arg2+1]
            sub.reverse()
            base = base[:arg1] + sub + base[arg2+1:]
        elif cmd == "move":
            temp = base.pop(arg1)
            base.insert(arg2, temp)
        print("".join(base))

    return "".join(base)

def unscramble(password):
    base = [i for i in password]
    rot_pos_map = {1:1, 3:2, 5:3, 7:4, 2:6, 4:7, 6:0, 0:1}

    for cmd, arg1, arg2 in reversed(cmds):
        if cmd == "swap_pos":
            temp = base[arg1]
            base[arg1] = base[arg2]
            base[arg2] = temp
        elif cmd == "swap_let":
            i1 = base.index(arg1)
            i2 = base.index(arg2)
            temp = base[i1]
            base[i1] = base[i2]
            base[i2] = temp
        elif cmd == "rotate_stp":
            i = -arg1 % len(base)
            base = base[i:] + base[:i]
        elif cmd == "rotate_pos":
            i = rot_pos_map[base.index(arg1)]
            base = base[i:] + base[:i]
        elif cmd == "reverse":
            sub = base[arg1:arg2+1]
            sub.reverse()
            base = base[:arg1] + sub + base[arg2+1:]
        elif cmd == "move":
            temp = base.pop(arg2)
            base.insert(arg1, temp)

    return "".join(base)

print(f"Scrambled Result: {scramble(password1)}")
print(f"Unscrambled Result: {unscramble(password2)}")

#  0 1 2 3 4 5 6 7
#  1 2 3 4 6 7 0 1
#  1 3 5 7 2 4 6 0