with open("input/21.txt") as f:
    data = f.read().split("\n")

items = []
alrgn_items = {}
ingrds_count = {}

for line in data:

    parts = line[:-1].split(" (contains ")
    item_ingrds = parts[0].split(" ")
    item_alrgns = parts[1].split(", ")

    item = (item_ingrds, item_alrgns)
    items.append(item)

    for ingrd in item_ingrds:
        if ingrd not in ingrds_count:
            ingrds_count[ingrd] = 0
        ingrds_count[ingrd] += 1
    
    for alrgn in item_alrgns:
        if alrgn not in alrgn_items:
            alrgn_items[alrgn] = []
        alrgn_items[alrgn].append(item)

ingrd_candis = {}
for alrgn, algrn_items in alrgn_items.items():

    candi_temp = set()
    for algrn_item in algrn_items:
        ingrds = algrn_item[0]
        if not candi_temp:
            candi_temp = set(ingrds)
        else:
            candi_temp.intersection_update(set(ingrds))
        
    ingrd_candis[alrgn] = candi_temp

alrgns_ingrds = {}
while any([len(i) > 0 for _, i in ingrd_candis.items()]):

    for alrgn, ingrd in ingrd_candis.items():
        if len(ingrd) == 1:
            ingrd_found = ingrd.pop()
            alrgns_ingrds[alrgn] = ingrd_found
            break

    for _, ingrd in ingrd_candis.items():
        if ingrd_found in ingrd:
            ingrd.remove(ingrd_found)

non_alrgn_occurences = sum([count for ingrd, count in ingrds_count.items() if ingrd not in alrgns_ingrds.values()])

alrgn_list = list(alrgns_ingrds.keys())
alrgn_list.sort()
canon_danger_list = ",".join([alrgns_ingrds[alrgn] for alrgn in alrgn_list])

print(f"Non-allergenic Ingredients: {non_alrgn_occurences}")
print(f"Canonical Dangerous Ingredient List:\n{canon_danger_list}")