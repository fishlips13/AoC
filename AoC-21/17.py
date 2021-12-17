import re

with open("input\\17.txt") as f:
    data = [int(i) for i in re.findall(r"-?\d+", f.read())]

y_max = (data[2] + 1) * data[2] // 2

valid_count = 0
for x_candi in range(data[1] + 1):
    for y_candi in range(data[2], -data[2] + 1):
        x, y = 0, 0
        vx, vy = x_candi, y_candi

        while x < data[1] and y > data[2]:
            x += vx
            y += vy
            
            if data[0] <= x <= data[1] and data[2] <= y <= data[3]:
                valid_count += 1
                break

            if vx > 0:
                vx -= 1
            vy -= 1

print(f"Highest Valid y: {y_max}")
print(f"Valid Initial Velocity Count: {valid_count}")