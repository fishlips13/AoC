from itertools import permutations
from intcode import Intcode

high = -999999999999999999999999999999999999

p = permutations(range(5,10))

for i in p:
    a = Intcode()
    b = Intcode()
    c = Intcode()
    d = Intcode()
    e = Intcode()

    a.input_signal(i[0])
    b.input_signal(i[1])
    c.input_signal(i[2])
    d.input_signal(i[3])
    e.input_signal(i[4])

    outE = 0

    while a.status != "halted":        
        a.input_signal(outE)
        outA = a.output_signal()

        b.input_signal(outA)
        outB = b.output_signal()

        c.input_signal(outB)
        outC = c.output_signal()

        d.input_signal(outC)
        outD = d.output_signal()

        e.input_signal(outD)
        outE = e.output_signal()

        high = max(high, outE)

print(high)