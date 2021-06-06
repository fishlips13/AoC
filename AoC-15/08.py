with open("input/08.txt") as f:
    data = f.read().split("\n")

hex_chars = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"])

all_count = 0
escape_count = 0
for line in data:

    all_count += len(line)
    escape_count += 4
    literal = line[1:-1]
    
    char_iter = iter(range(len(literal)))
    for i in char_iter:

        all_count -= 1

        if literal[i] != "\\":
            continue

        escape_count += 1
        if i < len(literal) - 1 and (literal[i+1] == "\\" or literal[i+1] == "\""):
            escape_count += 1
            next(char_iter)
        elif i < len(literal) - 3 and literal[i+1] == "x" and literal[i+2] in hex_chars and literal[i+3] in hex_chars:
            next(char_iter)
            next(char_iter)
            next(char_iter)
    pass
    
print(f"Part 1 Count: {all_count}")
print(f"Part 2 Count: {escape_count}")
pass