def checksum(dragon, space):
    while len(dragon) < space:
        extra = dragon[::-1]
        extra = extra.replace("1", "2")
        extra = extra.replace("0", "1")
        extra = extra.replace("2", "0")
        dragon += "0" + extra

    dragon = dragon[:space]

    while len(dragon) % 2 == 0:
        dragon_new = ""
        it = iter(dragon)
        for left in it:
            right = next(it)
            dragon_new += "1" if left == right else "0"
        dragon = dragon_new
    
    return dragon

with open("input\\16.txt") as f:
    dragon = f.read()

space1 = 272
space2 = 35651584

print(f"Chekcsum: {checksum(dragon, space1)}")
print(f"Chekcsum: {checksum(dragon, space2)}")