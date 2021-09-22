import http.server
import socketserver

PORT = 8080

class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # def __init__(self, message, subtitle):
    #     self.message = message
    #     self.subtitle = subtitle

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        payload = '<h1>message</h1>'
        self.wfile.write(payload.encode('utf-8'))


with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()