from intcode import ASCII_Computer
from itertools import combinations

droid = ASCII_Computer()
items_all = set()
items_held = set()
items_floor = set()

f = open("cmds.txt")
cmds = f.read().split("\n")
f.close()

droid.print_output = False
for cmd in cmds:
    droid.input_cmd(cmd)
    if cmd.startswith("take"):
        items_all.add(cmd[5:])
        items_held.add(cmd[5:])
droid.print_output = False

for count in range(len(items_all)):
    done = False
    for comb in combinations(items_all, count):
        items_comb = set(comb)
        to_drop = items_held - items_comb
        to_take = items_comb - items_held

        while to_drop:
            drop_item = to_drop.pop()
            droid.input_cmd("drop " + drop_item)

        while to_take:
            item_take = to_take.pop()
            droid.input_cmd("take " + item_take)

        items_held = items_comb

        droid.input_cmd("east")

        output = droid.output_cmd()
        
        if output.find("lighter") == -1 and output.find("heavier") == -1:
            print(items_comb)
            print(output)
            done = True
            break
    print("done " + str(count))
    if done:
        break

droid.print_output = True
print("done")

while True:
    cmd = input()
    droid.input_cmd(cmd)

    if cmd == "quit":
        quit()