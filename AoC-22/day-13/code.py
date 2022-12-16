import re
from functools import cmp_to_key

def correct_pairs_index_sum(pairs):
    index_sum = 0

    for i, pair in enumerate(pairs, 1):
        if compare_packets(*pair) == 1:
            index_sum += i
    
    return index_sum

def decoder_key(pairs, divider_data):
    pairs.extend(divider_data)
    packets = [j for i in pairs for j in i]
    
    packets.sort(key=cmp_to_key(compare_packets), reverse=True)
    
    decoder_key = 1
    for i, packet in enumerate(packets, 1):
        if  compare_packets(packet, divider_data[0][0]) == 0 or \
            compare_packets(packet, divider_data[0][1]) == 0 :
            decoder_key *= i
    
    return decoder_key

def compare_packets(left, right):
    if type(left) == list and type(right) == list:
        for sub_pair in zip(left, right):
            correct = compare_packets(*sub_pair)
            if correct != 0:
                return correct
        if len(left) == len(right):
            return 0
        else:
            return 1 if len(left) < len(right) else -1
    elif type(left) == list and type(right) == int:
        return compare_packets(left, [right])
    elif type(left) == int and type(right) == list:
        return compare_packets([left], right)
    else:
        if left > right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

def parse_data(path):
    with open(path) as f:
        data = [i.split("\n") for i in f.read().split("\n\n")]

    pairs = []
    for entry in data:
        pair = []
        for packet in entry:
            parts = re.findall(r"\d+|\[|\]", packet)
            stack = [[]]

            for char in parts[1:-1]:
                if char == "[":
                    stack.append([])
                elif char == "]":
                    temp = stack.pop()
                    stack[-1].append(temp)
                else:
                    stack[-1].append(int(char))

            pair.append(stack[0])
        pairs.append(pair)
    
    return pairs

def tests():
    test1_exp = 13
    test2_exp = 140

    data = parse_data("puzzles\\day-13\\test_input.txt")
    test1_res = correct_pairs_index_sum(data)

    divider_data = parse_data("puzzles\\day-13\\divider_input.txt")
    test2_res = decoder_key(data, divider_data)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("puzzles\\day-13\\input.txt")
    answer1 = correct_pairs_index_sum(data)

    divider_data = parse_data("puzzles\\day-13\\divider_input.txt")
    answer2 = decoder_key(data, divider_data)

    print(f"Part 1 -> Correct Index Sum: {answer1}")
    print(f"Part 2 -> Decoder Key: {answer2}")

tests()
puzzle()