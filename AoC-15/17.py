from itertools import combinations

with open("input/17.txt") as f:
    containers = [int(i) for i in f.read().split("\n")]

total_eggnog = 150
total_valid = 0

min_count = len(containers)
min_combs = 0

for count in range(len(containers)):
    for comb in combinations(containers, count):
        
        if sum(comb) != total_eggnog:
            continue
        
        total_valid += 1

        if count < min_count:
            min_count = count
            min_combs = 1
        elif count == min_count:
            min_combs += 1

print(f"Valid Combinations: {total_valid}")
print(f"Valid Minimal Combinations: {min_combs}")