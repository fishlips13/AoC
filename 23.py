with open("input/23.txt") as f:
    data = f.read()

cup_count = 1000000
move_count = 10000000

cups = [int(i) for i in data]
cups.extend([i for i in range(len(data)+1, cup_count)])
highest = max(cups)

moves_so_far = 0
for _ in range(move_count):
    current = cups[0]
    removed = cups[1:4]
    remaining = [current] + cups[4:]
    
    destination = current - 1
    if destination == 0:
        destination = highest
    while destination in removed:
        destination -= 1
        if destination == 0:
            destination = highest

    dest_index = remaining.index(destination)
    cups = remaining[1:dest_index+1] + removed + remaining[dest_index+1:] + [remaining[0]]

one_index = cups.index(1)
cups_one_removed = cups[one_index+1:] + cups[:one_index]
labels = int("".join([str(i) for i in cups_one_removed]))

print(f"Cup Labels: {labels}")