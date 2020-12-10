from itertools import combinations

with open("input/09.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

combos = {}

preamble_length = 25
for comb in combinations(data[:preamble_length], 2):
    comb_sum = sum(comb)
    if comb_sum not in combos:
        combos[comb_sum] = 0
    combos[comb_sum] += 1

weakness_value = 0
for i_next in range(preamble_length, len(data)):

    if data[i_next] not in combos:
        weakness_value = data[i_next]

    i_first = i_next - preamble_length

    for i in range(i_first + 1, i_next):
        combo_old = data[i_first] + data[i]
        combo_new = data[i_next] + data[i]

        if combo_new not in combos:
            combos[combo_new] = 0

        combos[combo_new] += 1
        combos[combo_old] -= 1

        if combos[combo_old] == 0:
            del combos[combo_old]

print(f"First Weakness Value: {weakness_value}")

current_total = 0
i_start = 0
for i in range(len(data)):
    current_total += data[i]

    while current_total > weakness_value:
        current_total -= data[i_start]
        i_start += 1

    if current_total == weakness_value:
        data_contig = data[i_start:i]
        print(f"Encryption Weakness: {min(data_contig) + max(data_contig)}")
        break