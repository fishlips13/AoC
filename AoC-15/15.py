from itertools import permutations
from math import prod

with open("input/15.txt") as f:
    data = [j.split(", ") for j in [i.replace(":", ",") for i in f.read().split("\n")]]

ingredients = []
for item in data:

    new_ingredient = [item[0]]
    for _property in item[1:]:
        new_ingredient.append(int(_property.split(" ")[1]))

    ingredients.append(new_ingredient)

score_max = 0
cal500_score_max = 0
for amounts in permutations(range(0, 101), len(ingredients)):

    if sum(amounts) != 100:
        continue

    property_totals = [0, 0, 0, 0, 0]
    for ingredient, amount in zip(ingredients, amounts):
        property_totals[0] += ingredient[1] * amount
        property_totals[1] += ingredient[2] * amount
        property_totals[2] += ingredient[3] * amount
        property_totals[3] += ingredient[4] * amount
        property_totals[4] += ingredient[5] * amount

    if any(i <= 0 for i in property_totals):
        continue
    
    score = prod(property_totals[:-1])
    score_max = max(score_max, score)
    if property_totals[4] == 500:
        cal500_score_max = max(cal500_score_max, score)

print(f"Highest Score: {score_max}")
print(f"500 Calorie Highest Score: {cal500_score_max}")
