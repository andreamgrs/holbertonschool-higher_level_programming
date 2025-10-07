#!/usr/bin/env python3
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler # a simple HTTP request handler that serves files from the current directory and any of its subdirectories.

# initiate a TCP server
# PORT stores the value of 8080
# server will be listening on incoming requests on that port, empty string for IP address so server will listen any network interface toas las IP 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever() # method on the TCPServer instance that starts the server and begins listening and responding to incoming requests