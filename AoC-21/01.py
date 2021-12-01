with open("input\\01.txt") as f:
    depth_data = [int(i) for i in f.read().split("\n")]

increase_count_2 = sum([1 for i in zip(depth_data, depth_data[1:]) if i[0] < i[1]])

depth_triples = [sum(i) for i in zip(depth_data, depth_data[1:], depth_data[2:])]
increase_count_3 = sum([1 for i in zip(depth_triples, depth_triples[1:]) if i[0] < i[1]])

print(f"Total Depth Pair Increases: {increase_count_2}")
print(f"Total Depth Triple Increases: {increase_count_3}")