from scapy.all import rdpcap
import pandas as pd

# Load packets from the captured .pcap file
packets = rdpcap("network_traffic.pcap")

# Define a function to extract key features
def extract_features(packets):
    data = []
    
    for pkt in packets:
        if pkt.haslayer("IP"):  # Check if the packet has an IP layer
            data.append({
                "src_ip": pkt["IP"].src,  # Source IP address
                "dst_ip": pkt["IP"].dst,  # Destination IP address
                "protocol": pkt["IP"].proto,  # Protocol type (TCP/UDP/ICMP)
                "length": len(pkt)  # Packet length
            })
    
    return pd.DataFrame(data)

# Extract features
df = extract_features(packets)


