adjacents = [(0,1), (1,0), (0,-1), (-1,0)]

def coords_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def outside_visible_count(trees):
    visible = set()
    
    for orig in trees:
        for adj in adjacents:
            curr = orig
            
            while True:
                curr = coords_add(curr, adj)

                if curr not in trees:
                    visible.add(orig)
                    break
                elif trees[curr] >= trees[orig]:
                    break

    return len(visible)

def scenic_score_max(trees):
    scenic_max = 0

    for orig in trees:
        scenic = 1

        for adj in adjacents:
            curr = orig
            
            seen = 0
            while True:
                curr = coords_add(curr, adj)

                if curr not in trees:
                    break

                seen += 1

                if trees[curr] >= trees[orig]:
                    break
            
            scenic *= seen

        scenic_max = max(scenic, scenic_max)

    return scenic_max

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    trees = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            trees[(x,y)] = int(char)

    return trees

def tests():
    test1_exp = 21
    test2_exp = 8

    data = parse_data("day-08\\test_input.txt")
    test1_res = outside_visible_count(data)
    test2_res = scenic_score_max(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-08\\input.txt")
    answer1 = outside_visible_count(data)
    answer2 = scenic_score_max(data)

    print(f"Part 1 -> Outside Visible Count: {answer1}")
    print(f"Part 2 -> Scenic Score Max: {answer2}")

tests()
puzzle()