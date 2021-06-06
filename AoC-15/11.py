def next_pass(current):
    i = len(current) - 1
    rollover = True

    while rollover:
        current[i], rollover = next_char(current[i])
        i -= 1
    
    return current

def next_char(current):
    new_ord = ord(current) + 1
    if new_ord != 123:
        return chr(new_ord), False
    else:
        return "a", True

def password_valid(candi):

    invalid_chars = ["i", "o", "l"]
    if any((True for i in invalid_chars if i in candi)):
        return False

    doubles = 0
    doubles_iter = iter(range(len(candi)))
    for i in doubles_iter:
        if i >= len(candi) - 1:
            break

        if candi[i] == candi[i+1]:
            doubles += 1
            next(doubles_iter)

    if doubles < 2:
        return False

    for i in range(len(candi) - 2):
        if ord(candi[i]) == ord(candi[i+1]) - 1 and ord(candi[i]) == ord(candi[i+2]) - 2:
            return True

    return False

with open("input/11.txt") as f:
    data = [i for i in f.read()]

while not password_valid(data):
    data = next_pass(data)

print(f"Next Password: {''.join(data)}")

data = next_pass(data)
while not password_valid(data):
    data = next_pass(data)
    
print(f"Next Password: {''.join(data)}")