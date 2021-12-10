from copy import deepcopy
from collections import deque

def find_bit_counts(data):
    counts = []

    for i in range(len(data[0])):
        counts.append(sum([1 for line in data if line[i] == "1"]))

    return counts

def find_valid(candis, mode):
    candis_deque = deque(candis)
    valids_deque = deque()

    while len(candis_deque) > 1:
        for i in range(len(candis[0])):
            bit_counts = find_bit_counts(candis_deque)

            candi_count_half = len(candis_deque) / 2
            while candis_deque:
                candi = candis_deque.pop()
                if mode == "1" and (candi[i] == "0" and bit_counts[i] < candi_count_half or \
                                    candi[i] == "1" and bit_counts[i] > candi_count_half) or \
                    mode == "0" and (candi[i] == "0" and bit_counts[i] > candi_count_half or \
                                     candi[i] == "1" and bit_counts[i] < candi_count_half) or \
                    candi[i] == mode and bit_counts[i] == candi_count_half:
                        valids_deque.append(candi)
            
            candis_deque = valids_deque
            valids_deque = deque()

            if len(candis_deque) == 1:
                break

    return candis_deque[0]

with open("input\\03.txt") as f:
    data = f.read().split("\n")

bit_counts = []

for i in range(len(data[0])):
    bit_counts = find_bit_counts(data)

gamma = int("".join(["1" if i > len(data) / 2 else "0" for i in bit_counts]), 2)
epsilon = int("1" * len(data[0]), 2) ^ gamma

o2_rating = int(find_valid(deepcopy(data), "1"), 2)
co2_rating = int(find_valid(deepcopy(data), "0"), 2)

print(f"Power Consumption: {gamma * epsilon}")
print(f"Life Support Rating: {o2_rating * co2_rating}")