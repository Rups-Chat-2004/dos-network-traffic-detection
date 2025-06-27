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

 `capture_packets.py` - Captures live packets and saves to `.pcap`. 
 `process_pcap.py` - Processes `.pcap` file to extract IP-based features. 
 `network_features.csv` - Feature-extracted CSV file. 
 `DoS_Detection.ipynb` - Colab notebook for processing and analyzing the CSV. 
 `requirements.txt` - Python dependencies. 

##  Installation

1. Clone the repo or download the ZIP
   ```bash
   git clone https://github.com/your-username/DoS-Network-Traffic-Detection.git
   cd DoS-Network-Traffic-Detection

##  Results

![Packet Length Distribution](https://github.com/user-attachments/assets/9ce1dc72-0d7e-4da2-9168-072256de6747)


![Classification Report](https://github.com/user-attachments/assets/b45cfdbd-c15f-4afc-8093-21f9caac20bf)


![Confusion Matrix](https://github.com/user-attachments/assets/10cc9f46-62b9-44df-8da6-0b17d23677ba)
