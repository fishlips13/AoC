from itertools import permutations

def best_seating_value(names, relations):
    happiness_max = 0
    for perm in permutations(names[1:]):
        seating = [names[0]] + list(perm)
        
        happiness = 0
        for i in range(len(seating)):
            seat_name = seating[i]
            left_name = seating[(i + len(seating) - 1) % len(seating)]
            right_name = seating[(i + 1) % len(seating)]
            
            happiness += relations[seat_name][left_name]
            happiness += relations[seat_name][right_name]

        happiness_max = max(happiness, happiness_max)

    return happiness_max

with open("input/13.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

relations = {}

for entry in data:
    person1 = entry[0]
    person2 = entry[-1][:-1]
    feeling = int(entry[3]) if entry[2] == "gain" else int(entry[3]) * -1

    if not person1 in relations:
        relations[person1] = {}

    relations[person1][person2] = feeling

guest_names = list(relations.keys())

myself = {}
for guest, relation in relations.items():
    myself[guest] = 0
    relation["Myself"] = 0

relations["Myself"] = myself
all_names = guest_names + ["Myself"]

print(f"Just Guests Best: {best_seating_value(guest_names, relations)}")
print(f"Myself and Guests Best: {best_seating_value(all_names, relations)}")