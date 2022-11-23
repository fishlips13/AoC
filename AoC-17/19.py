def coord_add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

adjacents = [(0,1), (1,0), (0,-1), (-1,0)]

with open("input\\19.txt") as f:
    data = f.read().split("\n")

grid = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        grid[(x, y)] = char

x_start = data[0].index("|")
path_curr = (x_start, 0)
path_prev = None
direction = (0, 1)
path = ""
distance = 0

done = False
while True:

    while grid[path_curr] != "+":

        if grid[path_curr] == " ":
            done = True
            break
        elif grid[path_curr].isalpha():
            path += grid[path_curr]

        distance += 1
        path_prev = path_curr
        path_curr = coord_add(path_curr, direction)
    
    if done:
        break

    for adjacent in adjacents:
        next_candi = coord_add(path_curr, adjacent)
        if grid[next_candi] != " " and next_candi != path_prev:
            path_curr = next_candi
            direction = adjacent
            distance += 1
            break


print(f"Path Landmarks: {path}")
print(f"Path Distance: {distance}")