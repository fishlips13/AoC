def first_marker_start(packet, length):
    for i in range(len(packet) - length):
        char_set = set(packet[i:i+length])
        if len(char_set) == length:
            return i + length

def parse_data(path):
    with open(path) as f:
        data = f.read()

    return data

def tests():
    test1_exp = 5
    test2_exp = 23

    data = parse_data("day-06\\test_input.txt")
    test1_res = first_marker_start(data, 4)
    test2_res = first_marker_start(data, 14)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-06\\input.txt")
    answer1 = first_marker_start(data, 4)
    answer2 = first_marker_start(data, 14)

    print(f"Part 1 -> First Packet Start: {answer1}")
    print(f"Part 2 -> First Message Start: {answer2}")

tests()
puzzle()