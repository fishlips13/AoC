from itertools import pairwise

with open("input\\01.txt") as f:
    data = [int(i) for i in f.read()]

data_cycle = data + [data[0]]
data_shifted = data[len(data) // 2:] + data[:len(data) // 2]

total1 = sum([i for i, j in pairwise(data_cycle) if i == j])
total2 = sum([i for i, j in zip(data, data_shifted) if i == j])

print(f"Captcha Total 1: {total1}")
print(f"Captcha Total 2: {total2}")