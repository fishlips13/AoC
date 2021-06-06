from intcode import Intcode

def in_map(coords, grid_map):
    if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(grid_map[0]) - 1 or coords[1] >= len(grid_map) - 1:
        return False
    return True

def get_side_dir(coords, direction, grid_map):
    direction_swap = (direction[1], -direction[0]) #  L
    if in_map((coords[0] + direction_swap[0], coords[1] + direction_swap[1]), grid_map):
        yield (direction_swap, "L")

    direction_swap = (-direction[1], direction[0]) # R
    if in_map((coords[0] + direction_swap[0], coords[1] + direction_swap[1]), grid_map):
        yield (direction_swap, "R")

ascii_interface = Intcode()

camera_output = []
while ascii_interface.status == "awaiting output":
    camera_output.append(ascii_interface.output_signal())

camera_output = "".join([chr(i) for i in camera_output]).split()
scaff = [[j for j in i] for i in camera_output]

curr = None
for y in enumerate(scaff):
    for x in enumerate(y[1]):
        if x[1] == "^":
            curr = (x[0], y[0])
            break
    if curr:
        break

direc = (-1, 0)
seg_len = 0
cmds = []
while direc != (0, 0):
    candi = (curr[0] + direc[0], curr[1] + direc[1])
    if in_map(candi, scaff) and scaff[candi[1]][candi[0]] == "#":
        curr = candi
        seg_len += 1
    else:
        cmds.append(seg_len)
        seg_len = 0

        for side_direc in get_side_dir(curr, direc, scaff):
            if scaff[curr[1] + side_direc[0][1]][curr[0] + side_direc[0][0]] == "#":
                direc = side_direc[0]
                cmds.append(side_direc[1])
                break
            direc = (0, 0)

move = ["A,B,A,B,C,C,B,A,B,C\n", "L,12,L,10,R,8,L,12\n", "R,8,R,10,R,12\n", "L,10,R,12,R,8\n", "n\n"]

for item in move:
    while ascii_interface.status == "awaiting output": # Discard prompts
        ascii_interface.output_signal()
    for val in item:
        ascii_interface.input_signal(ord(val)) # Read in instructions

final = []
while ascii_interface.status == "awaiting output": # Outputs the map at the end, DISCARD
    final.append(ascii_interface.output_signal())

print(final[-1])


# THIS IS A FK'N MESS. JUST NO