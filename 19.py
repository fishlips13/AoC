def delve(message, index, rule_base):
    if index >= len(message):
        return set()
    elif rule_base in endpoints:
        if message[index] == endpoints[rule_base]:
            return set([1])
        return set()

    lengths_both = set()

    for rule_side in rules[rule_base]:
        lengths_side = delve(message, index, rule_side[0])

        for i in range(1, len(rule_side)):
            lengths_new = set()
            for length in lengths_side:
                length_candis = delve(message, index + length, rule_side[i])
                lengths_new.update([j + length for j in length_candis])
            lengths_side = lengths_new

        lengths_both.update(lengths_side)

    return {i for i in lengths_both if i <= len(message)}

def set_rule(item):
    parts1 = item.split(": ")
    parts2 = parts1[1].split(" | ")

    if "\"" in parts2[0]:
        endpoints[parts1[0]] = parts2[0].replace("\"", "")
        return
    
    rule = [i.split(" ") for i in parts2]
    rules[parts1[0]] = rule
    return

def count_valid():
    count = 0
    for message in messages:
        length_candidates = delve(message, 0, base_id)
        if len(message) in length_candidates:
            count += 1
    return count

with open("input/19.txt") as f:
    data = f.read().split("\n")

rules = {}
endpoints = {}
messages = []
base_id = "0"

data_iter = iter(data)

for item in data_iter:
    if not item:
        break

    set_rule(item)

for item in data_iter:
    messages.append(item)

print(f"Valid messages: {count_valid()}")

set_rule("8: 42 | 42 8")
set_rule("11: 42 31 | 42 11 31")

print(f"Valid loopy messages: {count_valid()}")