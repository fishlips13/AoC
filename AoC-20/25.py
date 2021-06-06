with open("input/25.txt") as f:
    data = f.read().split("\n")

enc_key1 = int(data[0])
enc_key2 = int(data[1])

def find_loop_size(enc_key):
    current = 1
    loop_size = 0
    while current != enc_key:
        current = (current * 7) % 20201227
        loop_size += 1
    return loop_size

def transform(subject, loop_size):
    current = 1
    for _ in range(loop_size):
        current = (current * subject) % 20201227
    return current

loop_size1 = find_loop_size(enc_key1)
loop_size2 = find_loop_size(enc_key2)

handshake_key1 = transform(enc_key1, loop_size2)
handshake_key2 = transform(enc_key2, loop_size1)

print(f"Handshake Key: {handshake_key1} ({handshake_key2})")