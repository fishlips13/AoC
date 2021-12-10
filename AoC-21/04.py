import re
from copy import deepcopy

def score_card_state(card_state):
    numbers = card_state[0][0]
    hits = card_state[0][1]

    total_unmarked = 0
    for i, row in enumerate(numbers):
        for j, value in enumerate(row):
            total_unmarked += int(value) * hits[i][j]
    return total_unmarked * int(card_state[1])

with open("input\\04.txt") as f:
    data = f.read().split("\n\n")

pulls = data[0].split(",")
card_count = 0
card_lookup = {}

for id, entry in enumerate(data[1:]):
    numbers = []
    hits = [[1] * 5 for _ in range(5)]
    card = (numbers, hits, id)
    card_count += 1

    for i, row in enumerate(entry.split("\n")):
        row_values = re.findall(r"\d+", row)
        numbers.append(row_values)

        for j, value in enumerate(row_values):
            if value not in card_lookup:
                card_lookup[value] = []
            card_lookup[value].append((card, i, j))

winner = None
loser = None
winners = set()

for pull in pulls:
    for card, i, j in card_lookup[pull]:
        card[1][i][j] = 0

        t = 8
        if sum(card[1][i]) == 0 or sum([k[j] for k in card[1]]) == 0:
            if not winner:
                winner = deepcopy((card, int(pull)))
            winners.add(card[2])
            if not loser and len(winners) == card_count:
                loser = deepcopy((card, int(pull)))

print(f"Winner Final Score: {score_card_state(winner)}")
print(f"Winner Loser Score: {score_card_state(loser)}")