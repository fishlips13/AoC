o = []

f = open("data.txt")
o = [int(i) for i in f.read().split(",")]
f.close()

t = 19690720
a = ()

for n in range(0, 100):
    for v in range(0, 100):
        d = o[:]
        d[1] = n
        d[2] = v

        i = 0
        while d[i] != 99:
            if d[i] == 1:
                d[d[i+3]] = d[d[i+1]] + d[d[i+2]]
            elif d[i] == 2:
                d[d[i+3]] = d[d[i+1]] * d[d[i+2]]
            else:
                raise(Exception("Bad command n: %d  -  v: %d" % (n, v)))
            
            i += 4
        
        if d[0] == t:
            a = (n, v)
        
    if a:
        break

print(str(100 * a[0] + a[1]))