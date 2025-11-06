#!/usr/bin/env python3
"""
Simple HTTP Server
Serves files from the current directory.
Usage: python simple_server.py [port]
"""

import sys
import http.server
import socketserver

def start_server(port=8000):
    """Start a simple HTTP server."""
    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

def main():
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number.")
            sys.exit(1)
    start_server(port)

if __name__ == "__main__":
    main()