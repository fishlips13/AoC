import re
from math import prod
from copy import deepcopy

def monkey_bus(monkeys, rounds, reduce=True):
    counts = [0] * len(monkeys)
    test_prod = prod([i for _, _, _, i, _, _  in monkeys])

    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            items, operation, op_value, test, true_throw, false_throw = monkey
            counts[i] += len(items)

            while items:
                item_new = operation(items.pop(0), op_value)
                if reduce:
                    item_new //= 3
                else:
                    item_new %= test_prod

                if item_new % test == 0:
                    monkeys[true_throw][0].append(item_new)
                else:
                    monkeys[false_throw][0].append(item_new)

    counts.sort(reverse=True)

    return counts[0] * counts[1]

def parse_data(path):
    with open(path) as f:
        data = [i.split("\n") for i in f.read().split("\n\n")]

    monkeys = []
    for entry in data:
        start       = re.findall(r"\d+", entry[1])
        op_value    = re.findall(r"\d+", entry[2])
        test        = re.findall(r"\d+", entry[3])[0]
        true_throw  = re.findall(r"\d+", entry[4])[0]
        false_throw = re.findall(r"\d+", entry[5])[0]

        if not op_value:
            operation = lambda x, _: x * x
        elif "+" in entry[2]:
            operation = lambda x, y: x + y
        else:
            operation = lambda x, y: x * y

        monkeys.append((list(map(int, start)),
                        operation,
                        int(op_value[0]) if op_value else None,
                        int(test),
                        int(true_throw),
                        int(false_throw)))

    return monkeys

def tests():
    test1_exp = 10605
    test2_exp = 2713310158

    data = parse_data("day-11\\test_input.txt")
    test1_res = monkey_bus(deepcopy(data), 20)
    test2_res = monkey_bus(deepcopy(data), 10000, False)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-11\\input.txt")
    answer1 = monkey_bus(deepcopy(data), 20)
    answer2 = monkey_bus(deepcopy(data), 10000, False)

    print(f"Part 1 -> Monkey Business (20): {answer1}")
    print(f"Part 2 -> Worrisome Monkey Business (10000): {answer2}")

tests()
puzzle()