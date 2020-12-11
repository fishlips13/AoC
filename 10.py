def num_configs(adapters, final, cache = {}):

    def num_sub_configs(new_final):
        if new_final not in cache:
            cache[new_final] = num_configs(adapters, new_final)
        return cache[new_final]

    if final == 0:
        return 1
    elif final < 0:
        return 0
    
    total = 0

    if adapters[final] - adapters[final-1] <= 3:
        total += num_sub_configs(final-1)
    if adapters[final] - adapters[final-2] <= 3:
        total += num_sub_configs(final-2)
    if adapters[final] - adapters[final-3] <= 3:
        total += num_sub_configs(final-3)

    return total

with open("input/10.txt") as f:
    adapters = [int(i) for i in f.read().split("\n")]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

diff_1_count = 0
diff_3_count = 0

for first, second in zip(adapters, adapters[1:]):
    if second - first == 1:
        diff_1_count += 1
    else:
        diff_3_count += 1

print(f"First by Third: {diff_1_count * diff_3_count}")
print(f"Total Configurations: {num_configs(adapters, len(adapters)-1)}")