from math import prod

class Tile:
    def __init__(self, tile_id, image_raw_string):
        self.tile_id = tile_id
        self.image_raw = []
        for row in image_raw_string:
            self.image_raw.append([i for i in row])

        self.image = [i[1:-1] for i in self.image_raw[1:-1]]

        self.top    = "".join(self.image_raw[0])
        self.bottom = "".join(self.image_raw[-1])
        self.left   = "".join([i[0] for i in self.image_raw])
        self.right  = "".join([i[-1] for i in self.image_raw])
    
    def get_borders_perms(self):
        borders = [self.top,    self.top[::-1],
                   self.bottom, self.bottom[::-1],
                   self.left,   self.left[::-1],
                   self.right,  self.right[::-1]]

        return ["".join(border) for border in borders]

    def transform(self, func):
        raw_new = func(self.image_raw)
        self.__init__(self.tile_id, raw_new)

def flip_image(image):
    return image[::-1]

def rotate_image(image):
    image_new = []
    for col in range(len(image[0])):
        image_new_row = []
        image_new.append(image_new_row)
        for row in range(len(image)):
            image_new_row.append(image[row][col])
    return [i[::-1] for i in image_new]

with open("input/20.txt") as f:
    data_tiles = [i.split("\n") for i in f.read().split("\n\n")]

tiles = {}
border_perms = {}
edge_count = {}

transform_ops = [rotate_image, rotate_image, rotate_image, flip_image, rotate_image, rotate_image, rotate_image]

sea_monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]

sea_monster_coords = [(0,18),
                      (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19),
                      (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)]

# Create tiles
for data_tile in data_tiles:
    tile_id = int(data_tile[0][5:-1])
    tiles[tile_id] = Tile(tile_id, data_tile[1:])

# Dict all edge perms
for tile_id, tile_upper in tiles.items():
    for border_perm in tile_upper.get_borders_perms():
        if border_perm not in border_perms:
            border_perms[border_perm] = []
        border_perms[border_perm].append(tile_id)

# Find borders and count occurrences
for border_tile_ids in border_perms.values():
    if len(border_tile_ids) == 1:
        border_tile_id = border_tile_ids[0]
        if border_tile_id not in edge_count:
            edge_count[border_tile_id] = 0
        edge_count[border_tile_id] += 1

# Corner tiles occur 4 times
corner_tile_ids = [tile_id for tile_id, count in edge_count.items() if count == 4]

# Pick arbitary corner to be top left and fix it
tile_top_left = tiles[corner_tile_ids[0]]
while len(border_perms[tile_top_left.top]) != 1 or len(border_perms[tile_top_left.left]) != 1:
    tile_top_left.transform(rotate_image)

tiles_grid = [[tile_top_left]]

# Find, fix, and grid left column
tile_upper = tile_top_left
while len(border_perms[tile_upper.bottom]) != 1:
    for tile_id in border_perms[tile_upper.bottom]:
        if tile_id != tile_upper.tile_id:
            break

    tile_lower = tiles[tile_id]
    tiles_grid.append([tile_lower])

    ops_iter = iter(transform_ops)
    while tile_lower.top != tile_upper.bottom:
        tile_lower.transform(next(ops_iter))

    tile_upper = tile_lower

# Find, fix, and grid each row
for tiles_row in tiles_grid:
    tile_left = tiles_row[0]

    while len(border_perms[tile_left.right]) != 1:
        for tile_id in border_perms[tile_left.right]:
            if tile_id != tile_left.tile_id:
                break

        tile_right = tiles[tile_id]
        tiles_row.append(tile_right)

        ops_iter = iter(transform_ops)
        while tile_right.left != tile_left.right:
            tile_right.transform(next(ops_iter))

        tile_left = tile_right

# Composite tile images into 1 image
image_full = [[] for _ in range(len(tile_top_left.image) * len(tiles_grid))]
for i, tiles_row in enumerate(tiles_grid):
    for tile in tiles_row:
        for j, image_row in enumerate(tile.image):
            image_full[i * len(tile.image) + j].extend(image_row)

monsters_found = False
ops_iter = iter(transform_ops)

# If found monsters, remove them from the map, else reorient the map until we do
while not monsters_found:
    for i in range(len(image_full) - 3):
        for j in range(len(image_full[0]) - 20):
            if all(["#" == image_full[i+x][j+y] for x, y in sea_monster_coords]):
                monsters_found = True
                for x, y in sea_monster_coords:
                    image_full[i+x][j+y] = " "
    
    image_full = next(ops_iter)(image_full)

# Count the remaining roughness
roughness = 0
for i in range(len(image_full)):
    for j in range(len(image_full[0])):
        if image_full[i][j] == "#":
            roughness += 1

print(f"Corner Product: {prod(corner_tile_ids)}")
print(f"Roughness: {roughness}")