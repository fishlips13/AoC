from collections import deque
from math import prod

class CupsLooping:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            
    def __init__(self, values):
        self.nodes = []
        self.lookup = {}
        self.current = None
        self.current_iter = None
        self.iter_count = 0

        node_prev = None
        for value in values:
            node_new = self.Node(value)
            self.lookup[value] = node_new
            if node_prev:
                node_prev.next = node_new
            self.nodes.append(node_new)
            node_prev = node_new

        self.current = self.nodes[0]
        node_new.next = self.current
        self.highest = max(values)

    def __iter__(self):
        self.current_iter = self.current
        self.iter_remain = len(self.nodes)
        return self

    def __next__(self):
        if self.iter_remain:
            ret = self.current_iter
            self.current_iter = self.current_iter.next
            self.iter_remain -= 1
            return ret
        raise StopIteration

    def labels_after_without_1(self):
        good_values = {i for i in range(2, 10)}
        temp = self.current
        self.current = self.lookup[1]
        ret_str = "".join([str(i.value) for i in self if i.value in good_values])
        self.current = temp
        return ret_str

    def star_locations_product(self):
        node = self.lookup[1]
        return node.next.value * node.next.next.value

    def play_round(self):
        removed = (self.current.next.value,
                   self.current.next.next.value,
                   self.current.next.next.next.value)

        destination = self.current.value - 1
        while destination == 0 or destination in removed:
            destination -= 1
            if destination <= 0:
                destination = self.highest

        dest_node = self.lookup[destination]
        dest_next_old = dest_node.next

        first3 = self.current.next
        last3 = self.current.next.next.next

        self.current.next = last3.next
        dest_node.next = first3
        last3.next = dest_next_old

        self.current = self.current.next

def play_game(cups_list, cup_count, move_count):
    cups_list.extend([i for i in range(len(cups_list)+1, cup_count+1)])
    cups_loop = CupsLooping(cups_list)

    for _ in range(move_count):
        cups_loop.play_round()
    
    return cups_loop

with open("input/23.txt") as f:
    data = f.read()

cups_list = [int(i) for i in data]

game1 = play_game(cups_list, 9, 100)
print(f"Cup Labels: {game1.labels_after_without_1()}")

game2 = play_game(cups_list, 1000000, 10000000)
print(f"Star Locations Product: {game2.star_locations_product()}")