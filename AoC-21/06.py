with open("input\\06.txt") as f:
    data = [int(i) for i in f.read().split(",")]

def fish_after_days(days, fish):
    for _ in range(days):
        spawners = fish[0]
        fish = fish[1:]
        fish[6] += spawners
        fish.append(spawners)
    return sum(fish)

fish = [0] * 9

for value in data:
    fish[value] += 1
    
print(f"Total fish after 80 days: {fish_after_days(80, fish)}")
print(f"Total fish after 256 days: {fish_after_days(256, fish)}")