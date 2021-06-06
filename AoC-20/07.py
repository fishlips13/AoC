def contained_bags_count(base_type, bag_types):
    count = 0
    if base_type in bag_types:
        for sub_type, sub_type_count in bag_types[base_type].items():
            count += sub_type_count + sub_type_count * contained_bags_count(sub_type, bag_types)
    return count

with open("input/07.txt") as f:
    data = f.read().split("\n")

bag_types = {}
for line in data:
    bag_type, content_data = line.split(" contain ")
    if content_data != "no other bags.":
        content_types = {i[2:-4] if i[-1] != "s" else i[2:-5] : int(i[0]) for i in content_data[:-1].split(", ")}
    else:
        content_types = {}
    bag_types[bag_type[:-5]] = content_types

my_bag = "shiny gold"
valid_bags = set()
frontier_bags = {my_bag}

while frontier_bags:
    frontier_bag = frontier_bags.pop()
    for bag_type, bag_contents in bag_types.items():
        if frontier_bag in bag_contents and bag_type not in valid_bags:
            valid_bags.add(bag_type)
            frontier_bags.add(bag_type)

print(f"Outermost Valid Count: {len(valid_bags)}")
print(f"Bags in Shiny Gold: {contained_bags_count(my_bag, bag_types)}")