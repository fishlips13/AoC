from queue import PriorityQueue

room_type_lookup = {3 : "A", 5 : "B", 7 : "C", 9 : "D"}
hallway = {(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)}
blocked = {(3, 1), (5, 1), (7, 1), (9, 1)}
costs = {"A" : 1, "B" : 10, "C" : 100, "D" : 1000}
adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_all_moves(grid:dict, rooms:dict):
    moves = []
    for current, pod_type in grid.items():
        if pod_type not in rooms:
            continue

        frontier = [current]
        visited = set([current])

        while frontier:
            location = frontier.pop()

            for adj in adjacents:
                neigh = (location[0] + adj[0], location[1] + adj[1])

                if neigh not in grid or neigh in visited or grid[neigh] != ".":
                    continue

                frontier.append(neigh)
                visited.add(neigh)

        visited.remove(current)
        visited.difference_update(blocked)

        for target in visited:
            dest_room = rooms[pod_type]

            if  current in hallway and target in hallway or \
                current in hallway and target not in dest_room or \
                current in dest_room and target in dest_room or \
                target not in hallway and target not in dest_room:
                continue

            if current in dest_room:
                valid_move = any([grid[coord] != pod_type for coord in dest_room if current[1] < coord[1]])
            elif target in dest_room:
                valid_move = all([grid[coord] == pod_type for coord in dest_room if target[1] < coord[1]])
            else:
                valid_move = True

            if valid_move:
                moves.append((current, target))

    return moves

def stringify_grid(grid:dict):
    keys_list = list(grid.keys())
    keys_list.sort()
    return "".join([grid[i] for i in keys_list])

def gridify_string(string:str, cells_all:list):
    return {i : j for i, j in zip(cells_all, string)}

def cost(start, end, pod_type):
    x_dist = abs(start[0] - end[0])

    if start in hallway or end in hallway:
        y_dist = abs(start[1] - end[1])
    else:
        y_dist = abs(start[1] - 1) + abs(end[1] - 1)

    return (x_dist + y_dist) * costs[pod_type]

def solve(grid:dict):
    cells_all = list(hallway) + list(blocked)
    rooms = {"A" : [], "B" : [], "C" : [], "D" : []}

    for coord, pod_type in grid.items():
        if pod_type != "." and coord not in hallway and coord not in blocked:
            rooms[room_type_lookup[coord[0]]].append(coord)

    for room in rooms.values():
        room.sort()
        cells_all.extend(room)

    cells_all.sort()

    grid_str = stringify_grid(grid)
    grids_queue = PriorityQueue()
    grids_queue.put((0, grid_str))
    cache = {}

    cost_min = 99999999999999
    while not grids_queue.empty():
        cost_curr, grid_str = grids_queue.get()

        grid_old = gridify_string(grid_str, cells_all)
        moves = find_all_moves(grid_old, rooms)
        if not moves and all([all([grid_old[cell] == room_type for cell in cells]) for room_type, cells in rooms.items()]):
            cost_min = min(cost_min, cost_curr)

        for orig, dest in moves:
            pod_type = grid_old[orig]
            grid_old[dest] = pod_type
            grid_old[orig] = "."

            move_cost = cost_curr + cost(orig, dest, pod_type)
            grid_str = stringify_grid(grid_old)

            if grid_str not in cache or move_cost < cache[grid_str]:
                grids_queue.put((move_cost, grid_str))
                cache[grid_str] = move_cost

            grid_old[orig] = pod_type
            grid_old[dest] = "."
        
    return cost_min

def build_grid(data):
    grid = {}
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell != " " and cell != "#":
                grid[(x,y)] = cell
    return grid

with open("input\\23.txt") as f:
    data = f.read().split("\n")

extra_lines = ["  #D#C#B#A#",
               "  #D#B#A#C#"]

data_extra = data[:3] + extra_lines + data[3:]

grid_simple = build_grid(data)
grid_extra = build_grid(data_extra)

print(f"Minimum Cost: {solve(grid_simple)}")
print(f"Minimum Cost: {solve(grid_extra)}")