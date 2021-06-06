def pattern_gen(length):
    while True:
        for _ in range(length):
            yield 0
        for _ in range(length):
            yield 1
        for _ in range(length):
            yield 0
        for _ in range(length):
            yield -1

f = open("data.txt")
data = f.read()
f.close()

signal = [int(i) for i in data] * 10000
offset = int(data[:7])
signal = signal[offset:]

for _ in range(100):
    signal_it = reversed(signal)
    final = [next(signal_it)]

    for i in signal_it:
        final.append((final[-1] + i) % 10)
    signal = final[::-1]

result = signal[:8]

print("".join([str(i) for i in result]))

quit()

for _ in range(100):
    old = signal[:]
    
    for i in range(len(old)):
        pattern = pattern_gen(i + 1)
        next(pattern)

        result = 0
        for j in old:
            pattern_val = next(pattern)
            if not pattern_val:
                continue

            result += j * pattern_val
        
        signal[i] = abs(result) % 10

print("".join([str(i) for i in signal[:8]]))