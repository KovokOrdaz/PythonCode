import netfilterqueue


def process_packet(packet):
    print(packet)
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


# iptables -I FORWARD -j NFQUEUE --queue-num 0
# echo 1 > /proc/sys/net/ipv4/ip_forward
