adjacents = [(1,0), (0,1), (-1,0), (0,-1)]

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def steps_to_summit(map_data):
    grid, start, end = map_data

    frontier = [start]
    visited = set()

    steps = 1
    while frontier:
        frontier_next = set()
        while frontier:
            curr = frontier.pop()
            visited.add(curr)

            for adj in adjacents:
                neigh = coords_add(curr, adj)

                if neigh in frontier_next or neigh in visited or neigh not in grid or grid[neigh] > grid[curr] + 1:
                    continue
                elif neigh == end:
                    return steps

                frontier_next.add(neigh)
        
        frontier = frontier_next
        steps += 1
    
    return -1

def shortest_low_route(map_data):
    steps_min = 99999999999

    for coord, height in map_data[0].items():
        if height != 1:
            continue

        steps = steps_to_summit((map_data[0], coord, map_data[2]))
        if steps != -1:
            steps_min = min(steps_min, steps)
    
    return steps_min

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    grid = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "S":
                height = 1
                start = (x,y)
            elif char == "E":
                height = 26
                end = (x,y)
            else:
                height = ord(char) - 96
            
            grid[(x,y)] = height

    return (grid, start, end)

def tests():
    test1_exp = 31
    test2_exp = 29

    data = parse_data("day-12\\test_input.txt")
    test1_res = steps_to_summit(data)
    test2_res = shortest_low_route(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-12\\input.txt")
    answer1 = steps_to_summit(data)
    answer2 = shortest_low_route(data)

    print(f"Part 1 -> Steps to Summit: {answer1}")
    print(f"Part 2 -> Shortest Low Route: {answer2}")

tests()
puzzle()