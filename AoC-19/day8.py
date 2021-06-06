f = open("data.txt")
d = f.read()
f.close()

size = 25 * 6
pixel_it = (i for i in d)
display = [2] * size

while True:
    done = False

    for i in range(0, size):
        value = next(pixel_it, None)
        if value == None:
            done = True
            break

        if display[i] != 2:
            continue
        else:
            display[i] = int(value)

    if done:
        break

for i in range(0, 6):
    print("".join(str(i) for i in display[i*25:i*25+25]))

# f = open("data.txt")
# d = f.read()
# f.close()

# size = 25 * 6
# pixel_it = (i for i in d)
# counts_all = []

# while True:
#     count_layer = [0, 0, 0]
#     done = False

#     for _ in range(0, size):
#         value = next(pixel_it, None)
#         if value == None:
#             done = True
#             break

#         count_layer[int(value)] += 1

#     if done:
#         break
#     counts_all.append(count_layer)

# count_min = counts_all[0]
# for count in counts_all:
#     if (count[0] < count_min[0]):
#         count_min = count

# print(count_min[1] * count_min[2])