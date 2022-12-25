decimal_lookup = {"2" : 2, "1" : 1, "0" : 0,  "-" : -1,  "=" : -2}
snafu_lookup   = { 2 : "2", 1 : "1", 0 : "0", -1  : "-", -2  : "="}

def fuel_requirement_sum(fuel_reqs):
    decimal_sum = sum([snafu_to_decimal(i) for i in fuel_reqs])

    return decimal_to_snafu(decimal_sum)

def snafu_to_decimal(snafu):
    value = 0

    for i, digit in enumerate(reversed(snafu)):
        value += 5 ** i * decimal_lookup[digit]

    return value

def decimal_to_snafu(decimal):
    dec_remain = decimal
    remain_maxs = []

    curr_max = 0
    while True:
        curr_max += 2 * (5 ** len(remain_maxs))
        if curr_max >= dec_remain:
            break
        remain_maxs.append(curr_max)

    snafu = ""
    for i, remain_max in enumerate(reversed(remain_maxs)):
        exp = len(remain_maxs) - i

        for dec_mult, snafu_digit in snafu_lookup.items():
            dec_val = dec_mult * (5 ** exp)
            if abs(dec_remain - dec_val) <= remain_max:
                snafu += snafu_digit
                dec_remain -= dec_val
                break

    return snafu + snafu_lookup[dec_remain]

def test_examples(path):
    with open(path) as f:
        data = [i.split(",") for i in f.read().split("\n")]

    examples = [(int(i[0]), i[1]) for i in data]

    for decimal, snafu in examples:
        test1_res = snafu_to_decimal(snafu)
        test2_res = decimal_to_snafu(decimal)

        assert test1_res == decimal, f"{test1_res}, should be {decimal}"
        assert test2_res == snafu, f"{test2_res}, should be {snafu}"

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    return data

def tests():
    test_examples("day-25\\examples.txt")

    test_exp = "2=-1=0"

    data = parse_data("day-25\\test_input.txt")
    test_res = fuel_requirement_sum(data)

    assert test_res == test_exp, f"{test_res}, should be {test_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-25\\input.txt")
    answer1 = fuel_requirement_sum(data)
    
    print(f"Part 1 -> Fuel Requirement Sum: {answer1}")

tests()
puzzle()