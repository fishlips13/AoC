with open("input/06.txt") as f:
    data = f.read().split("\n")

message_most = ""
message_least = ""
for i in range(len(data[0])):
    char_count_dict = {}

    for line in data:
        if line[i] not in char_count_dict:
            char_count_dict[line[i]] = 0
        char_count_dict[line[i]] += 1
    
    char_count_list = [i for i in char_count_dict.items()]
    char_count_list.sort(key = lambda x: x[1])
    message_most += char_count_list[-1][0]
    message_least += char_count_list[0][0]

print(f"Message Fake: {message_most}")
print(f"Message Real: {message_least}")