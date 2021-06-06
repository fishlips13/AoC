right_sue_details = {"children" : 3, "cats" : 7, "samoyeds" : 2, "pomeranians" : 3, "akitas" : 0, "vizslas" : 0, "goldfish" : 5, "trees" : 3, "cars" : 2, "perfumes" : 1}

with open("input/16.txt") as f:
    data = f.read().split("\n")

sues = {}
for line, sue_id in zip(data, range(1, len(data)+1)):
    sues[sue_id] = {j[0] : int(j[1]) for j in [i.split(": ") for i in line[line.index(": ")+2:].split(", ")]}

wrong_sue_id = 0
for sue_id, details in sues.items():
    if all(detail in right_sue_details and right_sue_details[detail] == value \
        for detail, value in details.items()):
        wrong_sue_id = sue_id
        break

right_sue_id = 0
for sue_id, details in sues.items():
    if all(detail in right_sue_details and \
        ((detail == "cats" or detail == "trees") and right_sue_details[detail] < value or \
        (detail == "pomeranians" or detail == "goldfish") and right_sue_details[detail] > value or \
        (detail != "cats" and detail != "trees" and detail != "pomeranians" and detail != "goldfish" and right_sue_details[detail] == value))
    for detail, value in details.items()):
        right_sue_id = sue_id
        break
    
print(f"Wrong Sue ID: {wrong_sue_id}")
print(f"Right Sue ID: {right_sue_id}")
