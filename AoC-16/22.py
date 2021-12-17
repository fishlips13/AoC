from os import stat
import re
from itertools import permutations
from queue import PriorityQueue
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: tuple
    item: Any=field(compare=False)

class Node:
    def __init__(self, x, y, size, used) -> None:
        self.coords = (x, y)
        self.size = size
        self.used = used
    
    def avail(self) -> int:
        return self.size - self.used

def valid_moves(nodes, adjacent_only = True):
    moves = []
    adjacents = {(0, 1), (1, 0), (0, -1), (-1, 0)}

    for orig, dest in permutations(nodes, 2):
        offset = (orig.coords[0] - dest.coords[0], orig.coords[1] - dest.coords[1])
        if orig.used != 0 and dest.avail() >= orig.used and \
            (not adjacent_only or offset in adjacents):
            moves.append((orig.coords, dest.coords))

    return moves

def heuristic(coord):
    return coord[0] + coord[1]

def build_state(nodes, goal_coords):
    states = {i.coords[0] + i.coords[1] * 100 : "." if i.used > 0 else "_" for i in nodes}
    states[goal_coords[0] + goal_coords[1] * 100] = "G"
    states_keys = list(states.keys())
    states_keys.sort()
    return "".join([states[i] for i in states_keys])

def fewest_steps(nodes_base, end):
    frontier = PriorityQueue()
    frontier.put(PrioritizedItem((0, 0), (deepcopy(nodes_base), end)))
    state_cache = set()

    while not frontier.empty():
        item = frontier.get()
        nodes, goal_curr = item.item
        move_count = item.priority[0] + 1
        print("yo")
        for coords_from, coords_to in valid_moves(nodes.values()):
            goal_new = goal_curr
            if coords_from == goal_new:
                if coords_to == (0, 0):
                    return move_count
                goal_new = coords_to

            nodes_new = deepcopy(nodes)
            nodes_new[coords_to].used += nodes_new[coords_from].used
            nodes_new[coords_from].used -= nodes_new[coords_to].used

            state = build_state(nodes_new.values(), goal_new)
            if state in state_cache:
                continue
            state_cache.add(state)

            frontier.put(PrioritizedItem((move_count, heuristic(goal_new)), (nodes_new, goal_new)))

with open("input\\22.txt") as f:
    data = [[j for j in map(int, re.findall(r"\d+", i))] for i in f.read().split("\n")[2:]]

nodes_base = {(i[0], i[1]) : Node(*i[:-2]) for i in data}
x_highest = max([i.coords[0] for i in nodes_base.values()])

#valid_pairs = sum([1 for _ in valid_moves(nodes_base.values(), False)])

#print(f"Valid Pairs: {valid_pairs}")
print(f"Fewest Steps: {fewest_steps(nodes_base, (x_highest, 0))}")