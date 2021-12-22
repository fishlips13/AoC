from copy import deepcopy

class Adjacents:
    def __init__(self, point) -> None:
        self.i = -1
        self.point = point
        self.offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.offsets):
            raise StopIteration
        return (self.point[0] + self.offsets[self.i][0], self.point[1] + self.offsets[self.i][1])

def enhance(cells, reps, x_min, y_min, x_max, y_max):
    for x in range(x_min - reps, x_max + reps):
        for y in range(y_min - reps, y_max + reps):
            if (x, y) not in cells:
                cells[(x, y)] = "."

    for i in range(reps):
        cells_new = {}

        for coord in cells:
            cell_str = "".join([cells[adj] if adj in cells else ("." if i % 2 == 0 else "#") for adj in Adjacents(coord)])
            cell_str = cell_str.replace("#", "1").replace(".", "0")
            cells_new[coord] = iea[int(cell_str, 2)]
        
        cells = cells_new
    
    return cells

with open("input\\20.txt") as f:
    data = f.read().split("\n")

cells = {}
iea = data[0]
x_min, y_min, x_max, y_max = 0, 0, len(data[2]), len(data) - 2

for y, line in enumerate(data[2:]):
    for x, cell in enumerate(line):
        cells[(x, y)] = cell

cells_2 = enhance(deepcopy(cells), 2, x_min, y_min, x_max, y_max)
cells_50 = enhance(deepcopy(cells), 50, x_min, y_min, x_max, y_max)

lit_total_2 = sum(1 if i == "#" else 0 for i in cells_2.values())
print(f"Total Lit Cells (2): {lit_total_2}")

lit_total_50 = sum(1 if i == "#" else 0 for i in cells_50.values())
print(f"Total Lit Cells (50): {lit_total_50}")