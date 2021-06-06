from intcode import Intcode

network = []

for i in range(50):
    new_net_comp = Intcode()
    new_net_comp.input_signal(i)
    network.append(new_net_comp)
del new_net_comp
del i

packets = []
nat = None
last_nat_y = None


while True:
    for net_comp in network:
        if net_comp.status == "awaiting input":
            net_comp.input_signal(-1)

        while net_comp.status == "awaiting output":
            address = net_comp.output_signal()
            x = net_comp.output_signal()
            y = net_comp.output_signal()

            if address == 255:
                nat = (0, x, y)
            else:
                packets.append((address, x, y))
        
    if not packets:
        if last_nat_y and nat[2] == last_nat_y:
            print(last_nat_y)
            break
        packets.append(nat)
        last_nat_y = nat[2]
        
    delayed_packets = []
    while packets:
        packet = packets.pop()
        net_comp = network[packet[0]]

        if net_comp.status == "awaiting input":
            net_comp.input_signal(packet[1])
            net_comp.input_signal(packet[2])
        elif net_comp.status == "awaiting output":
            delayed_packets.append(packet)
    
    packets.extend(delayed_packets)