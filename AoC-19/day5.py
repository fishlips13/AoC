d = []
f = open("data.txt")
d = [int(i) for i in f.read().split(",")]
f.close()

diag = 5

i = 0
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
        break

    # Assign parameter values
    p = [0,0,0]

    if o[0] == 3:
        p[0] = d[i+1]
    else:
        if o[1] == 0:
            p[0] = d[d[i+1]]
        else:
            p[0] = d[i+1]

    if o[0] == 1 or o[0] == 2 or o[0] == 5 or o[0] == 6 or o[0] == 7 or o[0] == 8:
        if o[2] == 0:
            p[1] = d[d[i+2]]
        else:
            p[1] = d[i+2]

    if o[0] == 1 or o[0] == 2 or o[0] == 7 or o[0] == 8:
        p[2] = d[i+3]

    # Select action by opcode
    if o[0] == 1:
        d[p[2]] = p[0] + p[1] # Add
        i += 4

    elif o[0] == 2:
        d[p[2]] = p[0] * p[1] # Mult
        i += 4

    elif o[0] == 3:
        d[p[0]] = diag # Input
        i += 2

    elif o[0] == 4:
        print(p[0]) # Output
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

    else:
        raise(Exception("Bad command i: %d  -  o[0]: %d" % (i, o[0]))) # Oops