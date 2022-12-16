move_lookup = {"U" : (0,1), "L" : (1,0), "D" : (0,-1), "R" : (-1,0)}

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def coords_sub(coord1, coord2):
    return (coord1[0] - coord2[0], coord1[1] - coord2[1])

def coord_norm(coord):
    return (coord[0] // abs(coord[0]) if coord[0] else 0, coord[1] // abs(coord[1]) if coord[1] else 0)

def segment_follow(head, tail):
    diff_x = abs(head[0] - tail[0])
    diff_y = abs(head[1] - tail[1])

    if diff_x > 1 or diff_y > 1:
        dist = coords_sub(head, tail)
        fix  = coord_norm(dist)
        return coords_add(tail, fix)

    return tail

def short_tail_positions(moves):
    head, tail = (0,0), (0,0)
    tail_past = set()
    tail_past.add(tail)

    for direction, count in moves:
        for _ in range(count):
            head = coords_add(head, move_lookup[direction])
            
            tail = segment_follow(head, tail)

            tail_past.add(tail)

    return len(tail_past)

def long_tail_positions(moves):
    segments = [(0,0)] * 10
    tail_past = set()
    tail_past.add(segments[9])

    for direction, count in moves:
        for _ in range(count):
            segments[0] = coords_add(segments[0], move_lookup[direction])
            
            for i, segs in enumerate(zip(segments, segments[1:])):
                segments[i+1] = segment_follow(*segs)

            tail_past.add(segments[9])

    return len(tail_past)

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    return [(i[0], int(i[2:])) for i in data]

def tests():
    test1_exp = 13
    test2_exp = 1
    test3_exp = 36

    data1 = parse_data("puzzles\\day-09\\test_input_1.txt")
    data2 = parse_data("puzzles\\day-09\\test_input_2.txt")
    test1_res = short_tail_positions(data1)
    test2_res = long_tail_positions(data1)
    test3_res = long_tail_positions(data2)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"
    assert test3_res == test3_exp, f"{test3_res}, should be {test3_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("puzzles\\day-09\\input.txt")
    answer1 = short_tail_positions(data)
    answer2 = long_tail_positions(data)

    print(f"Part 1 -> Short Tail Positions: {answer1}")
    print(f"Part 2 -> Long Tail Positions: {answer2}")

tests()
puzzle()