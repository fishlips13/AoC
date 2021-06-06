from copy import deepcopy

def find_memory_addresses(mask):
    addresses = []

    for i, bit in enumerate(mask):
        if bit == "X":
            next_mask = deepcopy(mask)
            next_mask[i] = "0"
            addresses.extend(find_memory_addresses(next_mask))
            next_mask[i] = "1"
            addresses.extend(find_memory_addresses(next_mask))
            return addresses

    return [deepcopy(mask)]

with open("input/14.txt") as f:
    data = [[j if not j.startswith("mem[") else j[4:-1] for j in i.split(" = ")] for i in f.read().split("\n")]

mask = []
wrong_memory = {}
right_memory = {}

for cmd, value in data:

    if cmd == "mask":
        mask = [i for i in value]
        continue

    # Wrong memory
    value = int(value)

    if value not in wrong_memory:
        wrong_memory[cmd] = value

    for bit, op in enumerate(reversed(mask)):
        if op == "0":
            wrong_memory[cmd] &= ~(1 << bit)
        elif op == "1":
            wrong_memory[cmd] |= (1 << bit)

    # Right memory
    address_mask = deepcopy(mask)
    bin_str = [i for i in bin(int(cmd))[2:].rjust(len(address_mask), "0")]

    for i in range(len(address_mask)):
        if address_mask[i] == "0":
            address_mask[i] = bin_str[i]
        elif address_mask[i] == "1":
            address_mask[i] = "1"

    addresses = find_memory_addresses(address_mask)
    for address in addresses:
        adrs_int = int("".join(address), base=2)
        right_memory[adrs_int] = value

print(f"Wrong Sum of Memory: {sum(wrong_memory.values())}")
print(f"Right Sum of Memory: {sum(right_memory.values())}")