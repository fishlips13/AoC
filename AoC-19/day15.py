from intcode import Intcode
from queue import PriorityQueue

# class Cell:

#     def __init__(self, coords, c_type):
#         self.coords = coords
#         self.c_type = c_type
#         self.dist = 0
#         self.prev = None

def manhatten(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def nbrs(cell):
    n = []
    n.append((cell[0] + 1, cell[1]))
    n.append((cell[0] - 1, cell[1]))
    n.append((cell[0], cell[1] + 1))
    n.append((cell[0], cell[1] - 1))
    return n

def coord_to_dir(ori, dest):
    if manhatten(ori, dest) != 1:
        raise Exception("Bad move")

    if dest[0] - ori[0] == -1: # west
        return 3
    elif dest[0] - ori[0] == 1: # east
        return 4
    elif dest[1] - ori[1] == 1: # north
        return 1
    elif dest[1] - ori[1] == -1: # south
        return 2

def dir_to_coord(ori, direction):
    if direction not in [1,2,3,4]:
        raise Exception("Bad direction")

    if direction == 3: # west
        return (ori[0] - 1, ori[1])
    elif direction == 4: # east
        return (ori[0] + 1, ori[1])
    elif direction == 1: # north
        return (ori[0], ori[1] + 1)
    elif direction == 2: # south
        return (ori[0], ori[1] - 1)

def short_path(ori, dest, cells):
    o_set = {ori}
    c_set = {ori : None}

    while True:
        curr = o_set.pop()

        if curr == dest:
            path = []

            while curr:
                path.append(curr)
                curr = c_set[curr]
            return path[:-1][::-1]

        nbr_list = nbrs(curr)
        for nbr in nbr_list:
            if nbr not in c_set and nbr in cells and (cells[nbr] or nbr == dest):
                o_set.add(nbr)
                c_set[nbr] = curr

robot = Intcode()

cells = {(0, 0): 1, (0, 1): 0, (1, 0): 0, (0, -1): 0, (-1, 0): 0}
oxygen = None
unknown_cells = {(0, 1), (1, 0), (0, -1), (-1, 0)}
robot_cell = (0, 0)

while unknown_cells:
    unknown_cell = unknown_cells.pop()
    path = short_path(robot_cell, unknown_cell, cells)

    report = None
    for step in path:
        robot.input_signal(coord_to_dir(robot_cell, step))
        report = robot.output_signal()
        if report:
            robot_cell = step
    
    cells[unknown_cell] = report

    if report:
        nbr_list = nbrs(robot_cell)
        for nbr in nbr_list:
            if nbr not in cells:
                cells[nbr] = 0
                unknown_cells.add(nbr)

    if report == 2:
        oxygen = unknown_cell

    if len(cells) % 100 == 0:
        print(len(cells))

print("done")
path = short_path((0, 0), oxygen, cells)
print(len(path))

dist_max = 0

for cell in cells:
    path = short_path(oxygen, cell, cells)
    dist_max = max(dist_max, len(path))

print(dist_max-1)