from math import ceil

with open("input/21.txt") as f:
    data = [i.split(": ") for i in f.read().split("\n")]

player_hp = 100

boss_hp = int(data[0][1])
boss_dmg = int(data[1][1])
boss_arm = int(data[2][1])

weapons = [("Dagger",      8, 4, 0),
           ("Shortsword", 10, 5, 0),
           ("Warhammer",  25, 6, 0),
           ("Longsword",  40, 7, 0),
           ("Greataxe",   74, 8, 0)]

armors = [("No armor",    0, 0, 0,),
          ("Leather",     13, 0, 1),
          ("Chainmail",   31, 0, 2),
          ("Splintmail",  53, 0, 3),
          ("Bandedmail",  75, 0, 4),
          ("Platemail",  102, 0, 5)]

dmg_rings = [("No dmg ring",  0, 0, 0),
             ("Damage +1",   25, 1, 0),
             ("Damage +2",   50, 2, 0),
             ("Damage +3",  100, 3, 0)]

arm_rings = [("No arm ring",  0, 0, 0),
             ("Defense +1",  20, 0, 1),
             ("Defense +2",  40, 0, 2),
             ("Defense +3",  80, 0, 3)]

equipment_sets = []
for weapon in weapons:
    for armor in armors:
        for dmg_ring in dmg_rings:
            for arm_ring in arm_rings:
                equipment_sets.append((weapon, armor, dmg_ring, arm_ring))

cheapest_winning_set = None
cheapest_cost = 9999999999
priciest_losing_set = None
priciest_cost = 0

for equipment_set in equipment_sets:
    cost       = sum(i[1] for i in equipment_set)
    player_dmg = sum(i[2] for i in equipment_set)
    player_arm = sum(i[3] for i in equipment_set)

    player_att = max(1, player_dmg - boss_arm)
    boss_att   = max(1, boss_dmg - player_arm)

    if cost < cheapest_cost and ceil(boss_hp / player_att) <= ceil(player_hp / boss_att):
        cheapest_winning_set = equipment_set
        cheapest_cost = cost
    
    if cost > priciest_cost and ceil(boss_hp / player_att) > ceil(player_hp / boss_att):
        priciest_losing_set = equipment_set
        priciest_cost = cost

print(f"Cheapest Winning Set: {', '.join([i[0] for i in cheapest_winning_set])}; Cost: {cheapest_cost}")
print(f"Priciest Losing Set: {', '.join([i[0] for i in priciest_losing_set])}; Cost: {priciest_cost}")