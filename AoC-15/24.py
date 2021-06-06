from itertools import combinations
from math import prod

def smallest_sub_config(packages, sub_config_weight):
    for comb_len in range(1, len(packages) + 1):
        for comb in combinations(packages, comb_len):
            if sum(comb) == sub_config_weight:
                config = set(comb)
                remaining_packages = packages - config
                if len(remaining_packages) == 0 or len(smallest_sub_config(remaining_packages, sub_config_weight)) > 0:
                    return config
    return set()

with open("input/24.txt") as f:
    packages = {int(i) for i in f.read().split("\n")}

stack_weight = sum(packages)

lowest_qe_3 = prod(smallest_sub_config(packages, stack_weight // 3))
lowest_qe_4 = prod(smallest_sub_config(packages, stack_weight // 4))

print(f"Lowest QE (3): {lowest_qe_3}")
print(f"Lowest QE (4): {lowest_qe_4}")