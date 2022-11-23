
def el_naive(inserts, step, sub):
    buffer = [0]

    i_current = 0
    for rep in range(1, inserts + 1):
        i_current = (i_current + step) % len(buffer) + 1
        buffer.insert(i_current, rep)

    return buffer[buffer.index(sub)+1]

def el_bruto(inserts, step, sub):

    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.next = None
            
    node_zero = Node(0)
    node_zero.next = node_zero
    lookup = {0 : node_zero}

    for rep in range(1, inserts + 1):
        node_new = Node(rep)
        node_prev = lookup[rep - 1]

        for _ in range(step):
            node_prev = node_prev.next

        node_new.next = node_prev.next
        node_prev.next = node_new

        lookup[rep] = node_new
        if rep % 1000000 == 0:
            print(rep // 1000000)

    return lookup[sub].next.value

def el_cheato(inserts, step):
    i_current = 0
    second = None

    for rep in range(1, inserts + 1):
        i_current = (i_current + step) % rep + 1
        if i_current == 1:
            second = rep
    
    return second

with open ("input\\17.txt") as f:
    data = int(f.read())

spin1 = 2017
spin2 = 50000000

print(f"Next value ({spin1}): {el_naive(spin1, data, spin1)}")
print(f"Next value ({spin2}): {el_cheato(spin2, data)}")