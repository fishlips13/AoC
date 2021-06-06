from copy import deepcopy

def add_coords(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

with open("input/24.txt") as f:
    data = f.read().split("\n")

direction_to_coord = {"e"  : (1,0),  "w"  : (-1,0),
                      "ne" : (0,1),  "sw" : (0,-1),
                      "se" : (1,-1), "nw" : (-1,1)}

paths = []
black_tiles = set()

for line in data:
    steps = []
    last_char = ""
    paths.append(steps)

    for char in line:
        if last_char == "n" or last_char == "s":
            steps[-1] += char
        else:
            steps.append(char)
        last_char = char

for path in paths:
    
    tile_coords = (0,0)
    for direction in path:
        step_coords = direction_to_coord[direction]
        tile_coords = add_coords(tile_coords, step_coords)

    if tile_coords not in black_tiles:
        black_tiles.add(tile_coords)
    else:
        black_tiles.remove(tile_coords)

initial_count = len(black_tiles)

days = 100
for _ in range(days):
    tiles_prev = deepcopy(black_tiles)
    tiles_next = deepcopy(black_tiles)
    white_candis = {}

    for tile_prev in tiles_prev:
        black_adj_count = 0

        for coord in direction_to_coord.values():
            adj_coord = add_coords(tile_prev, coord)
            if adj_coord in tiles_prev:
                black_adj_count += 1
            else: 
                if adj_coord not in white_candis:
                    white_candis[adj_coord] = 0
                white_candis[adj_coord] += 1
        
        if black_adj_count == 0 or black_adj_count > 2:
            tiles_next.remove(tile_prev)
    
    for coord, count in white_candis.items():
        if count == 2:
            tiles_next.add(coord)
        
    black_tiles = tiles_next

print(f"Initial Black Tile Count: {initial_count}")
print(f"{days} Day Black Tile Count: {len(black_tiles)}")