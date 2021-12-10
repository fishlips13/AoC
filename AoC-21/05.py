import re

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

        self.x_min = min(x1, x2)
        self.x_max = max(x1, x2)
        self.y_min = min(y1, y2)
        self.y_max = max(y1, y2)

    def is_vertical(self):
        return self.x1 == self.x2
    
    def is_horizontal(self):
        return self.y1 == self.y2

with open("input\\05.txt") as f:
    data = [[int(j) for j in re.findall(r"\d+", i)] for i in f.read().split("\n")]

level_lines = []
diagonal_lines = []

for line in data:
    line = Line(*line)
    if line.is_vertical() or line.is_horizontal():
        level_lines.append(line)
    else:
        diagonal_lines.append(line)

points = set()
overlaps_level = set()
overlaps_diagonal = set()

for line in level_lines:
    if line.is_vertical():
        for point in [(line.x1, y) for y in range(line.y_min, line.y_max + 1)]:
            if point in points:
                overlaps_level.add(point)
            points.add(point)
    elif line.is_horizontal():
        for point in [(x, line.y1) for x in range(line.x_min, line.x_max + 1)]:
            if point in points:
                overlaps_level.add(point)
            points.add(point)

for line in diagonal_lines:
    x_sign = 1 if line.x1 < line.x2 else -1
    y_sign = 1 if line.y1 < line.y2 else -1
    for point in [(x, y) for x, y in zip(range(line.x1, line.x2 + x_sign, x_sign), range(line.y1, line.y2 + y_sign, y_sign))]:
        if point in points and point:
            overlaps_diagonal.add(point)
        points.add(point)

print(f"Level Overlaps: {len(overlaps_level)}")
print(f"All Overlaps: {len(overlaps_level.union(overlaps_diagonal))}")