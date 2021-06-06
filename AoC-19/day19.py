from intcode import Intcode

def probe_location(x, y):
    drone = Intcode()
    drone.input_signal(x)
    drone.input_signal(y)
    return drone.output_signal()

def in_map(x, y):
    return x >= 0 and x < 50 and y >= 0 and y < 50

grid = [[""] * 50 for _ in range(50)]

x_left = 4
x_right = 4
y = 3

tractor_lines = {y : x_right}

while True:
    y += 1
    x_left += 1
    x_right += 1

    # Lower bound, find pull
    while not probe_location(x_left, y):
        x_left += 1

    # Upper Bound, find no pull
    while probe_location(x_right, y):
        x_right += 1

    tractor_lines[y] = x_right - 1

    y_opp = y - 99
    x_opp = x_left + 99

    if y % 100 == 0:
        print(y)

    if y_opp in tractor_lines and x_opp <= tractor_lines[y_opp]:
        print(x_left, y_opp)
        break

print("Done")

# While x,y in map (0 -> 49)
#   (Trace bottom, moving down always follows left+bottom side)
#   While x,y is not pulled
#       Move right, x++
#   dict add ->  y : (x,x)
#   Move down, y++


# While x,y in map (0 -> 49)
#   (Trace top, moving right always follows top+right side)
#   While x,y is not pulled
#       Move down, y++
#   dict set -> y : (dict[y][0], max(dict[y][1], x))
#   Move right, x++

# For i in dict
#   Total += i[1] - i[0]


# total = 0
# for y in range(50):
#     for x in range(50):
#         grid[y][x] = "#" if probe_location(x, y) else "."

# for line in grid:
#     print("".join(line))