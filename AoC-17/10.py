def knot(circle, lengths, current = 0, skip = 0):
    for length in lengths:
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

    return circle, current, skip

with open("input\\10.txt") as f:
    data = f.read()

lengths_int = [int(i) for i in data.split(",")]
lengths_ord = [ord(i) for i in data] + [17, 31, 73, 47, 23]

circle_single = [i for i in range(256)]
circle_single, current, skip = knot(circle_single, lengths_int)

circle_many = [i for i in range(256)]
current, skip = 0, 0
for _ in range(64):
    circle_many, current, skip = knot(circle_many, lengths_ord, current, skip)

xors = [0] * 16
for i, value in enumerate(circle_many):
    xors[i//16] ^= value

hash_str = ""
for xor in xors:
    hex_str = hex(xor)[2:]
    if len(hex_str) == 1:
        hex_str = "0" + hex_str
    hash_str += hex_str

single_check = circle_single[0] * circle_single[1]

print(f"Single Check: {single_check}")
print(f"Single Check: {hash_str}")