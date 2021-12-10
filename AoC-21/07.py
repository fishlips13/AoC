with open("input\\07.txt") as f:
    data = [int(i) for i in f.read().split(",")]

fuel_min_simple = 99999999999999999
fuel_min_complex = 99999999999999999

for x in range(min(data), max(data) + 1):
    fuel_min_simple = min(fuel_min_simple, sum([abs(x - i) for i in data]))
    fuel_min_complex = min(fuel_min_complex, sum([((abs(x - i) + 1) * abs(x - i) // 2) for i in data]))

print(f"Minimum fuel simple: {fuel_min_simple}")
print(f"Minimum fuel complex: {fuel_min_complex}")