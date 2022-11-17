def phrase_valid(phrase):
    used = set()
    for word in phrase:

        if word in used:
            return False
        used.add(word)

    return True

def phrase_valid_anag(phrase):
    used = set()
    for word in phrase:

        letters = list(word)
        letters.sort()
        word = "".join(letters)

        if word in used:
            return False
        used.add(word)

    return True

with open("input\\04.txt") as f:
    data = [i.split() for i in f.read().split("\n")]

valid_count = sum([1 if phrase_valid(i) else 0 for i in data])
valid_count_anag = sum([1 if phrase_valid_anag(i) else 0 for i in data])

print(f"Valid Count: {valid_count}")
print(f"Valid Count Anagram: {valid_count_anag}")