from operator import xor

with open("input/02.txt") as f:
    data = f.read().split("\n")

for i in range(len(data)):
    values = data[i].split(" ") # "0-1 a: aaaaa"
    values[0] = [int(j) for j in values[0].split("-")]
    values[1] = values[1][0]
    data[i] = values # [0,1], "a", "aaaaa"

def part1():
    valid_count = 0
    for password in data:

        letter_count = 0
        for char in password[2]:
            if char == password[1]:
                letter_count += 1
        
        if letter_count >= password[0][0] and letter_count <= password[0][1]:
            valid_count += 1

    print(f"Part 1 Count: {str(valid_count)}")

def part2():
    valid_count = 0
    for password in data:

        first_occurs, second_occurs = False, False
        index1, index2 = password[0][0] - 1, password[0][1] - 1

        if index1 < len(password[2]):
            first_occurs = password[2][index1] == password[1]
            
        if index2 < len(password[2]):
            second_occurs = password[2][index2] == password[1]

        if xor(first_occurs, second_occurs):
            valid_count += 1
    
    print(f"Part 2 Count: {str(valid_count)}")

part1()
part2()