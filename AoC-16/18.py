def safe_tile_count(row, row_count):
    safe_count = row.count(".")

    for _ in range(row_count - 1):
        row_new = ""

        for i in range(len(row)):
            left = row[i-1] if i > 0 else "."
            centre = row[i]
            right = row[i+1] if i < len(row) - 1 else "."

            if left == "^" and centre == "^" and right == "." or \
                left == "." and centre == "^" and right == "^" or \
                left == "^" and centre == "." and right == "." or \
                left == "." and centre == "." and right == "^":
                row_new += "^"
            else:
                row_new += "."

        safe_count += row_new.count(".")
        row = row_new

    return safe_count

with open("input\\18.txt") as f:
    row = f.read()

row_count1 = 40
row_count2 = 400000

print(f"Trap Count 1: {safe_tile_count(row, row_count1)}")
print(f"Trap Count 2: {safe_tile_count(row, row_count2)}")