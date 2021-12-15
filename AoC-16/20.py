with open("input\\20.txt") as f:
    ip_ranges = [tuple([j for j in map(int, i.split("-"))]) for i in f.read().split("\n")]

ip_total = 4294967295 + 1
lowest = 99999999999999
found_ranges = []

for candi in [i[1] + 1 for i in ip_ranges]:
    if all(candi < ip_range[0] or candi > ip_range[1] for ip_range in ip_ranges):
        lowest = min(lowest, candi)

while ip_ranges:
    new_range = ip_ranges.pop()

    for found_range in found_ranges:
        # new both inside
        if new_range[0] >= found_range[0] and new_range[1] <= found_range[1]:
            # make invalid
            new_range = None
            break
        # new left inside
        elif new_range[0] >= found_range[0] and new_range[0] <= found_range[1]:
            new_range = (found_range[1] + 1, new_range[1])
        # new right inside
        elif new_range[1] >= found_range[0] and new_range[1] <= found_range[1]:
            new_range = (new_range[0], found_range[0] - 1)
        # new enveloping, split
        elif new_range[0] <= found_range[0] and new_range[1] >= found_range[1]:
            ip_ranges.append((found_range[1] + 1, new_range[1]))
            new_range = (new_range[0], found_range[0] - 1)
        # else, new outside, do nothing

    if new_range:
        found_ranges.append(new_range)

blocked_total = sum([i[1] - i[0] + 1 for i in found_ranges])

print(f"Lowest Open: {lowest}")
print(f"Total Open: {ip_total - blocked_total}")