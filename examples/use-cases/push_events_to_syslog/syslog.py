import os
import socketserver

HOST = os.getenv("HOST") or "0.0.0.0"
PORT = int(os.getenv("PORT")) or 514
class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = bytes.decode(self.request[0].strip())

        print(f"{data}")

try:
    print(f"Setting up a syslog to listen on: {HOST}:{PORT}")

    server = socketserver.UDPServer((HOST,PORT), UDPHandler)
    server.serve_forever(poll_interval=0.5)
except (IOError, SystemExit):
    raise
except KeyboardInterrupt:
    print ("Crtl+C Pressed. Shutting down.")
