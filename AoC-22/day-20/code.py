def gps_decrypt(numbers, loops, encryption_key):
    number_array = []
    numbers_and_ids = []

    for i, number in enumerate(numbers):
        number_and_id = (number * encryption_key, i)
        number_array.append(number_and_id)
        numbers_and_ids.append(number_and_id)

    for _ in range(loops):
        for number_and_id in numbers_and_ids:
            i_array = number_array.index(number_and_id)
            popped = number_array.pop(i_array)
            i_new = (i_array + number_and_id[0]) % len(number_array)
            number_array.insert(i_new, popped)

    zero_index = 0
    while True:
        if number_array[zero_index][0] == 0:
            break
        zero_index += 1

    markers = [1000, 2000, 3000]
    marker_sum = 0
    for marker in markers:
        marker_sum += number_array[(zero_index + marker) % len(number_array)][0]
    
    return marker_sum

def parse_data(path):
    with open(path) as f:
        data = f.read().split("\n")

    return list(map(int, data))

def tests():
    test1_exp = 3
    test2_exp = 1623178306

    data = parse_data("day-20\\test_input.txt")
    test1_res = gps_decrypt(data, 1, 1)
    test2_res = gps_decrypt(data, 10, 811589153)

    assert test1_res == test1_exp, f"{test1_res}, should be {test1_exp}"
    assert test2_res == test2_exp, f"{test2_res}, should be {test2_exp}"

    print("Tests passed")

def puzzle():
    data = parse_data("day-20\\input.txt")
    answer1 = gps_decrypt(data, 1, 1)
    answer2 = gps_decrypt(data, 10, 811589153)

    print(f"Part 1 -> : {answer1}")
    print(f"Part 2 -> : {answer2}")

tests()
puzzle()