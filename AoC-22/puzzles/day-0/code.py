def func1(data):
    pass

def func2(data):
    pass

def parse_data(path):
    with open(path) as f:
        data = f.read()

    return data

def tests():
    test1_exp = None
    test2_exp = None

    data = parse_data("puzzles\\day-0\\test_input.txt")
    test1_res = func1(data)
    test2_res = func2(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("puzzles\\day-0\\input.txt")
    answer1 = func1(data)
    answer2 = func2(data)

    print(f"Part 1 -> : {answer1}")
    print(f"Part 2 -> : {answer2}")

tests()
puzzle()