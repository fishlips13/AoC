class Cell:
    def __init__(self, coords):
        self.coords = coords
        self.neighbours = []
        self.teleporter = None

class Teleporter:
    def __init__(self, x, y, data):
        self.tp_id = None
        self.cell_in = None
        self.cell_out = None

        char_positions = [(x + 1, y), (x, y + 1)]
        dot_positions = [(x - 1, y), (x, y - 1), (x + 2, y), (x, y + 2)]

        for p in char_positions:
            if in_map(p[0], p[1], data) and data[p[1]][p[0]] != " ":
                char2 = data[p[1]][p[0]]
                break

        for p in dot_positions:
            if in_map(p[0], p[1], data) and data[p[1]][p[0]] == ".":
                dot = (p[0], p[1])
                break

        self.tp_id = data[y][x] + char2
        self.cell_in = None
        self.cell_out = None

        if in_center(x, y, data):
            self.cell_in = dot
        else:
            self.cell_out = dot

    def is_inner(self, cell):
        if cell.coords == self.cell_in:
            return True
        return False

    def is_entry_exit(self):
        if self.tp_id == "AA" or self.tp_id == "ZZ":
            return True
        return False

    def get_other(self, origin, depth):
        if self.cell_in == origin.coords:
            return (self.cell_out, depth + 1)
        else:
            return (self.cell_in, depth - 1)
    
    @staticmethod
    def combine(tp1, tp2):
        if tp1.cell_in:
            tp1.cell_out = tp2.cell_out
        else:
            tp1.cell_in = tp2.cell_in

        return tp1

def in_map(x, y, data):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return False
    return True

def in_center(x, y, data):
    if x == 0 or y == 0 or x == len(data[0]) - 2 or y == len(data) - 2:
        return False
    return True

def get_card_neighbours(coords, cells):
    neighbours = []
    all_relative = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for relative in all_relative:
        candidate = (coords[0] + relative[0], coords[1] + relative[1])
        if candidate in cells:
            neighbours.append(cells[candidate])

    return neighbours

f = open("data.txt")
data = f.read().split("\n")
f.close()

cells = {}
teleporters = {}
tp_cache = set()

for y in range(len(data)):
    for x in range(len(data[0])):
        content = data[y][x]

        if content == "#" or content == " ":
            continue
        elif content == ".":
            cells[(x, y)] = Cell((x, y))
        elif (x, y) not in tp_cache:
            new_tp = Teleporter(x, y, data)

            if new_tp.tp_id in teleporters:
                new_tp = Teleporter.combine(new_tp, teleporters[new_tp.tp_id])

            teleporters[new_tp.tp_id] = new_tp

            tp_cache.add((x + 1, y))
            tp_cache.add((x, y + 1))

for cell in cells:
    cells[cell].neighbours = get_card_neighbours(cells[cell].coords, cells)

for tp in teleporters.values():
    if tp.tp_id != "AA" and tp.tp_id != "ZZ":
        cells[tp.cell_in].teleporter = tp
        cells[tp.cell_out].teleporter = tp

origin_coords = teleporters["AA"].cell_out
dest_coords = teleporters["ZZ"].cell_out

frontier = {(origin_coords, 0)}
visited = {(origin_coords, 0)}
distance = 0

while (dest_coords, 0) not in visited:
    new_frontier = set()

    for frontier_cell in frontier:
        cell = cells[(frontier_cell[0][0], frontier_cell[0][1])]
        depth = frontier_cell[1]

        for neighbour in cell.neighbours:
            coords_depth = (neighbour.coords, depth)
            if coords_depth not in visited:
                new_frontier.add(coords_depth)
                visited.add(coords_depth)
        
        if cell.teleporter and not cell.teleporter.is_entry_exit() and (cell.teleporter.is_inner(cell) or depth != 0):
            other = cell.teleporter.get_other(cell, depth)
            if other not in visited:
                new_frontier.add(other)
                visited.add(other)
    
    frontier = new_frontier
    distance += 1

print(distance)