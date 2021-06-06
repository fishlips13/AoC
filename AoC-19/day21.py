import intcode

f = open("droid_program.spsc")
data = f.read().split("\n")
f.close()

droid = intcode.ASCII_Computer()

for item in data:
    if item[0] != "#" or item[0] != "\n":
        droid.input_cmd(item.strip())