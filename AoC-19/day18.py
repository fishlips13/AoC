from copy import deepcopy
import time

class Cell:
    def __init__(self, coords, content):
        self.coords = coords
        self.content = content
        self.neighbours = []
        self.previous = None

class Key:
    def __init__(self, cell, key):
        self.cell = cell
        self.key = key
        self.other_keys = {}

def explore(origin, cells):
    frontier = {origin.coords}
    visited = {origin.coords}

    while frontier:
        frontier_cell = frontier.pop()
        cell = cells[(frontier_cell[0], frontier_cell[1])]

        for neighbour in cell.neighbours:
            if neighbour.coords not in visited:
                neighbour.previous = cell
                frontier.add(neighbour.coords)
                visited.add(neighbour.coords)

def shortest_path(robot_keys, all_keys, held_keys, cache):

    floor_keys = all_keys.keys() - held_keys.keys()
    if not floor_keys:
        return 0

    cache_key = "".join(sorted(floor_keys)) + "-" + "".join(sorted(robot_keys.keys()))
    if cache_key in cache:
        return cache[cache_key]

    distance_min = 9999999999999

    for robot_key in robot_keys:
        for floor_key in floor_keys:

            # Is target key accessible by robot?
            if floor_key not in robot_keys[robot_key].other_keys:
                continue
            
            # Shortened reference to path: robot -> target key
            robot_to_floor_path = robot_keys[robot_key].other_keys[floor_key]

            # Doors locked between robot and target key?
            if robot_to_floor_path[0] - held_keys.keys():
                continue

            new_keys = dict(held_keys)
            new_keys[floor_key] = all_keys[floor_key]

            new_robot_keys = dict(robot_keys)
            new_robot_keys[floor_key] = all_keys[floor_key]
            del(new_robot_keys[robot_key])

            distance_to_floor_key = robot_to_floor_path[1]
            distance_shortest = shortest_path(new_robot_keys, all_keys, new_keys, cache)

            distance_min = min(distance_min, distance_to_floor_key + distance_shortest)

    cache[cache_key] = distance_min

    return distance_min

def clear(cells):
    for cell in cells:
        cells[cell].previous = None

def get_card_neighbours(coords, cells):
    neighbours = []
    all_relative = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for relative in all_relative:
        candidate = (coords[0] + relative[0], coords[1] + relative[1])
        if candidate in cells:
            neighbours.append(cells[candidate])

    return neighbours

f = open("data.txt")
data = f.read().split()
f.close()

cells = {}
all_keys = {}
entrances = {}

entrance_symbols = {"£", "$", "%", "&"}

for y in range(len(data)):
    for x in range(len(data[0])):
        coords = (x, y)
        content = data[y][x]

        if content == "#":
            continue
        elif content == "@":
            content = (entrance_symbols - entrances.keys()).pop()
        
        cells[coords] = Cell(coords, content)

        if content >= "a" and content <= "z" or content in entrance_symbols:
            all_keys[content] = Key(cells[coords], content)

        if content in entrance_symbols:
            entrances[content] = all_keys[content]

for cell in cells:
    cells[cell].neighbours = get_card_neighbours(cells[cell].coords, cells)

for key_origin in all_keys:
    explore(all_keys[key_origin].cell, cells)

    for key_dest in all_keys:
        if key_origin == key_dest:
            continue

        distance = 0
        reqs = set()
        current_cell = all_keys[key_dest].cell

        while current_cell.previous and current_cell.content != key_origin:
            if current_cell.content >= "A" and current_cell.content <= "Z":
                reqs.add(current_cell.content.lower())

            distance += 1
            current_cell = current_cell.previous

        if distance:
            all_keys[key_origin].other_keys[key_dest] = (reqs, distance)
    
    clear(cells)

print(shortest_path(entrances, all_keys, entrances, {}))

# Recur
# If any keys we dont have
#   For each key we dont have
#       Recur passing held keys + new key
#       Add distance to key + return distance
#       Keep minimum total (ignore path)
# Else no more keys to get (base case)
#   Return zero (distance is zero cause no keys to go to!)