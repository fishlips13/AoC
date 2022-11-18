adjacents = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def knot_hash(input_str):
    lengths_ord = [ord(i) for i in input_str] + [17, 31, 73, 47, 23]

    circle = [i for i in range(256)]
    current, skip = 0, 0

    for _ in range(64):
        for length in lengths_ord:

            i_end = current + length
            if i_end < len(circle):
                start = circle[:current]
                middle = list(reversed(circle[current:i_end]))
                end = circle[i_end:]
            else:
                i_end %= len(circle)
                middle = circle[i_end:current]
                segment = list(reversed(circle[current:] + circle[:i_end]))
                seg_start_len = len(circle) - current
                start = segment[seg_start_len:]
                end = segment[:seg_start_len]

            circle = start + middle + end
            current = (current + length + skip) % len(circle)
            skip += 1

    xors = [0] * 16
    for i, value in enumerate(circle):
        xors[i//16] ^= value

    hash_str = ""
    for xor in xors:
        hex_str = hex(xor)[2:]
        if len(hex_str) == 1:
            hex_str = "0" + hex_str
        hash_str += hex_str
    
    return hash_str
    
with open("input\\14.txt") as f:
    data = f.read()

used = set()

for i_row in range(128):
    row_key_str = f"{data}-{i_row}"
    row_hash = knot_hash(row_key_str)

    row_str = ""
    row_hash_iter = iter(row_hash)
    for char1, char2 in zip(row_hash_iter, row_hash_iter):

        bin_str = bin(int(char1 + char2, 16))[2:]
        row_str += "0" * (8 - len(bin_str)) + bin_str

    for j_col, bit in enumerate(row_str):
        if bit == "1":
            used.add((i_row, j_col))

used_count = len(used)
region_count = 0

while used:
    frontier = [used.pop()]
    while frontier:
        cell = frontier.pop()

        for adj in adjacents:
            neigh = (cell[0] + adj[0], cell[1] + adj[1])

            if neigh in used:
                frontier.append(neigh)
                used.remove(neigh)

    region_count += 1

print(f"Used Count: {used_count}")
print(f"Region Count: {region_count}")