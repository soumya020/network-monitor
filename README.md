# network-monitor
A GUI-based network packet monitoring tool built with Python

Network Monitoring Tool:- 
A lightweight, GUI-based network packet sniffer built with Python. Capture, view, and export live network traffic in real time.

✨ Features

📡 Live packet capture — sniff TCP, UDP, and ICMP packets in real time
🎨 Color-coded display — instantly distinguish protocols at a glance
📋 Tabular view — see Source IP, Destination IP, Protocol, and Port
💾 Export to CSV — save captured packets for later analysis
🛑 Start / Stop control — full control over capture sessions


🚀 Getting Started
Prerequisites

Python 3.x
scapy library (for packet sniffing)
tkinter (usually built into Python)
Run as Administrator / root (required for packet sniffing)

Installation
bash# 1. Clone the repository
git clone https://github.com/soumya020/network-monitor.git
cd network-monitor

# 2. Install dependencies
scapy>=2.5.0

# 3. Run the tool (as admin/root)
# On Windows (run terminal as Administrator):
python network_monitor.py

# On Linux/Mac:
sudo python3 network_monitor.py

📖 How to Use

Launch the app (with admin/root privileges)
Click Start Capture to begin sniffing packets
Watch live traffic appear in the table, color-coded by protocol:

🟢 Green → TCP
🔵 Blue → UDP
🟡 Yellow → ICMP


Click Stop Capture to pause
Click Save Data to export captured packets as a .csv file


📁 Project Structure
network-monitor/
│
└── network_monitor.py   # Main application file

🛠️ Built With

Python — Core language
Scapy — Packet capture and analysis
Tkinter — GUI framework


⚠️ Disclaimer
This tool is intended for educational and ethical use only. Only monitor networks you own or have explicit permission to monitor.
