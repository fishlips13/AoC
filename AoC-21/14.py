import re

def build_polymer_counts(template, elements, lookup, max_depth):
    counts = [0] * len(elements)
    cache = [{} for _ in range(max_depth)]

    for pair in zip(template, template[1:]):
        result = build_pair("".join(pair), lookup, elements, 0, max_depth, cache)
        counts = [i + j for i, j in zip(counts, result)]
    
    overlaps = [template[1:-1].count(i) for i in elements]

    return [i + j for i, j in zip(counts, overlaps)]

def build_pair(pair, lookup, elements, depth, max_depth, cache):
    if depth == max_depth:
        return [pair.count(i) for i in elements]

    if pair in cache[depth]:
        return cache[depth][pair]

    left = build_pair(pair[0] + lookup[pair], lookup, elements, depth + 1, max_depth, cache)
    right = build_pair(lookup[pair] + pair[1], lookup, elements, depth + 1, max_depth, cache)
    result = [i + j for i, j in zip(left, right)]
    result[elements.index(lookup[pair])] -= 1
    cache[depth][pair] = tuple(result)
    
    return result

with open("input\\14.txt") as f:
    data = f.read()

elements = list(set(re.findall(r"[A-Z]", data)))
elements.sort()
data = [i.split(" -> ") for i in data.split("\n")]

inserts = {i[0] : i[1] for i in data[2:]}

counts_10 = build_polymer_counts(data[0][0], elements, inserts, 10)
counts_40 = build_polymer_counts(data[0][0], elements, inserts, 40)
min_max_diff_10 = max(counts_10) - min(counts_10)
min_max_diff_40 = max(counts_40) - min(counts_40)

print(f"Element Min Max Difference (10): {min_max_diff_10}")
print(f"Element Min Max Difference (40): {min_max_diff_40}")