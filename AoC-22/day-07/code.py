def find_total_10000(dirs):
    sizes_all = []
    dir_size(dirs, sizes_all)

    return sum([i for i in sizes_all if i <= 100000])

def delete_size(dirs):
    total_space  = 70000000
    space_needed = 30000000

    sizes_all = []
    dir_size(dirs, sizes_all)

    sizes_all.sort()
    
    deletion_size_min = space_needed - total_space + sizes_all[-1]
    for size in sizes_all:
        if size >= deletion_size_min:
            return size

def dir_size(dir, sizes_all):
    size = 0

    for item in dir.values():
        if type(item) == int:
            size += int(item)
        else:
            size += dir_size(item, sizes_all)

    sizes_all.append(size)

    return size

def parse_data(path):
    with open(path) as f:
        data = [i.split(" ") for i in f.read().split("\n")]

    dir_top = {}
    dir_stack = [dir_top]

    for line in data:
        if line == "$ ls":
            continue

        dir_curr = dir_stack[-1]

        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    dir_stack.pop()
                elif line[2] == "/":
                    dir_stack = [dir_top]
                else:
                    dir_stack.append(dir_curr[line[2]])
        
        elif line[1] not in dir_curr:
            dir_curr[line[1]] = {} if line[0] == "dir" else int(line[0])
            
    return dir_top

def tests():
    test1_exp = 95437
    test2_exp = 24933642

    data = parse_data("day-07\\test_input.txt")
    test1_res = find_total_10000(data)
    test2_res = delete_size(data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-07\\input.txt")
    answer1 = find_total_10000(data)
    answer2 = delete_size(data)

    print(f"Part 1 -> Total of <100000 Dirs: {answer1}")
    print(f"Part 2 -> Folder Delete Size: {answer2}")

tests()
puzzle()