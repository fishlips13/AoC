import re

def is_abba(value):
    for match in re.finditer(r"(.)(.)(?=\2\1)", value):
        if match.group(1) != match.group(2):
            return True
    return False
    
def get_babs(value):
    babs = set()
    for match in re.finditer(r"(.)(?=(.)\1)", value):
        if match.group(1) != match.group(2):
            babs.add("".join(match.group(2, 1, 2)))
    return babs

with open("input/07.txt") as f:
    data = f.read().split("\n")

tls_ips = 0
ssl_ips = 0
for line in data:
    supernets, hypernets = [], []

    i_first = 0
    for i in range(len(line)):
        if line[i] == "[":
            supernets.append(line[i_first:i])
            i_first = i + 1
        elif line[i] == "]":
            hypernets.append(line[i_first:i])
            i_first = i + 1

    supernets.append(line[i_first:])

    if any(is_abba(i) for i in supernets) and not any(is_abba(i) for i in hypernets):
        tls_ips += 1

    babs = set()
    for supernet in supernets:
        babs.update(get_babs(supernet))
    
    found_bab = False
    for bab in babs:
        for hypernet in hypernets:
            if bab in hypernet:
                found_bab = True

    if found_bab:
        ssl_ips += 1

print(f"TLS IPs: {tls_ips}")
print(f"SSL IPs: {ssl_ips}")