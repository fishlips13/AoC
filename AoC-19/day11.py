from intcode import Intcode

robot = Intcode()
cr = (0, 0)
fr = (0, 1)

panels = {cr : 1}

while robot.status != "halted":

    if cr not in panels:
        panels[cr] = 0

    robot.input_signal(panels[cr])
    panels[cr] = robot.output_signal()
    direction = robot.output_signal()

    if direction == 0: # left
        fr = (fr[1], -fr[0])
    else: # right
        fr = (-fr[1], fr[0])
    
    cr = (cr[0] + fr[0], cr[1] + fr[1])

m = [["0"] * 43 for i in range(6)]

for panel in panels:
    m[-panel[1]][-panel[0]] = str(panels[panel])

for i in m:
    i[:] = [" " if j == "0" else j for j in i]

for i in m:
    print("".join(i))

# -42 to 0
#  -5 to 0