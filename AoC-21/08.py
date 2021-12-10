from itertools import cycle

with open("input\\08.txt") as f:
    data = [[j.split(" ") for j in i.split(" | ")] for i in f.read().split("\n")]

unique_count = sum([1 for _, o in data for i in o if len(i) in [2, 3, 4, 7]])

output_total = 0
for patterns, output in data:

    found = {}
    for pattern in cycle(patterns):
        pattern = set([i for i in pattern])
        length = len(pattern)
        
        if length == 2:
            found[1] = pattern
        elif length == 4:
            found[4] = pattern
        elif length == 3:
            found[7] = pattern
        elif length == 7:
            found[8] = pattern
        elif length == 6 and 4 in found and len(found[4].intersection(pattern)) == 4:
            found[9] = pattern
        elif length == 6 and 9 in found and 1 in found and pattern != found[9] and len(found[1].intersection(pattern)) == 2:
            found[0] = pattern
        elif length == 6 and 9 in found and 0 in found and pattern != found[9] and pattern != found[0]:
            found[6] = pattern
        elif length == 5 and 1 in found and len(found[1].intersection(pattern)) == 2:
            found[3] = pattern
        elif length == 5 and 4 in found and len(found[4].intersection(pattern)) == 2:
            found[2] = pattern
        elif length == 5 and 2 in found and 3 in found and pattern != found[2] and pattern != found[3]:
            found[5] = pattern

        if len(found) == 10:
            break

    lookup = {}
    for key, pattern in found.items():
        pattern = list(pattern)
        pattern.sort()
        lookup["".join(pattern)] = key

    for exp, value in enumerate(output[::-1]):
        value = [i for i in value]
        value.sort()
        output_total += lookup["".join(value)] * pow(10, exp)

print(f"Unique Segment Count: {unique_count}")
print(f"Output Total: {output_total}")


# 1
# 4
# 7
# 8
# 2 3 5
# 0 6 9

# 0  if not '9' and 2 of '1' inside
# 1  2 segs
# 2  if 2 of '4' inside
# 3  if 2 of '1' inside
# 4  4 segs
# 5  if not '2' or '3'
# 6  if not '9' or '0'
# 7  3 segs
# 8  7 segs
# 9  if 4 of '4' inside