import re

def row_impossibles(sensors, row):
    overlaps = []
    row_beacons_x = set()

    for origin, beacon, manh_dist in sensors:
        row_dist = abs(origin[1] - row)

        if manh_dist > row_dist:
            overlap_size = manh_dist - row_dist
            overlaps.append((origin[0] - overlap_size, origin[0] + overlap_size))

        if beacon[1] == row:
             row_beacons_x.add(beacon[0])

    overlaps.sort()
    
    imp_count = 0
    right_max = -999999999999
    for left, right in zip(overlaps, overlaps[1:]):
        seg_end = min(left[1], right[0] - 1)
        imp_count += seg_end - left[0] + 1
        imp_count -= sum([1 for x in row_beacons_x if x >= left[0] and x <= seg_end])
        right_max = max(right_max, right[1])
    
    if overlaps:
        imp_count += right_max - overlaps[-1][0]  + 1

    return imp_count

def tuning_frequency(sensors, axis_max):
    for row in range(axis_max + 1):
        overlaps = []
        for origin, _, manh_dist in sensors:
            row_dist = abs(origin[1] - row)

            if manh_dist > row_dist:
                overlap_size = manh_dist - row_dist
                start = max(origin[0] - overlap_size, 0)
                end   = min(origin[0] + overlap_size, axis_max)
                if start <= end:
                    overlaps.append((start, end))

        overlaps.sort()

        extent = -1
        for left, right in zip(overlaps, overlaps[1:]):
            extent = max(extent, left[1])
            if extent < right[0]:
                return (extent + 1) * 4000000 + row

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")
    
    sensors = []
    for line in data:
        values = list(map(int, re.findall(r"-?\d+", line)))
        sensors.append(((values[0], values[1]), (values[2], values[3]),
                        abs(values[0] - values[2]) + abs(values[1] - values[3])))

    return sensors

def tests():
    test1_exp = 26
    test2_exp = 56000011

    data = parse_data("puzzles\\day-15\\test_input.txt")
    test1_res = row_impossibles(data, 10)
    test2_res = tuning_frequency(data, 20)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("puzzles\\day-15\\input.txt")
    answer1 = row_impossibles(data, 2000000)
    answer2 = tuning_frequency(data, 4000000)

    print(f"Part 1 -> Tuning Frequency: {answer1}")
    print(f"Part 2 -> Impossible in Row (2000000): {answer2}")

tests()
puzzle()