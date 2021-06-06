from copy import deepcopy

def neighs_filled_count(x, y, seats):

    offsets = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    filled_count = 0

    for offset in offsets:
        neigh_x = x + offset[0]
        neigh_y = y + offset[1]

        if valid_seat(neigh_x, neigh_y, seats) and seats[neigh_y][neigh_x] == "#":
            filled_count += 1

    return filled_count

def direction_filled_count(x, y, seats):

    offsets = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    filled_count = 0

    for offset in offsets:

        next_x, next_y = x, y
        while True:
            next_x += offset[0]
            next_y += offset[1]

            if valid_seat(next_x, next_y, seats):
                if seats[next_y][next_x] == ".":
                    continue
                elif seats[next_y][next_x] == "#":
                    filled_count += 1

            break

    return filled_count

def valid_seat(x, y, seats):
    return x >= 0 and y >= 0 and x < len(seats[0]) and y < len(seats)

def seats_next(seats, fill_threshold,  search):

    new_seats = []
    changed = False
    for y in range(len(seats)):

        new_row = []
        new_seats.append(new_row)
        for x in range(len(seats[0])):

            filled_count = search(x, y, seats)
            if seats[y][x] == "L" and filled_count == 0:
                new_row.append("#")
                changed = True
            elif seats[y][x] == "#" and filled_count >= fill_threshold:
                new_row.append("L")
                changed = True
            else:
                new_row.append(seats[y][x])


    return new_seats, changed

def count_seats_filled(seats):
    filled_count = 0

    for row in seats:
        for seat in row:
            if seat == "#":
                filled_count += 1

    return filled_count

with open("input/11.txt") as f:
    seats = [[j for j in i] for i in f.read().split("\n")]

seats_copy = deepcopy(seats)

changed = True
while changed:
    seats, changed = seats_next(seats, 4, neighs_filled_count)

changed = True
while changed:
    seats_copy, changed = seats_next(seats_copy, 5, direction_filled_count)

print(f"Stable Neighbour Seats Filled: {count_seats_filled(seats)}")
print(f"Stable Direction Seats Filled: {count_seats_filled(seats_copy)}")