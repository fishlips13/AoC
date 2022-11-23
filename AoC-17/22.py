from copy import deepcopy

def print_grid(grid:dict, vidus):
    for y in range(-3, 5):
        row = ""
        for x in range(-5, 5):
            if (x,y) == vidus:
                row += "O"
            elif (x, y) not in grid:
                row += "."
            else:
                row += grid[(x, y)]
        print(row)
    print("")

def add_coords(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])
    
def virus_weak(grid):
    carrier_coords = (0, 0)
    carrier_facing = (0, -1)

    infected_count = 0
    for _ in range(10000):
        if carrier_coords not in grid:
            grid[carrier_coords] = "."

        if grid[carrier_coords] == ".":
            carrier_facing = (carrier_facing[1], -carrier_facing[0])
            grid[carrier_coords] = "#"
            infected_count += 1

        else:
            carrier_facing = (-carrier_facing[1], carrier_facing[0])
            grid[carrier_coords] = "."
        
        carrier_coords = add_coords(carrier_coords, carrier_facing)

    return infected_count

def virus_strong(grid):
    carrier_coords = (0, 0)
    carrier_facing = (0, -1)

    infected_count = 0
    for _ in range(10000000):
        if carrier_coords not in grid:
            grid[carrier_coords] = "."

        if grid[carrier_coords] == ".":
            carrier_facing = (carrier_facing[1], -carrier_facing[0])
            grid[carrier_coords] = "W"

        elif grid[carrier_coords] == "W":
            grid[carrier_coords] = "#"
            infected_count += 1

        elif grid[carrier_coords] == "#":
            carrier_facing = (-carrier_facing[1], carrier_facing[0])
            grid[carrier_coords] = "F"

        else:
            carrier_facing = (-carrier_facing[0], -carrier_facing[1])
            grid[carrier_coords] = "."

        carrier_coords = add_coords(carrier_coords, carrier_facing)

    return infected_count

with open("input\\22.txt") as f:
    data = f.read().split("\n")

grid_width = len(data) // 2

grid = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        coords = (x - grid_width, y - grid_width)
        grid[coords] = char

print(f"Infected Count: {virus_weak(deepcopy(grid))}")
print(f"Infected Count: {virus_strong(deepcopy(grid))}")