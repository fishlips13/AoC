class Gate:
    def __init__(self, input1, op, input2, output):
        self.input1 = fix_int_str(input1)
        self.op = op
        self.input2 = fix_int_str(input2)
        self.output = output

    def is_resolvable(self, wires):
        return (self.input1 == None or self.input1 in wires or type(self.input1) == int) and \
                                      (self.input2 in wires or type(self.input2) == int)

    def resolve_gate(self, wires):
        value1 = wires[self.input1] if self.input1 in wires else self.input1
        value2 = wires[self.input2] if self.input2 in wires else self.input2

        if not self.op:
            result = value2
        elif self.op == "AND":
            result = value1 & value2
        elif self.op == "OR":
            result = value1 | value2
        elif self.op == "NOT":
            result = ~ value2
        elif self.op == "LSHIFT":
            result = value1 << value2
        elif self.op == "RSHIFT":
            result = value1 >> value2

        while result < 0:
            result += 65536
        result %= 65536

        return result

def fix_int_str(string):
    if not string:
        return string
    try:
        return int(string)
    except ValueError:
        return string

def resolve_system(gates, end_wire):
    wires = {}
    while end_wire not in wires:
        for gate in gates:
            if gate.output not in wires and gate.is_resolvable(wires):
                wires[gate.output] = gate.resolve_gate(wires)
    return wires

with open("input/07.txt") as f:
    data = [[j for j in i.split(" ") if j != "->"] for i in f.read().split("\n")]

gates = {}
for part in data:
    if len(part) == 2:
        part.insert(0, None)
        part.insert(0, None)
    if len(part) == 3:
        part.insert(0, None)
    
    gate = Gate(*part)
    gates[gate.output] = gate

wires = resolve_system(gates.values(), "a")

a_signal1 = wires["a"]
gates["b"].input2 = a_signal1

wires = resolve_system(gates.values(), "a")
a_signal2 = wires["a"]

print(f"\'a\' First Signal: {a_signal1}")
print(f"\'a\' Second Signal: {a_signal2}")