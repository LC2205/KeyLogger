# KeyLogger
Keylogger made in python to keep track of keyboard presses, and links of websites visited, then being exfiltrated to an (assumed to be) external server for logging

# DISCLAIMER
Use of this program for malicious intents or purposes do not fall under my responsibility as this project is purely for educational purposes, I do not condone the use of keyloggers to retrieve sensitive data from unsuspecting victims.

# How it's done:
The keylogger uses the Keyboard library in python to simply record the registered inputs and send over a record of them over a given time period to an HTTP server to be saved to a .txt file.
The HTTP server runs on the http library on python to handle any POST requests sent from the logging "target" for either "/key" or "/pcap" depending on the data being provided.
The pcap storing and processing is done using the pyshark library to listen for traffic on the "target" and allow for the processing to be done at the server, into another .txt file

# Usage
If you would like to use this, ensure you have all libraries installed and feel free to modify sections of the code for it to work differently/more efficiently, constructive criticism is appreciated.
If you are wanting to attempt to use this through external networks rather than sending to the localhost server like I did for testing, look into port forwarding on your router and modify the server variable to contain your own IP address to send to
WARNING FOR THE ABOVE: Do not do this to any network that you do not have permission to test on, it is illegal to perform packet sniffing unauthorised and that is what this will do. Also keep in mind that if you do share your IP onto the code for it to run there is the possibility of it being found and you will not be having much fun if it is found by someone knowledgeable.
