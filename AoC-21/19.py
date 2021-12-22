class EachRotation:
    def __init__(self, point) -> None:
        self.funcs = [lambda x: (3,3,3), rotate_y, rotate_x, rotate_z, rotate_z]
        self.i = 0
        self.point = point
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.i > len(self.funcs):
            raise StopIteration
        elif self.i != 0:
            self.point = self.funcs[self.i-1](self.point)
        self.i += 1
        return self.point

def rotate_x(point):
    return (point[0], -point[2], point[1])

def rotate_y(point):
    return (point[2], point[1], -point[0])

def rotate_z(point):
    return (-point[1], point[0], point[2])





with open("input\\19.txt") as f:
    data = [i.split("\n") for i in f.read().split("\n\n")]

t = set()
for i in EachRotation((1,2,3)):
    t.add(i)

exit()
scanners = {}
for entry in data:
    scanner_id = entry[0][12:-4]
    points = [tuple(map(int, i.split(","))) for i in entry[1:]]
    scanners[scanner_id] = points