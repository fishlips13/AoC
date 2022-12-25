from math import lcm
from heapq import heappush, heappop
from copy import deepcopy

blizzard_lookup = {">" : (1,0), "<" : (-1,0), "v" : (0,1), "^" : (0,-1)}
moves = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def coords_sub(coord1, coord2):
    return (coord1[0] - coord2[0], coord1[1] - coord2[1])

def coord_mag(coord):
    return abs(coord[0]) + abs(coord[1])

def build_blizzs_states(grid_data):
    bounds, blizzards, size = grid_data

    x_bounds = {i : [] for i in range(size[0])}
    y_bounds = {i : [] for i in range(size[1])}
    for bound in bounds:
        x_bounds[bound[0]].append(bound)
        y_bounds[bound[1]].append(bound)

    blizz_bounds = {}
    for x_bound1, x_bound2 in filter(lambda x: len(x) == 2, x_bounds.values()):
        blizz_bounds[x_bound1] = x_bound2
        blizz_bounds[x_bound2] = x_bound1
    
    for y_bound1, y_bound2 in filter(lambda x: len(x) == 2, y_bounds.values()):
        blizz_bounds[y_bound1] = y_bound2
        blizz_bounds[y_bound2] = y_bound1

    valley_x, valley_y  = size[0] - 2, size[1] - 2
    state_count = lcm(valley_x, valley_y)

    blizzs_states = {}
    for i in range(state_count):

        blizzs_state = set()
        for blizz in blizzards:
            blizz_next = coords_add(blizz[0], blizz[1])

            if blizz_next in blizz_bounds:
                blizz_next = coords_add(blizz_bounds[blizz_next], blizz[1])
            
            blizz[0] = blizz_next
            blizzs_state.add(blizz_next)
        
        blizzs_states[i] = blizzs_state

    return blizzs_states

def valley_travel_time(walls, size, blizzs_states, start, end, start_time):
    valley_x, valley_y  = size[0] - 2, size[1] - 2
    state_count = lcm(valley_x, valley_y)

    frontier = []
    heappush(frontier, (0, (start, start_time)))
    visited = set()

    while frontier:
        _, valley_state = heappop(frontier)
        pos_curr, time = valley_state
        i_state_curr = time % state_count

        if (pos_curr, i_state_curr) in visited:
            continue
        visited.add((pos_curr, i_state_curr))

        time += 1
        i_state_next = time % state_count

        for move in moves:
            pos_next = coords_add(pos_curr, move)

            if pos_next == end:
                return time
            elif pos_next in walls or pos_next in blizzs_states[i_state_next]:
                continue
            
            heur = heuristic(pos_next, end, time)
            heappush(frontier, (heur, (pos_next, time)))

def time_to_exit(grid_data):
    blizzs_states = build_blizzs_states(grid_data)

    walls, _, size = grid_data
    start = (1, 0)
    end = (size[0] - 2, size[1] - 1)

    walls.add((start[0], start[1] - 1))
    walls.add((end[0], end[1] + 1))

    # Turns out, the 'exit' isn't the exit on the diagram, it's the tile below it
    # I'd argue it's ambiguous but, eh, I can see it both ways
    #     + 1 to move to it as the path is always clear
    return valley_travel_time(walls, size, blizzs_states, start, end, 0) + 1

def time_return_and_exit(grid_data):
    blizzs_states = build_blizzs_states(grid_data)

    walls, _, size = grid_data
    start = (1, 0)
    end = (size[0] - 2, size[1] - 1)

    walls.add((start[0], start[1] - 1))
    walls.add((end[0], end[1] + 1))

    # Same as above, 'exit' is 1 off
    #   + 2 to move to it and back for the next phase
    #   Don't add on the way back, the 'entry' is correct on the diagram
    #   + 1 on the way back again
    time = valley_travel_time(walls, size, blizzs_states, start, end, 0) + 2
    time = valley_travel_time(walls, size, blizzs_states, end, start, time)
    time = valley_travel_time(walls, size, blizzs_states, start, end, time) + 1

    return time

def heuristic(curr, dest, time):
    return coord_mag(coords_sub(curr, dest)) + 1000 * time

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    walls = set()
    blizzards = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x,y))
            elif char in blizzard_lookup:
                blizzards.append([(x,y), blizzard_lookup[char]])

    return walls, blizzards, (len(data[0]), len(data))

def tests():
    test1_exp = 18
    test2_exp = 54

    data = parse_data("day-24\\test_input.txt")
    test1_res = time_to_exit(deepcopy(data))
    test2_res = time_return_and_exit(deepcopy(data))

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-24\\input.txt")
    answer1 = time_to_exit(deepcopy(data))
    answer2 = time_return_and_exit(deepcopy(data))

    print(f"Part 1 -> Time to Cross Once: {answer1}")
    print(f"Part 2 -> Time to Cross Thrice: {answer2}")

tests()
puzzle()