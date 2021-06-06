from hashlib import md5

def get_hash(data, start, max_count):
    for i in range(max_count):
        result = md5((data + str(i)).encode()).hexdigest()

        if result.startswith(start):
            return data + str(i), result

    return data + str(i), "found nothing"

with open("input/04.txt") as f:
    data = f.read()

five = get_hash(data, "00000", 999999)
six = get_hash(data, "000000", 9999999)

print("5 string: " + five[0] + "\n5 hash: " + five[1])
print("-----------")
print("6 string: " + six[0] + "\n6 hash: " + six[1])