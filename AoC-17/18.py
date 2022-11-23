from copy import deepcopy
from collections import deque

def part1():
    cmds = []
    for line in data:
        cmds.append(parse_cmd(*line))

    regs = {}
    for _, arg1, __ in cmds:
        if isinstance(arg1, str) and arg1 not in regs:
            regs[arg1] = 0

    def run(cmds, regs):
        i = 0
        last_snd = None

        while i < len(cmds):
            if i < 0 or i >= len(cmds):
                print("Program out of command bounds. Exiting")
                return

            cmd, arg1, arg2 = cmds[i]
            if isinstance(arg1, str) and arg1 not in regs:
                regs[arg1] = 0
            
            if cmd == "snd":
                last_snd = regs[arg1]

            elif cmd == "set":
                if arg2 in regs:
                    regs[arg1] = regs[arg2]
                else:
                    regs[arg1] = arg2

            elif cmd == "add":
                regs[arg1] += regs[arg2] if arg2 in regs else arg2

            elif cmd == "mul":
                regs[arg1] *= regs[arg2] if arg2 in regs else arg2

            elif cmd == "mod":
                regs[arg1] %= regs[arg2] if arg2 in regs else arg2

            elif cmd == "rcv":
                value = regs[arg1] if arg1 in regs else arg1
                if value:
                    return last_snd

            elif cmd == "jgz":
                value1 = regs[arg1] if arg1 in regs else arg1
                value2 = regs[arg2] if arg2 in regs else arg2
                if value1 > 0:
                    i += value2 - 1

            i += 1
    
    print(f"Last Sound: {run(cmds, regs)}")

def part2():
    class Program:
        def __init__(self, id, data):
            self.cmds = []
            self.regs = {}
            self.inbound = deque()
            self.outbound = deque()
            self.run_it = self._run()

            for line in data:
                self.cmds.append(parse_cmd(*line))

            for _, arg1, __ in self.cmds:
                if isinstance(arg1, str) and arg1 not in self.regs:
                    self.regs[arg1] = 0

            self.regs["p"] = id
        
        def resume(self):
            next(self.run_it)

        def _run(self):
            i = 0

            while i < len(self.cmds):
                if i < 0 or i >= len(self.cmds):
                    print("Program out of command bounds. Exiting")
                    return

                cmd, arg1, arg2 = self.cmds[i]
                
                if cmd == "snd":
                    self.outbound.appendleft(self.regs[arg1])

                elif cmd == "set":
                    if arg2 in self.regs:
                        self.regs[arg1] = self.regs[arg2]
                    else:
                        self.regs[arg1] = arg2

                elif cmd == "add":
                    self.regs[arg1] += self.regs[arg2] if arg2 in self.regs else arg2

                elif cmd == "mul":
                    self.regs[arg1] *= self.regs[arg2] if arg2 in self.regs else arg2

                elif cmd == "mod":
                    self.regs[arg1] %= self.regs[arg2] if arg2 in self.regs else arg2

                elif cmd == "rcv":
                    while not self.inbound:
                        yield None
                    self.regs[arg1] = self.inbound.pop()

                elif cmd == "jgz":
                    value1 = self.regs[arg1] if arg1 in self.regs else arg1
                    value2 = self.regs[arg2] if arg2 in self.regs else arg2
                    if value1 > 0:
                        i += value2 - 1

                i += 1

    p0 = Program(0, data)
    p1 = Program(1, data)

    p1_sent = 0
    while True:
        p0.resume()
        p1.resume()

        while p0.outbound:
            p1.inbound.appendleft(p0.outbound.pop())
        
        while p1.outbound:
            p0.inbound.appendleft(p1.outbound.pop())
            p1_sent += 1

        if not p0.inbound and not p1.inbound:
            break

    print(f"Program 1 Sent: {p1_sent}")

def parse_cmd(cmd:str, arg1:str, arg2:str = None):
    arg1 = int(arg1) if arg1.lstrip("-").isdigit() else arg1
    if arg2:
        arg2 = int(arg2) if arg2.lstrip("-").isdigit() else arg2
    return (cmd, arg1, arg2)

with open("input\\18.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

part1()
part2()