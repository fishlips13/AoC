
def priority_sum(path):
    with open(path) as f:
        data = f.read()

    sacks = data.split("\n")
    
    priority_total = 0
    for sack in sacks:
        comp_size = len(sack) // 2
        left  = set(i for i in sack[0:comp_size])
        right = set(i for i in sack[comp_size:])

        pair = left.intersection(right)
        priority_total += priority(pair.pop())

    return priority_total

def badge_sum(path):
    with open(path) as f:
        data = f.read()

    sacks = data.split("\n")
    
    priority_total = 0
    for i in range(0, len(sacks), 3):
        overlap = set(sacks[i]).intersection(set(sacks[i+1])).intersection(set(sacks[i+2]))

        priority_total += priority(overlap.pop())

    return priority_total

def priority(item):
    ord_val = ord(item)

    if ord_val > 96:
        return ord_val - 96
    else:
        return ord_val - 64 + 26

def tests():
    test1_exp = 157
    test2_exp = 70

    test1_res = priority_sum("day-03\\test_input.txt")
    test2_res = badge_sum("day-03\\test_input.txt")

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    mistake_priorities = priority_sum("day-03\\input.txt")
    badge_priorities = badge_sum("day-03\\input.txt")

    print(f"Part 1 -> Sum of Mistake Priorities: {mistake_priorities}")
    print(f"Part 2 -> Sum of Badge Priorities: {badge_priorities}")

tests()
puzzle()