#!/usr/bin/python
import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer


try:
    PORT_NUMBER = int(os.environ['PORT_NUMBER'])
except:
    PORT_NUMBER = 80;

class demoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("I'm listening on port {}.".format(PORT_NUMBER))
        return

server = HTTPServer(('', PORT_NUMBER), demoHandler)
print "Started webserver on port {}.".format(PORT_NUMBER)
server.serve_forever()


