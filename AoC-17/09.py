import re

with open("input\\09.txt") as f:
    data = f.read()

garbage = []
garbage_count = 0
i_left = 0
while i_left < len(data):
    if data[i_left] == "<":
        garbage_count -= 1

        i_right = i_left
        while True:

            if data[i_right] == "!":
                garbage_count -= 1
                i_right += 1
            elif data[i_right] == ">":
                garbage.append((i_left, i_right + 1))
                i_left = i_right + 1
                break

            garbage_count += 1
            i_right += 1

    i_left += 1

clean = ""
i_left = 0
for pile in garbage:
    clean += data[i_left : pile[0]]
    i_left = pile[1]
clean += data[i_left:]

curlies = "".join(re.findall(r"[{}]", clean))

depth = 0
score = 0
for bracket in curlies:
    if bracket == "{":
        depth += 1
    else:
        score += depth
        depth -= 1

print(f"Score: {score}")
print(f"Garbage Count: {garbage_count}")