
def full_overlap_count(pairs):
    full_overlaps = 0
    for left, right in pairs:
        if  left[0] >= right[0] and left[1] <= right[1] or \
            right[0] >= left[0] and right[1] <= left[1]:
            full_overlaps += 1

    return full_overlaps

def partial_overlap_count(pairs):
    partial_overlaps = 0
    for left, right in pairs:
        if  left[0] >= right[0] and left[0] <= right[1] or \
            left[1] >= right[0] and left[1] <= right[1] or \
            right[0] >= left[0] and right[0] <= left[1] or \
            right[1] >= left[0] and right[1] <= left[1]:
            partial_overlaps += 1

    return partial_overlaps

def parse_data(path):
    with open(path) as f:
        data = f.read()

    pairs = []
    for line in data.split("\n"):
        left, right = line.split(",")
        pairs.append([list(map(int, left.split("-"))), list(map(int, right.split("-")))])
    
    return pairs

def tests():
    test1_exp = 2
    test2_exp = 4

    pairs = parse_data("puzzles\\day-04\\test_input.txt")
    test1_res = full_overlap_count(pairs)
    test2_res = partial_overlap_count(pairs)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    pairs = parse_data("puzzles\\day-04\\input.txt")
    answer1 = full_overlap_count(pairs)
    answer2 = partial_overlap_count(pairs)

    print(f"Part 1 -> Full Overlap Count: {answer1}")
    print(f"Part 2 -> Partial Overlap Count: {answer2}")

tests()
puzzle()