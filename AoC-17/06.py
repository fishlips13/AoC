with open("input\\06.txt") as f:
    data = [int(i) for i in f.read().split()]

cache = {}

cycles = 0
while True:
    data_str = ",".join([str(i) for i in data])
    if data_str in cache:
        break
    cache[data_str] = cycles

    val_max = -1
    i_max = -1
    for i, value in enumerate(data):
        if value > val_max:
            val_max = value
            i_max = i

    data[i_max] = 0
    i = i_max
    for j in range(val_max):
        i = (i + 1) % len(data)
        data[i] += 1

    cycles += 1

loop_size = cycles - cache[data_str]

print(f"Redistribution Cycles: {cycles}")
print(f"Loop Size: {loop_size}")