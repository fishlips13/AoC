from copy import deepcopy
from collections import deque

class Intcode:
    
    original = []

    @staticmethod
    def setup():
        f = open("data.txt")
        Intcode.original = [int(i) for i in f.read().split(",")]
        f.close()

        diff = 10000 - len(Intcode.original)
        if diff > 0:
            Intcode.original.extend([0] * diff)

    def __init__(self):
        if not Intcode.original:
            Intcode.setup()

        self.d = deepcopy(Intcode.original)
        self.inp = None
        self.outp = None
        self.status = None
        self.it = self.run()
        next(self.it)

    def input_signal(self, a):
        self.inp = a
        next(self.it)

    def output_signal(self):
        outp_temp = self.outp
        next(self.it)
        return outp_temp

    def run(self):

        d = self.d
        i = 0
        r = 0

        while True:
            # Parse opcode
            o = []
            c = d[i]
            o.append(c % 100)
            c //= 100
            o.append(c % 10)
            c //= 10
            o.append(c % 10)
            o.append(c // 10)

            if o[0] == 99: # HCF
                self.status = "halted"
                while True:
                    yield self.status
                    raise Exception("intcode computer halted")

            # Assign parameter values
            p = [0,0,0]

            if o[0] == 3:
                if o[1] == 0:
                    p[0] = d[i+1]
                elif o[1] == 1:
                    raise Exception("Parameter 1 invalid mode")
                elif o[1] == 2:
                    p[0] = d[i+1] + r
            else:
                if o[1] == 0:
                    p[0] = d[d[i+1]]
                elif o[1] == 1:
                    p[0] = d[i+1]
                elif o[1] == 2:
                    p[0] = d[d[i+1] + r]

            if o[0] == 1 or o[0] == 2 or o[0] == 5 or o[0] == 6 or o[0] == 7 or o[0] == 8:
                if o[2] == 0:
                    p[1] = d[d[i+2]]
                elif o[2] == 1:
                    p[1] = d[i+2]
                elif o[2] == 2:
                    p[1] = d[d[i+2] + r]

            if o[0] == 1 or o[0] == 2 or o[0] == 7 or o[0] == 8:
                if o[3] == 0:
                    p[2] = d[i+3]
                elif o[3] == 1:
                    raise Exception("Parameter 3 invalid mode")
                elif o[3] == 2:
                    p[2] = d[i+3] + r

            # Select action by opcode
            if o[0] == 1:
                d[p[2]] = p[0] + p[1] # Add
                i += 4

            elif o[0] == 2:
                d[p[2]] = p[0] * p[1] # Mult
                i += 4

            elif o[0] == 3:
                self.status = "awaiting input"
                yield self.status
                d[p[0]] = self.inp # Input
                i += 2

            elif o[0] == 4:
                self.outp = p[0] # Output
                self.status = "awaiting output"
                yield self.status
                i += 2

            elif o[0] == 5:
                if p[0] != 0: # Jump !=
                    i = p[1]
                else:
                    i += 3

            elif o[0] == 6:
                if p[0] == 0: # Jump ==
                    i = p[1]
                else:
                    i += 3

            elif o[0] == 7:
                if p[0] < p[1]: # Test <
                    d[p[2]] = 1
                else:
                    d[p[2]] = 0
                i += 4

            elif o[0] == 8:
                if p[0] == p[1]: # Test ==
                    d[p[2]] = 1
                else:
                    d[p[2]] = 0
                i += 4
            
            elif o[0] == 9: # Relative base
                r += p[0]
                i += 2

            else:
                raise Exception("Bad command i: %d  -  o[0]: %d" % (i, o[0])) # Oops

class ASCII_Computer:

    def __init__(self, input_first = False):
        self.intcode_program = Intcode()
        self.print_output = True
        self.output_queue = deque()

        status = self.intcode_program.status
        if status == "halted" \
            or status == "awaiting output" and input_first == "input" \
            or status == "awaiting input" and input_first == "output":
            raise Exception("Invalid ASCII computer mode.")
        
        self._run()

    def input_cmd(self, cmd):
        if not cmd or type(cmd) is not str:
            raise Exception("Invalid ASCII input.")

        if cmd[-1] != "\n":
            cmd += "\n"

        self._run(cmd)

    def output_cmd(self):
        return "".join(self.output_queue)

    def _run(self, line = ""):
        if self.intcode_program.status == "awaiting input":
            for letter in line:
                self.intcode_program.input_signal(ord(letter))
        elif self.intcode_program.status == "halted":
            print("ASCII computer halted.")
            return

        self.output_queue.clear()
        output = []
        while self.intcode_program.status == "awaiting output":
            val = self.intcode_program.output_signal()
            
            if val >= 256:
                print(val)
                break
            
            output.append(chr(val))
            if output[-1] == "\n":
                self.output_queue.append("".join(output[:-1]))
                if self.print_output:
                    print("".join(output[:-1]))
                output = []