def split_upper(lower_bound, upper_bound):
    return (lower_bound + upper_bound + 1) // 2, upper_bound
    
def split_lower(lower_bound, upper_bound):
    return lower_bound, (lower_bound + upper_bound - 1) // 2

with open("input/05.txt") as f:
    data = f.read().split("\n")

id_max = 0
ids = set()

for board_pass in data:

    y_lower, y_upper = 0, 127
    for char in board_pass[:7]:
        y_lower, y_upper = split_lower(y_lower, y_upper) if char == "F" else split_upper(y_lower, y_upper)
    
    x_lower, x_upper = 0, 7
    for char in board_pass[7:]:
        x_lower, x_upper = split_lower(x_lower, x_upper) if char == "L" else split_upper(x_lower, x_upper)

    _id = y_lower * 8 + x_lower
    ids.add(_id)
    id_max = max(_id, id_max)

second_id_iter = iter(ids)
next(second_id_iter)

my_id = 0
for _id in zip(ids, second_id_iter):
    if _id[0] != _id[1] - 1:
        my_id = _id[0] + 1
        break

print(f"Highest ID: {id_max}")
print(f"My ID: {_id[0] + 1}")