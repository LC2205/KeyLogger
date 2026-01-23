# KeyLogger
Keylogger made in python to keep track of keyboard presses, and links of websites visited

# DISCLAIMER
Use of this program for malicious intents or purposes do not fall under my responsibility as this project is purely for educational purposes, I do not condone the use of keyloggers to retrieve sensitive data from unsuspecting victims.

# How it's done:
The keylogger uses the Keyboard library in python to simply record the registered inputs and send over a record of them over a minute to an HTTP server to be saved to a .txt file.
The HTTP server runs on the http library on python to handle any POST requests sent from the logging "target" for either "/key" or "/pcap" depending on the data being provided.
The pcap storing and processing is done using the pycap and pyshark libraries to listen for traffic on the "target" and allow for the processing to be done at the server, into another .txt file
