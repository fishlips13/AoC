import json

def total_numbers_recursive(base, current, ignore_red):

    if type(base) is str:
        return 0
    elif type(base) is int:
        return int(base)

    if type(base) is dict:
        dict_total = 0
        for pair in base.items():

            if ignore_red and type(pair[1]) is str and pair[1] == "red":
                dict_total = 0
                break

            dict_total += total_numbers_recursive(pair[0], 0, ignore_red)
            dict_total += total_numbers_recursive(pair[1], 0, ignore_red)

        current += dict_total

    elif type(base) is list:
        for item in base:
           current += total_numbers_recursive(item, 0, ignore_red)

    return current

with open("input/12.txt") as f:
    data = json.load(f)

print(f"Total Number Count: {total_numbers_recursive(data, 0, False)}")
print(f"Total Number Count (ignoring 'red'): {total_numbers_recursive(data, 0, True)}")