from math import prod

class Packet:
    def __init__(self) -> None:
        self.version = 0
        self.type_ID = 0
        self.literal_value = None
        self.sub_packets = []

def evaluate(packet:Packet) -> int:
    if packet.type_ID == 4:
        return packet.literal_value

    sub_values = [evaluate(i) for i in packet.sub_packets]
    if packet.type_ID == 0:
        return sum(sub_values)
    elif packet.type_ID == 1:
        return prod(sub_values)
    elif packet.type_ID == 2:
        return min(sub_values)
    elif packet.type_ID == 3:
        return max(sub_values)
    elif packet.type_ID == 5:
        return 1 if sub_values[0] > sub_values[1] else 0
    elif packet.type_ID == 6:
        return 1 if sub_values[0] < sub_values[1] else 0
    elif packet.type_ID == 7:
        return 1 if sub_values[0] == sub_values[1] else 0

def version_total(packet:Packet) -> int:
    return packet.version + sum([version_total(i) for i in packet.sub_packets])

def bin_str_to_int(bin_str) -> int:
    return int(bin_str, 2)

def build_packet(raw_bin, i_start = 0) -> tuple[Packet, int]:
    packet = Packet()
    i = i_start
    while i < len(raw_bin):
        packet.version = bin_str_to_int(raw_bin[i:i+3])
        packet.type_ID = bin_str_to_int(raw_bin[i+3:i+6])

        i += 6
        if packet.type_ID == 4:
            literal_bin = ""

            while raw_bin[i] != "0":
                literal_bin += raw_bin[i+1:i+5]
                i += 5

            literal_bin += raw_bin[i+1:i+5]
            i += 5

            packet.literal_value = bin_str_to_int(literal_bin)
            break
        else:
            if raw_bin[i] == "0":
                sub_length = bin_str_to_int(raw_bin[i+1:i+16])
                i += 16

                i_final = i + sub_length
                while i < i_final:
                    sub_packet, i_new = build_packet(raw_bin, i)
                    packet.sub_packets.append(sub_packet)
                    i = i_new

                break
            else:
                sub_count = bin_str_to_int(raw_bin[i+1:i+12])
                i += 12

                for _ in range(sub_count):
                    sub_packet, i_new = build_packet(raw_bin, i)
                    packet.sub_packets.append(sub_packet)
                    i = i_new

                break
    
    return packet, i

with open("input\\16.txt") as f:
    data = f.read()

data_bin = ""
for i in data:
    data_bin += bin(int(i, 16))[2:].zfill(4)

packet, _ = build_packet(data_bin)

print(f"Version Total: {version_total(packet)}")
print(f"Packet Evaluated: {evaluate(packet)}")