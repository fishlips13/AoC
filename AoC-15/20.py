from functools import reduce

# Thanks Stack Overflow
def find_factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

with open("input/20.txt") as f:
    data = int(f.read())

house = 1
house_pt1, house_pt2 = None, None
visit_count = {}

while not house_pt1 or not house_pt2:

    factors = find_factors(house)
    elves = []

    for elf in factors:
        if elf not in visit_count:
            visit_count[elf] = 0
        if visit_count[elf] < 50:
            elves.append(elf)
            visit_count[elf] += 1

    presents1 = sum(factors) * 10
    presents2 = sum(elves) * 11

    if not house_pt1 and presents1 >= data:
        house_pt1 = house
    if not house_pt2 and presents2 >= data:
        house_pt2 = house

    house += 1

print(f"Earliest House pt1: {house_pt1}")
print(f"Earliest House pt2: {house_pt2}")