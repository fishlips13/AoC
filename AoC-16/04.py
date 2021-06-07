import re

with open("input/04.txt") as f:
    data = f.read().split("\n")


rooms = []
target = "northpole object storage"

for line in data:
    hits = re.findall(r"\w+", line)
    name_chars = "".join(hits[:-2])
    sector = int(hits[-2])
    checksum = hits[-1]
    char_counts_dict = {}
    for name_char in name_chars:
        if name_char not in char_counts_dict:
            char_counts_dict[name_char] = 0
        char_counts_dict[name_char] += 1

    char_counts_list = [i for i in char_counts_dict.items()]
    char_counts_list.sort(key = lambda x: (-x[1], x[0]))

    if all(i[0] in checksum for i in char_counts_list[:5]):
        rooms.append((" ".join(hits[:-2]), sector))

valid_id_sum = 0
for room in rooms:
    valid_id_sum += room[1]

# 97 - 122
target_id = None
for room in rooms:
    offset = room[1] % 26
    name = []

    for name_char in room[0]:
        if name_char == " ":
            name.append(" ")
            continue

        ord_new = ord(name_char) + offset
        if ord_new > 122:
            ord_new -= 26
        name.append(chr(ord_new))
    
    if "".join(name) == target:
        target_id = room[1]
        break

print(f"Valid Room Sector ID Total: {valid_id_sum}")
print(f"North Pole Objects Sector ID: {target_id}")