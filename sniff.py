from scapy.all import sniff, Dot11

def packet_handler(packet):
    if packet.haslayer(Dot11):
        print(f"Packet: {packet.summary()}")

sniff(iface="wlp2s0mon", prn=packet_handler)
