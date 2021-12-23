import re

def axis_full_overlap(a1, a2, b1, b2):
    return a1 <= b1 <= a2 and a1 <= b2 <= a2

def axis_partial_overlap(a1, a2, b1, b2):
    return a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b2

def count_cubes(volumes):
    return sum([(x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) for x1, x2, y1, y2, z1, z2 in volumes])

with open("input\\22.txt") as f:
    data = f.read().split("\n")

regions = [(i[:3].strip(), tuple(map(int, re.findall(r"-?\d+", i)))) for i in data]

volumes = []
for toggle, region_bounds in regions:
    if len(volumes) == 0:
        volumes.append(region_bounds)
        continue

    new_x1, new_x2, new_y1, new_y2, new_z1, new_z2 = region_bounds
    volumes_next = []
    
    while volumes:
        old_bounds = volumes.pop()
        old_x1, old_x2, old_y1, old_y2, old_z1, old_z2 = old_bounds

        # Old entirely within new (discard old)
        if axis_full_overlap(new_x1, new_x2, old_x1, old_x2) and \
           axis_full_overlap(new_y1, new_y2, old_y1, old_y2) and \
           axis_full_overlap(new_z1, new_z2, old_z1, old_z2):
            continue

        # No overlap (don't change old)
        if not (axis_partial_overlap(old_x1, old_x2, new_x1, new_x2) and \
                axis_partial_overlap(old_y1, old_y2, new_y1, new_y2) and \
                axis_partial_overlap(old_z1, old_z2, new_z1, new_z2)):
            volumes_next.append(old_bounds)
            continue

        # Left cut
        if old_x1 < new_x1:
            volumes_next.append((old_x1, new_x1 - 1, old_y1, old_y2, old_z1, old_z2))
            old_x1 = new_x1

        # Right cut
        if old_x2 > new_x2:
            volumes_next.append((new_x2 + 1, old_x2, old_y1, old_y2, old_z1, old_z2))
            old_x2 = new_x2
            
        # Bottom cut
        if old_y1 < new_y1:
            volumes_next.append((old_x1, old_x2, old_y1, new_y1 - 1, old_z1, old_z2))
            old_y1 = new_y1
            
        # Top cut
        if old_y2 > new_y2:
            volumes_next.append((old_x1, old_x2, new_y2 + 1, old_y2, old_z1, old_z2))
            old_y2 = new_y2

        # Backward cut
        if old_z1 < new_z1:
            volumes_next.append((old_x1, old_x2, old_y1, old_y2, old_z1, new_z1 - 1))
            old_z1 = new_z1

        # Forward cut
        if old_z2 > new_z2:
            volumes_next.append((old_x1, old_x2, old_y1, old_y2, new_z2 + 1, old_z2))
            old_z2 = new_z2

    if toggle == "on":
        volumes_next.append(region_bounds)

    volumes = volumes_next

cubes_total = count_cubes(volumes)

print(f"Total Cubes Active: {cubes_total}")