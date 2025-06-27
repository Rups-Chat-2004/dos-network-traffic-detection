from scapy.all import sniff, wrpcap

def capture_packets(count=100, filename="network_traffic.pcap"):
    """
    Captures live network packets and saves them to a PCAP file.
    :param count: Number of packets to capture
    :param filename: File to save packets
    """
    packets = sniff(count=count)  # Capture 'count' number of packets
    wrpcap(filename, packets)  # Save packets to a PCAP file
    print(f"Captured {count} packets and saved to {filename}")

capture_packets()

