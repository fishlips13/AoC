import re

def dance(line, moves):
    for move in moves:

        if move[0] == "s":
            line = line[-move[1]:] + line[:-move[1]]

        elif move[0] == "x":
            temp = line[move[1]]
            line[move[1]] = line[move[2]]
            line[move[2]] = temp

        else:
            i1 = line.index(move[1])
            i2 = line.index(move[2])
            temp = line[i1]
            line[i1] = line[i2]
            line[i2] = temp
    
    return line


with open("input\\16.txt") as f:
    data = f.read().split(",")

moves = []
for entry in data:
    nums = [int(i) for i in re.findall(r"\d+", entry)]
    if entry[0] == "s":
        moves.append(("s", nums[0]))
    elif entry[0] == "x":
        moves.append(("x", nums[0], nums[1]))
    else:
        moves.append(("p", entry[1], entry[3]))

line1 = list("abcdefghijklmnop")
line_single = "".join(dance(line1, moves))

line2 = list("abcdefghijklmnop")
dummy = list("abcdefghijklmnop")

bill = 1000000000
for i in range(1, bill + 1):
    line2 = dance(line2, moves)
    if line2 == dummy:
        break

for _ in range(bill % i):
    line2 = dance(line2, moves)
        
line_full = "".join(line2)

print(f"Line Single: {line_single}")
print(f"Line Full: {line_full}")