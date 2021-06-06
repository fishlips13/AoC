with open("input/16.txt") as f:
    data = f.read().split("\n")

rules  = {}
my_ticket = None
other_tickets = []
good_tickets = []

data_iter = iter(data)
for line in data_iter:

    if not line:
        continue
    elif line == "your ticket:":
        break

    rule_parts = line.split(": ")
    rule_pairs = rule_parts[1].split(" or ")
    rule_values1 = tuple(int(i) for i in rule_pairs[0].split("-"))
    rule_values2 = tuple(int(i) for i in rule_pairs[1].split("-"))
    rules[rule_parts[0]] = (rule_values1, rule_values2)

my_ticket = [int(i) for i in next(data_iter).split(",")]

next(data_iter)
next(data_iter)

for item in data_iter:
    other_tickets.append([int(i) for i in item.split(",")])

error_value = 0
for ticket in other_tickets:

    bad_ticket = False
    for field in ticket:
        if all([field < rule[0][0] or field > rule[0][1] and field < rule[1][0] or field > rule[1][1] for rule in rules.values()]):
            error_value += field
            bad_ticket = True
            continue
    
    if not bad_ticket:
        good_tickets.append(ticket)

field_poss_matrix = []
for _ in range(len(rules)):
    field_poss_matrix.append(set(rules.keys()))

for ticket in good_tickets:
    for i, field in enumerate(ticket):
        for name, rule_values in rules.items():
            if (field < rule_values[0][0] or field > rule_values[0][1] and field < rule_values[1][0] or field > rule_values[1][1]) and name in field_poss_matrix[i]:
                field_poss_matrix[i].remove(name)

field_poss_matrix = [i for i in enumerate(field_poss_matrix)]
field_poss_matrix.sort(key=lambda x: len(x[1]))
field_poss_matrix.reverse()

for i, j in zip(range(len(field_poss_matrix)), range(1, len(field_poss_matrix))):
    field_poss_matrix[i] = (field_poss_matrix[i][0], field_poss_matrix[i][1] - field_poss_matrix[j][1])

field_poss_matrix.sort(key=lambda x: x[0])

product = 1
for field_set in field_poss_matrix:
    for field in field_set[1]:
        if "departure" in field:
            product *= my_ticket[field_set[0]]

print(f"Error Value: {error_value}")
print(f"Ticket Product: {product}")