from hashlib import md5

with open("input/05.txt") as f:
    data = f.read()

chars_basic = []
chars_adv = {}
valid_indicies = ["0", "1", "2", "3", "4", "5", "6", "7"]

i = 0
while len(chars_basic) < 8 or len(chars_adv) < 8:
    candi = data + str(i)

    result = md5(candi.encode()).hexdigest()
    if result.startswith("00000"):
        sixth_char = result[5]
        if len(chars_basic) < 8:
            chars_basic.append(sixth_char)
        if sixth_char in valid_indicies and sixth_char not in chars_adv:
            chars_adv[sixth_char] = result[6]

    i += 1

code_adv = [i for i in chars_adv.items()]
code_adv.sort(key = lambda x: x[0])

print(f"Basic Passcode {''.join(chars_basic)}")
print(f"Advanced Passcode {''.join([i[1] for i in code_adv])}")