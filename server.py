#!/usr/bin/env python3

# Example HTTP server
#
# See <https://docs.python.org/3/library/http.server.html> for details
#

import http.server
import socketserver
from redact import redacted_message
import sys

[message, subtitle] = redacted_message()

PORT = 8080
class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith(sys.argv[1]):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()

            # message = "Why? Because fuck you, that's why!! "
            # subtitle = "- ProfAvery"
            payload = f"""
            <html>
                <head> 
                    <title>FOAAS - Why? Because fuck you, that's why. - ProfAvery</title> 
                    <meta charset="utf-8"> <meta property="og:title" content="Why? Because fuck you, that's why. - ProfAvery"> 
                    <meta property="og:description" content="Why? Because fuck you, that's why. - ProfAvery"> 
                    <meta name="twitter:card" content="summary"> <meta name="twitter:site" content="@foaas"> 
                    <meta name="twitter:title" content="FOAAS: Fuck Off As A Service"> 
                    <meta name="twitter:description" content="Why? Because fuck you, that's why. - ProfAvery"> 
                    <meta name="viewport" content="width=device-width, initial-scale=1"> <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet"> 
                    <script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-143325008-1"></script> 
                    </head> 
                    <body style="margin-top:40px;" data-new-gr-c-s-check-loaded="14.994.0" data-gr-ext-installed="" data-gr-ext-disabled="forever"> 
                        <div class="container"> 
                            <div id="view-10"> 
                                <div class="hero-unit"> 
                                    <h1>{message} </h1> 
                                    <p>
                                    <em>{subtitle}</em>
                                    </p> 
                                </div> 
                            </div> 
                            <p style="text-align: center">
                                <a href="https://foaas.com">foaas.com</a>
                            </p> 
                        </div>  
                    </body>
            </html>

            """
            self.wfile.write(payload.encode('utf-8'))


with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()