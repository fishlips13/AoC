from itertools import combinations
from copy import deepcopy
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

f = open("data.txt")
moons = f.read().split("\n")
f.close()

moons[:] = ["".join(filter(lambda x: x.isdigit() or x == "-" or x ==",", i)) for i in moons]
moons[:] = [i.split(",") for i in moons]
for i in moons:
    i[:] = [[int(j) for j in i], [0] * 3]

moons_init = deepcopy(moons)
periods = [0] * 3

cycle_count = 1000000
percent = 0
for cycle in range(cycle_count):

    if cycle % (cycle_count // 10) == 0:
        percent += 10
        print(percent, "%")

    # For each combination of moons
    for pair in combinations(moons, 2):
        moon1 = pair[0]
        moon2 = pair[1]
        
        # Apply gravity to velocity
        for i in range(3):
            if moon1[0][i] < moon2[0][i]:
                moon1[1][i] +=1
                moon2[1][i] -=1
            elif moon1[0][i] > moon2[0][i]:
                moon1[1][i] -=1
                moon2[1][i] +=1

    # Apply velocity to position
    for moon in moons:
        for i in range(3):
            moon[0][i] += moon[1][i]
    
    for i in range(3):
        if periods[i] == 0:

            valid = True
            for j in range(4):
                if moons[j][0][i] != moons_init[j][0][i] or moons[j][1][i] != moons_init[j][1][i]:
                    valid = False
                    break
            
            if valid:
                periods[i] = cycle + 1

    # Find total energy
    total = 0
    for moon in moons:
        total +=sum([abs(i) for i in moon[0]]) * sum([abs(i) for i in moon[1]])

print(total)
print(periods)

if all(i > 0 for i in periods):
    answer = lcm(lcm(periods[0], periods[1]), periods[2])
try:
    print(answer)
except:
    print("More plz")