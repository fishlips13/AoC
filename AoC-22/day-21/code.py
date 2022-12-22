def solve_monkey(monkeys, name = "root"):
    monkey = monkeys[name]
    if type(monkey) == int:
        return monkey
    
    left = solve_monkey(monkeys, monkey[0])
    right = solve_monkey(monkeys, monkey[2])

    if monkey[1] == "+":
        return left + right
    elif monkey[1] == "-":
        return left - right
    elif monkey[1] == "*":
        return left * right
    else:
        return left // right

def solve_human(monkeys, name = "root", final_value = None):
    monkey = monkeys[name]
    humn_in_left = name_in_tree(monkeys, monkey[0], "humn")
    other_tree_value = solve_monkey(monkeys, monkey[2] if humn_in_left else monkey[0])

    if final_value == None:
        return solve_human(monkeys, monkey[0] if humn_in_left else monkey[2], other_tree_value)

    if monkey[1] == "+":
        humn_tree_value = final_value - other_tree_value
    elif monkey[1] == "-":
        humn_tree_value = final_value + other_tree_value if humn_in_left else -final_value + other_tree_value
    elif monkey[1] == "*":
        humn_tree_value = final_value // other_tree_value
    else:
        humn_tree_value = final_value * other_tree_value if humn_in_left else other_tree_value // final_value

    if monkey[0] == "humn" or monkey[2] == "humn":
        return humn_tree_value

    return solve_human(monkeys, monkey[0] if humn_in_left else monkey[2], humn_tree_value)

def name_in_tree(monkeys, tree_name, name):
    monkey = monkeys[tree_name]
    if tree_name == "humn":
        return True
    elif type(monkey) == int:
        return False

    return name_in_tree(monkeys, monkey[0], name) or \
            name_in_tree(monkeys, monkey[2], name)

def parse_data(path):
    with open(path) as f:
        data = [i.split(" ") for i in f.read().split("\n")]

    monkeys = {}
    for entry in data:        
        monkeys[entry[0][:-1]] = tuple(entry[1:]) if len(entry) != 2 else int(entry[1])

    return monkeys

def tests():
    test1_exp = 152
    test2_exp = 301

    data = parse_data("day-21\\test_input.txt")
    test1_res = solve_monkey(data)
    test2_res = solve_human(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-21\\input.txt")
    answer1 = solve_monkey(data)
    answer2 = solve_human(data)

    print(f"Part 1 -> Root Answer: {answer1}")
    print(f"Part 2 -> Human Answer: {answer2}")

tests()
puzzle()