with open("input/02.txt") as f:
    data = f.read().split("\n")

keypad_simple = ["123",
                 "456",
                 "789"]

keypad_complex = ["  1  ",
                  " 234 ",
                  "56789",
                  " ABC ",
                  "  D  "]

move_map = {"L" : (-1, 0), "R" : (1, 0), "U" : (0, -1), "D" : (0, 1)}

def build_keypad_map(keypad):
    keypad_map = {}

    for y in range(len(keypad)):
        for x in range(len(keypad[0])):
            if keypad[y][x] != " ":
                keypad_map[(x, y)] = keypad[y][x]

    return keypad_map

def find_code(all_steps, digit_map):
    for coords, digit in digit_map.items():
        if digit == "5":
            break

    code = ""

    for digit_steps in all_steps:
        for step in digit_steps:
            move = move_map[step]
            coords_new = (coords[0] + move[0], coords[1] + move[1])
            if coords_new in digit_map:
                coords = coords_new

        code += digit_map[coords]
    
    return code

digit_map_simple = build_keypad_map(keypad_simple)
digit_map_complex = build_keypad_map(keypad_complex)

print(f"Code: {find_code(data, digit_map_simple)}")
print(f"Code: {find_code(data, digit_map_complex)}")