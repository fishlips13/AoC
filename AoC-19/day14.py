from math import ceil
from copy import deepcopy

f = open("data.txt")
data = [i.split() for i in f.read().split("\n")]
f.close()

for i in data:
    i[:] = [j.replace(",", "") for j in i]

recipes = {}

for recipe in data:

    ing_data = iter(recipe[::-1])
    result = next(ing_data) 
    recipes[result] = [int(next(ing_data))]
    next(ing_data) # Skip '=>'

    for value in ing_data:
        recipes[result].append((value, int(next(ing_data))))

surp = {}
surp_prev = {}
ore = 1000000000000

fuel_made = 0
fuel_attempt = ore

while True:
    reqs = {"FUEL" : fuel_attempt}
    ore_attempt = 0

    while len(reqs) > 0:
        result = reqs.popitem()
        name = result[0]
        need = result[1]

        if name == "ORE":
            ore_attempt += need
            continue

        recipe = iter(recipes[name])
        given = next(recipe)

        if name in surp:
            surp_use = min(need, surp[name])
            need -= surp_use
            surp[name] -= surp_use
            if surp[name] == 0:
                del(surp[name])

        count = ceil(need / given)
        n_mod_g = need % given
        surp_new = 0
        if n_mod_g:
            surp_new = given - n_mod_g
            if name in surp:
                surp[name] += surp_new
            else:
                surp[name] = surp_new

        for ing in recipe:
            if ing[0] in reqs:
                reqs[ing[0]] += ing[1] * count
            else:
                reqs[ing[0]] = ing[1] * count

    if ore_attempt < ore // 2 or fuel_attempt == 1 and ore_attempt <= ore:
        ore -= ore_attempt
        fuel_made += fuel_attempt
        surp_prev = deepcopy(surp)
    elif fuel_attempt == 1 and ore_attempt > ore:
        break
    else:
        surp = deepcopy(surp_prev)
        fuel_attempt //= 2
        fuel_attempt = fuel_attempt or 1

print(fuel_made)
