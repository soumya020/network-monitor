import tkinter as tk
from tkinter import ttk, filedialog
from scapy.all import sniff, IP, TCP, UDP, ICMP
import threading
import csv

captured_packets = []
running = False


# GUI Window
root = tk.Tk()
root.title("Network Monitoring Tool")
root.geometry("700x400")


# TABLE
columns = ("Source IP", "Destination IP", "Protocol", "Port")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True)


# Row Colors
tree.tag_configure("tcp", background="#d4f7d4")
tree.tag_configure("udp", background="#d4e4f7")
tree.tag_configure("icmp", background="#f7efd4")


def process_packet(packet):

    src = "-"
    dst = "-"
    protocol = "-"
    port = "-"
    tag = ""

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        if packet.haslayer(TCP):
            protocol = "TCP"
            port = packet[TCP].dport
            tag = "tcp"

        elif packet.haslayer(UDP):
            protocol = "UDP"
            port = packet[UDP].dport
            tag = "udp"

        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            tag = "icmp"

        tree.insert("", "end", values=(src, dst, protocol, port), tags=(tag,))
        captured_packets.append([src, dst, protocol, port])


def sniff_packets():
    sniff(prn=process_packet, store=False, stop_filter=lambda x: not running)


def start_capture():
    global running
    running = True
    thread = threading.Thread(target=sniff_packets)
    thread.daemon = True
    thread.start()


def stop_capture():
    global running
    running = False


def save_csv():

    file = filedialog.asksaveasfilename(defaultextension=".csv")

    if file:
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Source IP","Destination IP","Protocol","Port"])
            writer.writerows(captured_packets)


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame,text="Start Capture",command=start_capture,bg="green",fg="white").grid(row=0,column=0,padx=10)

tk.Button(button_frame,text="Stop Capture",command=stop_capture,bg="red",fg="white").grid(row=0,column=1,padx=10)

tk.Button(button_frame,text="Save Data",command=save_csv).grid(row=0,column=2,padx=10)


root.mainloop()
