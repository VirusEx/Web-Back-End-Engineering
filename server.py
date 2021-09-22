#!/usr/bin/env python3

# Example HTTP server
#
# See <https://docs.python.org/3/library/http.server.html> for details
#

import http.server
import socketserver

PORT = 8080


class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        payload = '<h1>Hello, world</h1>'
        self.wfile.write(payload.encode('utf-8'))


with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()