with open("input/01.txt") as f:
    data = f.read()

floor = 0
done = False

for i in range(len(data)):
    char = data[i]
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if not done and floor == -1:
        print("first basement: " + str(i+1))
        done = True

print("final: " + str(floor))