import re

with open("input\\15.txt") as f:
    data = f.read().split("\n")

discs = []
for line in data:
    hits = re.findall(r"\d+", line) 
    discs.append((int(hits[1]), int(hits[-1])))