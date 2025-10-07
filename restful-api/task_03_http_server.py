#!/usr/bin/env python3
import http.server
import json


class handler_get(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            my_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            my_data_str = json.dumps(my_data).encode("utf-8")
            self.wfile.write(my_data_str)

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            my_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            my_data_str = json.dumps(my_data).encode("utf-8")
            self.wfile.write(my_data_str)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            text = "OK"
            body = text.encode("utf-8")
            self.wfile.write(body)

        elif self.path == "/":
            text = "Hello, this is a simple API!"
            body = text.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            text = "Endpoint not found"
            body = text.encode("utf-8")
            self.wfile.write(body)

if __name__ == "__main__":
    PORT = 8000
    server = http.server.HTTPServer(("localhost", PORT), handler_get)
    server.serve_forever()