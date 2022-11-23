import re

with open("input\\25.txt") as f:
    data = [i.split("\n") for i in f.read().split("\n\n")]

tape = {0 : 0}
cursor = 0
state = data[0][0][-2]
steps = int(re.findall(r"\d+", data[0][1])[0])
instructions = {}

for entry in data[1:]:
    state_name   = entry[0][-2]

    write_0      = int(entry[2][-2])
    move_0       = -1 if re.findall("left", entry[3]) else 1
    state_next_0 = entry[4][-2]
    
    write_1      = int(entry[6][-2])
    move_1       = -1 if re.findall("left", entry[7]) else 1
    state_next_1 = entry[8][-2]

    instructions[state_name] = ((write_0, move_0, state_next_0), (write_1, move_1, state_next_1))

for _ in range(steps):
    write, move, state_next = instructions[state][tape[cursor]]

    tape[cursor] = write
    cursor += move
    state = state_next

    if cursor not in tape:
        tape[cursor] = 0

checksum = sum(i for i in tape.values())

print(f"Checksum: {checksum}")