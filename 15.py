def last_spoken(start, reps):
    numbers = {}
    last_number = start[-1]

    for i, item in enumerate(start):
        numbers[item] = (i, -1)

    for i in range(len(numbers), reps):
        if last_number in numbers and numbers[last_number][1] != -1:
            last_number = numbers[last_number][0] - numbers[last_number][1]
        else:
            last_number = 0
        
        numbers[last_number] = (i, numbers[last_number][0] if last_number in numbers else -1)

    return last_number

with open("input/15.txt") as f:
    data = [int(i) for i in f.read().split(",")]

rep_count = 2020
rep_count_long = 30000000

print(f"Last Number Spoken: {last_spoken(data, rep_count)}")
print(f"Last Number Spoken LONG: {last_spoken(data, rep_count_long)}")