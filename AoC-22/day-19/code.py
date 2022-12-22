import re
from math import ceil

def blueprint_stats(blueprints, time_max):
    quality_level_total = 0
    geode_max_multiple = 1

    for i, blueprint in enumerate(blueprints):
        ore_cost, clay_cost, obs_cost, geo_cost = blueprint

        frontier = [((1, 0, 0, 0), (0, 0, 0, 0), 0)]
        time_best = [[(0, 0)] * time_max] * len(blueprints)
        cache = set()
        geodes_max = 0
        ore_bot_max = max(ore_cost, clay_cost, obs_cost[0], geo_cost[0])
        clay_bot_max = obs_cost[1]
        obs_bot_max = geo_cost[1]

        while frontier:
            bot_counts, res_counts, time = frontier.pop()

            state_str = ",".join(map(str, bot_counts)) + ";" + ",".join(map(str, res_counts))
            if state_str in cache:
                continue
            cache.add(state_str)

            ore_bots, clay_bots, obs_bots, geo_bots = bot_counts
            ore, clay, obs, geo = res_counts

            # Ore Bot
            if ore_bots < ore_bot_max:
                ore_turns = ceil(max(0, ore_cost - ore) / ore_bots) + 1

                if time + ore_turns <= time_max - 3:
                    ore_bots_new = ore_bots + 1
                    ore_new  = ore + ore_bots * ore_turns - ore_cost
                    clay_new = clay + clay_bots * ore_turns
                    obs_new  = obs + obs_bots * ore_turns
                    geo_new  = geo + geo_bots * ore_turns

                    frontier.append(((ore_bots_new, clay_bots, obs_bots, geo_bots),
                                    (ore_new, clay_new, obs_new, geo_new),
                                    time + ore_turns))
                else:
                    time_remain = time_max - time
                    geodes_max = max(geodes_max, geo + geo_bots * time_remain)

            # Clay Bot

            if clay_bots < clay_bot_max:
                clay_turns = ceil(max(0, clay_cost - ore) / ore_bots) + 1

                if time + clay_turns <= time_max - 3:
                    clay_bots_new = clay_bots + 1
                    ore_new  = ore + ore_bots * clay_turns - clay_cost
                    clay_new = clay + clay_bots * clay_turns
                    obs_new  = obs + obs_bots * clay_turns
                    geo_new  = geo + geo_bots * clay_turns

                    frontier.append(((ore_bots, clay_bots_new, obs_bots, geo_bots),
                                    (ore_new, clay_new, obs_new, geo_new),
                                    time + clay_turns))
                else:
                    time_remain = time_max - time
                    geodes_max = max(geodes_max, geo + geo_bots * time_remain)

            # Obs Bot

            if clay_bots and obs_bots < obs_bot_max:
                obs_turns_ore  = ceil(max(0, obs_cost[0] - ore) / ore_bots) + 1
                obs_turns_clay = ceil(max(0, obs_cost[1] - clay) / clay_bots) + 1
                obs_turns = max(obs_turns_ore, obs_turns_clay)

                if time + obs_turns <= time_max - 3:
                    obs_bots_new = obs_bots + 1
                    ore_new  = ore + ore_bots * obs_turns - obs_cost[0]
                    clay_new = clay + clay_bots * obs_turns - obs_cost[1]
                    obs_new  = obs + obs_bots * obs_turns
                    geo_new  = geo + geo_bots * obs_turns

                    frontier.append(((ore_bots, clay_bots, obs_bots_new, geo_bots),
                                    (ore_new, clay_new, obs_new, geo_new),
                                    time + obs_turns))
                else:
                    time_remain = time_max - time
                    geodes_max = max(geodes_max, geo + geo_bots * time_remain)


            # Geo Bot

            if obs_bots:
                geo_turns_ore = ceil(max(0, geo_cost[0] - ore) / ore_bots) + 1
                geo_turns_obs = ceil(max(0, geo_cost[1] - obs) / obs_bots) + 1
                geo_turns = max(geo_turns_ore, geo_turns_obs)

                time_next = time + geo_turns
                if time + geo_turns <= time_max - 1:
                    geo_bots_new = geo_bots + 1
                    ore_new  = ore + ore_bots * geo_turns - geo_cost[0]
                    clay_new = clay + clay_bots * geo_turns
                    obs_new  = obs + obs_bots * geo_turns - geo_cost[1]
                    geo_new  = geo + geo_bots * geo_turns
                    
                    if time_best[i][time_next][0] > geo_bots and time_best[i][time_next][1] > geo:
                        continue
                    elif time_best[i][time_next][0] < geo_bots and time_best[i][time_next][1] < geo:
                        time_best[i][time_next] = (geo_bots, geo)

                    frontier.append(((ore_bots, clay_bots, obs_bots, geo_bots_new),
                                    (ore_new, clay_new, obs_new, geo_new),
                                    time_next))
                else:
                    time_remain = time_max - time
                    geodes_max = max(geodes_max, geo + geo_bots * time_remain)

        quality_level_total += (i + 1) * geodes_max
        geode_max_multiple *= geodes_max
    
    return quality_level_total, geode_max_multiple

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    blueprints = []

    for entry in data:
        values = list(map(int, re.findall(r"\d+", entry)))
        blueprints.append((values[1],
                           values[2],
                           (values[3], values[4]),
                           (values[5], values[6])))

    return blueprints

def tests():
    test1_exp = 33
    test2_exp = 3472

    data = parse_data("day-19\\test_input.txt")
    test1_res, _ = blueprint_stats(data, 24)
    _, test2_res = blueprint_stats(data[:3], 32)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-19\\input.txt")
    answer1, _ = blueprint_stats(data, 24)
    _, answer2 = blueprint_stats(data[:3], 32)

    print(f"Part 1 -> Quality Index Total: {answer1}")
    print(f"Part 2 -> Blueprint Multiple: {answer2}")

tests()
puzzle()