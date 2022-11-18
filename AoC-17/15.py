import re

with open("input\\15.txt") as f:
    data = f.read()

a_start, b_start = [int(i) for i in re.findall(r"\d+", data)]

a_val, b_val = a_start, b_start
match_count1 = 0

for _ in range(40000000):
    a_val = (a_val * 16807) % 2147483647
    b_val = (b_val * 48271) % 2147483647
    
    a_bin_str = f"{a_val:016b}"[-16:]
    b_bin_str = f"{b_val:016b}"[-16:]


    if a_bin_str == b_bin_str:
        match_count1 += 1

print(f"Match Count: {match_count1}")

a_val, b_val = a_start, b_start
match_count2 = 0

for _ in range(5000000):
    while True:
        a_val = (a_val * 16807) % 2147483647
        if a_val % 4 == 0:
            break

    while True:
        b_val = (b_val * 48271) % 2147483647
        if b_val % 8 == 0:
            break
    
    a_bin_str = f"{a_val:016b}"[-16:]
    b_bin_str = f"{b_val:016b}"[-16:]

    if a_bin_str == b_bin_str:
        match_count2 += 1

print(f"Match Count: {match_count2}")