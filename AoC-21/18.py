from math import ceil, floor
from itertools import permutations
from copy import deepcopy

class Numb:
    def __init__(self, value) -> None:
        self.value = value

class Snumb:
    def __init__(self, snumb_str:str) -> None:
        self.numbs = []

        stack = []
        for value in snumb_str:
            if value == "," or value == "[":
                continue
            elif value == "]":
                temp = stack.pop()
                stack.append([stack.pop(), temp])
            elif value.isdigit():
                numb = Numb(int(value))
                stack.append(numb)
                self.numbs.append(numb)
        
        self.value = stack[0]

    def __add__(self, other:"Snumb"):
        self.value = [self.value, other.value]
        self.numbs.extend(other.numbs)
        self.reduce()
        return self
    
    def __radd__(self, other):
        if isinstance(other, int):
            return self
        return self.__add__(other)

    def __str__(self) -> str:
        return Snumb.__snumb_str(self.value)

    def reduce(self):
        while True:
            self.value, _ = Snumb.__explode(self.value, self.numbs)
            _, splitted = Snumb.__split(self.value, self.numbs)
            if not splitted:
                break

    def magnitude(self):
        return self.__snumb_mag(self.value)

    @classmethod
    def __snumb_mag(cls, snumb:list):
        if isinstance(snumb, Numb):
            return snumb.value

        return 3 * cls.__snumb_mag(snumb[0]) + 2 * cls.__snumb_mag(snumb[1])

    @classmethod
    def __snumb_str(cls, snumb:list):
        if isinstance(snumb, Numb):
            return snumb.value

        return f"[{cls.__snumb_str(snumb[0])},{Snumb.__snumb_str(snumb[1])}]"
        
    @classmethod
    def __explode(cls, snumb:list, numbs:list, depth = 0, i = 0):
        new_snumb = []

        for sub_snumb in snumb:
            if isinstance(sub_snumb, Numb):
                new_snumb.append(sub_snumb)
                i += 1
            else:
                result, i = cls.__explode(sub_snumb, numbs, depth + 1, i)
                new_snumb.append(result)
        
        if depth == 4 and isinstance(new_snumb[0], Numb) and isinstance(new_snumb[1], Numb):
            i_left = i - 3
            if i_left >= 0:
                numbs[i_left].value += new_snumb[0].value

            i_right = i
            if i_right < len(numbs):
                numbs[i_right].value += new_snumb[1].value

            numbs[i-2] = Numb(0)
            del numbs[i-1]

            return numbs[i-2], i - 1
        
        return new_snumb, i

    @classmethod
    def __split(cls, snumb:list, numbs:list, i = 0):

        splitted = False
        for j, sub_snumb in enumerate(snumb):
            if isinstance(sub_snumb, Numb):
                i += 1
                if sub_snumb.value >= 10:
                    numb_left = Numb(floor(sub_snumb.value / 2))
                    sub_snumb.value = ceil(sub_snumb.value / 2)
                    numbs.insert(i - 1, numb_left)
                    snumb[j] = [numb_left, sub_snumb]
                    return i, True
            else:
                i, splitted = cls.__split(sub_snumb, numbs, i)
                if splitted:
                    return i, True
        
        return i, splitted

with open("input\\18.txt") as f:
    data = f.read().split("\n")

snumbs = [Snumb(i) for i in data]
snumb_sum = sum(deepcopy(snumbs))
mag_max = max([(deepcopy(i) + deepcopy(j)).magnitude() for i, j in permutations(snumbs, 2)])

print(f"Snail Sum Magnitude: {snumb_sum.magnitude()}")
print(f"Snail Max Magnitude: {mag_max}")

# Terrible class memory overwriting. Yuck