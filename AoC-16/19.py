from collections import deque

def simple_circle(elf_count):
    circle = deque([i + 1 for i in range(elf_count)])

    while len(circle) > 1:
        circle.append(circle.popleft())
        circle.popleft()

    return circle[0]

def complex_circle(elf_count):
    if elf_count % 2 != 0:
        raise(Exception("Yah dun doofed"))

    circle = deque([(i + elf_count // 2) % elf_count + 1 for i in range(elf_count)])

    while True:
        circle.popleft()
        if len(circle) == 1:
            return circle[0]
        circle.popleft()
        circle.append(circle.popleft())

with open("input\\19.txt") as f:
    elf_count = int(f.read())

print(f"Winner Simple: {simple_circle(elf_count)}")
print(f"Winner Complex: {complex_circle(elf_count)}")