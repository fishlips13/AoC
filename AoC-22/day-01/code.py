
def cal_totals_sorted(path):
    with open(path) as f:
        data = f.read()

    elves = [list(map(int, i.split("\n"))) for i in data.split("\n\n")]
    totals = [sum(i) for i in elves]
    totals.sort(reverse=True)

    return totals

def tests():
    test1_res = 24000
    test2_res = 45000

    cal_totals = cal_totals_sorted("day-01\\test_input.txt")
    cal_top_3_total = sum(cal_totals[0:3])

    assert cal_totals[0] == test1_res, f"{cal_totals[0]}, should be {test1_res}"
    assert cal_top_3_total == test2_res, f"{cal_top_3_total}, should be {test2_res}"

    print("Tests passed")

def puzzle():
    cal_totals = cal_totals_sorted("day-01\\input.txt")
    top_3_total = sum(cal_totals[0:3])

    print(f"Part 1 -> Calorie Max: {cal_totals[0]}")
    print(f"Part 2 -> Calorie Max Top 3: {top_3_total}")

tests()
puzzle()