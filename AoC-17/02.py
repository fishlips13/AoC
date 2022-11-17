from itertools import permutations

with open("input\\02.txt") as f:
    data = [[int(j) for j in i.split()] for i in f.read().split("\n")]

checksum = sum([max(i) - min(i) for i in data])

divisible_result = 0
for line in data:
    for val1, val2 in permutations(line, 2):
        val_min = min(val1, val2)
        val_max = max(val1, val2)

        if val_max % val_min == 0:
            divisible_result += val_max // val_min
            break

print(f"Checksum: {checksum}")
print(f"Divisible Result: {divisible_result}")