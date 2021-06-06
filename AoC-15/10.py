with open("input/10.txt") as f:
    data = [int(i) for i in f.read()]

def look_say(data, reps):
    for _ in range(reps):
        new_data = []

        current_value = None
        streak = 1

        for value in data:
            if value != current_value:

                if current_value:
                    new_data.append(streak)
                    new_data.append(current_value)

                current_value = value
                streak = 1
            else:
                streak += 1

        new_data.append(streak)
        new_data.append(current_value)

        data = new_data
    
    return data

print(f"Length 40: {len(look_say(data, 40))}")
print(f"Length 50: {len(look_say(data, 50))}")