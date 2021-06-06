from intcode import Intcode

a = Intcode()
a.input_signal(2)
c = []

while a.status != "halted":
    c.append(a.output_signal())

print(c)