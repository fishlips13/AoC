with open("input\\13.txt") as f:
    data = int(f.read())

coords_adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_open(coord, fav_num):
    x, y = coord
    value = x*x + 3*x + 2*x*y + y + y*y + fav_num
    bit_count = sum(1 for i in  f"{value:b}" if i == "1")
    return bit_count % 2 == 0

def steps_to_dest(origin, destination):
    frontier = set([origin])
    visited = set()
    steps = 0

    while True:
        frontier_next = set()
        while frontier:
            cell = frontier.pop()
            if cell == destination:
                return steps
            visited.add(cell)

            for coord_adj in coords_adj:
                coord_new = (cell[0] + coord_adj[0], cell[1] + coord_adj[1])
                if coord_new[0] < 0 or coord_new[1] < 0 or \
                    coord_new in visited or not is_open(coord_new, data):
                    continue

                frontier_next.add(coord_new)

        frontier = frontier_next
        frontier_next = []
        steps += 1
        
def cells_in_range(origin, range_max):
    frontier = set([origin])
    visited = set()
    steps = 0

    while True:
        frontier_next = set()
        while frontier:
            cell = frontier.pop()
            visited.add(cell)

            for coord_adj in coords_adj:
                coord_new = (cell[0] + coord_adj[0], cell[1] + coord_adj[1])
                if steps >= range_max or coord_new[0] < 0 or coord_new[1] < 0 or \
                    coord_new in visited or not is_open(coord_new, data):
                    continue

                frontier_next.add(coord_new)

        if not frontier_next:
            return len(visited)

        frontier = frontier_next
        frontier_next = []
        steps += 1

origin = (1, 1)
destination = (31, 39)
range_max = 50

print(f"Steps to {destination}: {steps_to_dest(origin, destination)}")
print(f"Reachable in {range_max} steps: {cells_in_range(origin, range_max)}")