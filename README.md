# DoS Network Traffic Detection

This project captures real-time network packets, extracts essential features, and detects potential Denial-of-Service (DoS) attacks using packet-level data analysis.

##  Overview

- Packets are captured on a Linux terminal using Scapy.
- Extracted features are stored in CSV format.
- A Google Colab notebook processes the CSV to detect anomalies (DoS).

##  Dataset Source

The dataset (`network_features.csv`) was captured directly from the Linux terminal using Scapy and processed in Google Colab.

##  Tools & Libraries

- Python
- Scapy
- Pandas
- Google Colab
- IPython / Jupyter
- CSV / PCAP formats

##  File Descriptions

- `capture_packets.py` – Captures live network packets using Scapy and saves them to a `.pcap` file.  
- `process_pcap.py` – Extracts features (source IP, destination IP, protocol, packet length) from the `.pcap` file and stores them in a `.csv`.  
- `network_traffic.pcap` – Contains raw packet data captured from the network interface.  
- `network_features.csv` – Stores the processed network traffic features in tabular format.  
- `DoS_Detection.ipynb` – Google Colab notebook that loads the CSV, analyzes traffic patterns, and detects potential DoS attacks.  
- `requirements.txt` – Lists Python dependencies required to run the Python scripts.  

##  Installation

1. Clone the repo or download the ZIP
   ```bash
   git clone https://github.com/your-username/DoS-Network-Traffic-Detection.git
   cd DoS-Network-Traffic-Detection

##  Results

![Packet Length Distribution](https://github.com/user-attachments/assets/9ce1dc72-0d7e-4da2-9168-072256de6747)


![Classification Report](https://github.com/user-attachments/assets/b45cfdbd-c15f-4afc-8093-21f9caac20bf)


![Confusion Matrix](https://github.com/user-attachments/assets/10cc9f46-62b9-44df-8da6-0b17d23677ba)
