with open("input\\11.txt") as f:
    data = f.read().split("\n")

coords_adj = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def step(octos):
    octos_ping = list(octos.keys())
    octos_cache = set()

    while octos_ping:
        for octo in octos_ping:
            octos[octo] += 1

        octos_ready = {octo for octo in octos_ping if octos[octo] > 9}
        octos_cache.update(octos_ready)

        octos_ping = []
        for octo in octos_ready:
            octos[octo] = 0
            octos_adj = [(octo[0] + adj[0], octo[1] + adj[1]) for adj in coords_adj]
            for octo_adj in octos_adj:
                if octo_adj not in octos or octo_adj in octos_cache:
                    continue
                octos_ping.append(octo_adj)
            
    return len(octos_cache)

octos = {}
for y, line in enumerate(data):
    for x, value in enumerate(line):
        octos[(x, y)] = int(value)

flash_total_100 = 0
for _ in range(100):
    flash_total_100 += step(octos)

total_steps = 100
while True:
    total_steps += 1
    if step(octos) == len(octos):
        break

print(f"Total flashes in 100 steps: {flash_total_100}")
print(f"Total steps to sync: {total_steps}")