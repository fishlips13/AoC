with open("input\\10.txt") as f:
    data = f.read().split("\n")

bound_lookup = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
error_lookup = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
ac_lookup = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}

error_score = 0
ac_scores = []

for line in data:
    start_stack = []

    valid = True
    for bound in line:
        if bound in bound_lookup:
            start_stack.append(bound)
            continue
        
        start = start_stack.pop()
        if bound_lookup[start] != bound:
            error_score += error_lookup[bound]
            valid = False
            break
    
    if not valid:
        continue

    ac_score = 0
    while start_stack:
        ac_score = 5 * ac_score + ac_lookup[start_stack.pop()]

    ac_scores.append(ac_score)

ac_middle_score = sorted(ac_scores)[(len(ac_scores) - 1) // 2]

print(f"Error Score: {error_score}")
print(f"Autocomplete Middle Score: {ac_middle_score}")