def score_naive(path):
    naive_lookup = {"A" : {"X" : 1 + 3, "Y" : 2 + 6, "Z" : 3 + 0},
                    "B" : {"X" : 1 + 0, "Y" : 2 + 3, "Z" : 3 + 6},
                    "C" : {"X" : 1 + 6, "Y" : 2 + 0, "Z" : 3 + 3}}

    with open(path) as f:
        data = f.read()

    turns = [i.split() for i in data.split("\n")]

    return sum([naive_lookup[i][j] for i, j in turns])

def score_real(path):
    real_lookup =  {"A" : {"X" : 3 + 0, "Y" : 1 + 3, "Z" : 2 + 6},
                    "B" : {"X" : 1 + 0, "Y" : 2 + 3, "Z" : 3 + 6},
                    "C" : {"X" : 2 + 0, "Y" : 3 + 3, "Z" : 1 + 6}}

    with open(path) as f:
        data = f.read()

    turns = [i.split() for i in data.split("\n")]

    return sum([real_lookup[i][j] for i, j in turns])

def tests():
    test1_res = score_naive("day-02\\test_input.txt")
    test1_exp = 15
    test2_res = score_real("day-02\\test_input.txt")
    test2_exp = 12

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    naive_res = score_naive("day-02\\input.txt")
    real_res = score_real("day-02\\input.txt")

    print(f"Part 1 -> Game Score: {naive_res}")
    print(f"Part 2 -> Game Real: {real_res}")

tests()
puzzle()