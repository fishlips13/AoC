def signal_strength_sum(instrs):
    signal_strength = 0

    i, x = 1, 1
    for op, val in instrs:        
        for op_loop in range(1 if op == "noop" else 2):

            if (i - 20) % 40 == 0:
                signal_strength += x * i

            if op_loop == 1:
                x += val

            i += 1

    return signal_strength

def render_crt(instrs):
    rows = []

    i, x = 1, 1
    for op, val in instrs:        
        for op_loop in range(1 if op == "noop" else 2):
            
            i_row = (i - 1) // 40
            if len(rows) <= i_row:
                rows.append("")

            i_pixel = (i - 1) % 40
            visible = i_pixel >= x - 1 and i_pixel <= x + 1
            rows[i_row] += "#" if visible else "."

            if op_loop == 1:
                x += val

            i += 1

    return "\n".join(rows)

def parse_data(path):
    with open(path) as f:
        data = [i.split(" ") for i in f.read().split("\n")]

    return [(i[0], int(i[1]) if i[0] == "addx" else 0) for i in data]

def tests():
    test1_exp = 13140
    test2_exp = "\n".join(["##..##..##..##..##..##..##..##..##..##..",
                           "###...###...###...###...###...###...###.",
                           "####....####....####....####....####....",
                           "#####.....#####.....#####.....#####.....",
                           "######......######......######......####",
                           "#######.......#######.......#######....."])

    data = parse_data("day-10\\test_input.txt")
    test1_res = signal_strength_sum(data)
    test2_res = render_crt(data)

    assert test1_res == test1_exp, f"\n{test1_res}\nshould be\n{test1_exp}"
    assert test2_res == test2_exp, f"\n{test2_res}\nshould be\n{test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-10\\input.txt")
    answer1 = signal_strength_sum(data)
    answer2 = render_crt(data)

    print(f"Part 1 -> Signal Strength Sum: {answer1}")
    print(f"Part 2 -> CRT Output:\n{answer2}")

tests()
puzzle()

# PLULKBZH