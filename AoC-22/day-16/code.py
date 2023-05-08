from itertools import permutations, combinations
from copy import deepcopy

def pressure_release_human(valve_data):
    valves, valve_dists = valve_data
    frontier = [("AA", 0, 0)]
    states = {}
    press_max = 0

    while frontier:
        frontier_new = []

        while frontier:
            open_valves_str, press_old, time_old = frontier.pop()
            open_valves = open_valves_str.split("-")
            
            for valve_next in valves.keys() - set(open_valves):
                steps = valve_dists[(open_valves[-1], valve_next)] + 1
                time_new = time_old + steps

                if time_new > 30:
                    continue

                press_tick = sum([valves[i][0] for i in open_valves if i in valves])
                press_new = press_tick * steps + press_old

                open_valves.append(valve_next)
                state_new = "-".join(open_valves)
                open_valves.pop()

                frontier_new.append((state_new, press_new, time_new))
                states[state_new] = (press_new, time_new)
        
        frontier = frontier_new
    
    for open_valves_str, state_data in states.items():
        open_valves = open_valves_str.split("-")
        press_old, time_old = state_data

        press_tick = sum([valves[i][0] for i in open_valves if i in valves])
        press_new = press_old + (30 - time_old) * press_tick
        press_max = max(press_max, press_new)

    return press_max

def pressure_release_elephant(valve_data):
    valves, valve_paths = valve_data
    pressure_max = 0

    for actor1_len in (range(7, len(valves) // 2 + 1)):
        print(actor1_len)
        for a1_valves in combinations(valves, actor1_len):
            a2_valves = valves.keys() - set(a1_valves)

            a1_max, a2_max = 0, 0
            for a1_route in permutations(a1_valves):
                a1_pressure = valve_route_pressure(a1_route, valves, valve_paths, 26)
                a1_max = max(a1_pressure, a1_max)

            for a2_route in permutations(a2_valves):
                a2_pressure = valve_route_pressure(a2_route, valves, valve_paths, 26)
                a2_max = max(a2_pressure, a2_max)
            
            pressure_max = max(a1_max + a2_max, pressure_max)

    return pressure_max
    
def valve_route_pressure(valve_route, valves, valve_dists, time_max):
    valve_route = list(valve_route)
    valve_route.insert(0, "AA")

    pressure, tick, time = 0, 0, 0
    for pair in zip(valve_route, valve_route[1:]):
        path_len = valve_dists[pair] + 1
        
        if time + path_len >= time_max:
            break

        pressure += tick * path_len
        tick += valves[pair[1]][0]
        time += path_len

    pressure += tick * (time_max - time)
    return pressure

def ughhhhhhhhh(valve_data):
    return
    valves, valve_paths = valve_data
    frontier = [("", "AA-##-AA-##", 0, 0)]
    press_max = 0
    cache_large = set()

    while frontier:
        open_valves_str, actors_str, pressure, time = frontier.pop()
        open_valves = open_valves_str.split("-") if open_valves_str != "" else []
        actors = actors_str.split("-")
        hum_curr, hum_dest = actors[:-2]
        ele_curr, ele_dest = actors[-2:]

        cache_str = f"{open_valves_str};{actors_str};{str(pressure)};{str(time)}"
        if cache_str in cache_large:
            continue
        cache_large.add(cache_str)
        
        if hum_dest == "##" or ele_dest == "##":
            closed_valves = list(valves.keys() - set(open_valves))
            closed_valves.append("$$")
            cache_small = set()            

            for valve1, valve2 in permutations(closed_valves, 2):
                
                open_valves_new = []
                
                if hum_dest == "##":
                    hum_dest_new = valve1
                    if valve1 != "$$":
                        open_valves_new.append(valve1)
                else:
                    hum_dest_new = hum_dest

                if ele_dest == "##":
                    ele_dest_new = valve2
                    if valve2 != "$$":
                        open_valves_new.append(valve2)
                else:
                    ele_dest_new = ele_dest

                open_valves.extend(open_valves_new)
                open_valves_str_new = "-".join(open_valves)
                open_valves = open_valves[:-len(open_valves_new)]

                actors_str_new = "-".join([hum_curr, hum_dest_new, ele_curr, ele_dest_new])

                cache_str = f"{open_valves_str_new};{actors_str_new}"
                if cache_str in cache_small:
                    continue
                cache_small.add(cache_str)

                frontier.append((open_valves_str_new, actors_str_new, pressure, time))

            continue

        if hum_curr == hum_dest:
            hum_dest = "##"
        elif hum_dest != "$$":
            dest_path = valve_paths[(hum_curr, hum_dest)]
            i_path_curr = dest_path.index(hum_curr) + 1
            hum_curr = dest_path[i_path_curr]

        if ele_curr == ele_dest:
            ele_dest = "##"
        elif ele_dest != "$$":
            dest_path = valve_paths[(ele_curr, ele_dest)]
            i_path_curr = dest_path.index(ele_curr) + 1
            ele_curr = dest_path[i_path_curr]

        if hum_dest == "$$" and ele_dest == "$$":
            time_scale = 26 - time
        else:
            time_scale = 1

        pressure += sum([valves[i][0] for i in open_valves if i in valves]) * time_scale
        time += time_scale

        if time == 26:
            press_max = max(pressure, press_max)
            continue

        actors_str = "-".join([hum_curr, hum_dest, ele_curr, ele_dest])

        frontier.append((open_valves_str, actors_str, pressure, time))

    return press_max

def parse_data(path):
    with open(path) as f:
        data = [i.split(" ") for i in f.read().replace(",", "").split("\n")]

    valves = {entry[1] : (int(entry[4][5:-1]), entry[9:]) for entry in data}
    valve_dists = {}
    
    for orig, dest in permutations(valves, 2):
        valve_dists[(orig, dest)] = distance_to_valve(orig, dest, valves)

    valves_useful = {i : j for i, j in valves.items() if j[0] > 0}

    return valves_useful, valve_dists

def distance_to_valve(orig, dest, valves):
    frontier = [orig]
    visited = set()

    steps = 1
    while True:
        frontier_new = []
        while frontier:
            curr = frontier.pop()

            for neigh in valves[curr][1]:
                if neigh == dest:
                    return steps
                elif neigh in visited:
                    continue

                frontier_new.append(neigh)
                visited.add(neigh)

        frontier = frontier_new
        steps += 1

def tests():
    test1_exp = 1651
    test2_exp = 1707

    data = parse_data("day-16\\test_input.txt")
    test1_res = pressure_release_human(data)
    test2_res = pressure_release_elephant(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-16\\input.txt")
    answer1 = pressure_release_human(data)
    answer2 = pressure_release_elephant(data)

    print(f"Part 1 -> : {answer1}")
    print(f"Part 2 -> : {answer2}")

#tests()
puzzle()