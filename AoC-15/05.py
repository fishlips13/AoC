with open("input/05.txt") as f:
    data = f.read().split("\n")

def part1():
    bad_strings = set(["ab", "cd", "pq", "xy"])
    vowels = ["a", "e", "i", "o", "u"]
    nice_count = 0

    for line in data:

        letters = {}
        for letter in line:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        vowel_count = 0
        for vowel in vowels:
            if vowel in letters:
                vowel_count += letters[vowel]

        pairs  = set()
        for i in range(len(line) - 1):
            pairs.add(line[i] + line[i+1])
        
        if vowel_count >= 3 and not pairs.intersection(bad_strings) and any(pair[0] == pair[1] for pair in pairs):
            nice_count += 1

    print("nice count: " + str(nice_count))

def part2():
    nice_count = 0

    for line in data:
        pairs = {}

        pair_found = False
        repeat_found = False

        for i in range(len(line)):

            if i < len(line) - 1:
                pair = line[i:i+2]
                if pair in pairs:
                    if pairs[pair] != i-1:
                        pair_found = True
                else:
                    pairs[pair] = i
            
            if i < len(line) - 2:
                if line[i] == line[i+2]:
                    repeat_found = True

        if pair_found and repeat_found:
            nice_count += 1

    print("nice count: " + str(nice_count))

part1()
part2()