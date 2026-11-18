#!/usr/bin/env python3
"""Local development server for the Bunga Telang site.

Usage:
    py server.py            # http://localhost:8000
    py server.py 3000       # http://localhost:3000
    py server.py 3000 --no-open
"""

import argparse
import functools
import http.server
import socket
import socketserver
import sys
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
        ".woff2": "font/woff2",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stdout.write("  %s\n" % (fmt % args))

    def do_GET(self):
        if self.path in ("/", ""):
            self.path = "/index.html"
        super().do_GET()


def find_port(host, preferred):
    for port in range(preferred, preferred + 25):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                probe.bind((host, port))
            except OSError:
                continue
        return port
    raise SystemExit(f"No free port found in range {preferred}-{preferred + 24}.")


def main():
    parser = argparse.ArgumentParser(description="Serve the Bunga Telang site locally.")
    parser.add_argument("port", nargs="?", type=int, default=DEFAULT_PORT)
    parser.add_argument("--host", default="127.0.0.1", help="bind address (use 0.0.0.0 to share on your LAN)")
    parser.add_argument("--no-open", action="store_true", help="do not open the browser")
    args = parser.parse_args()

    port = find_port(args.host, args.port)
    handler = functools.partial(Handler, directory=str(ROOT))

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.ThreadingTCPServer((args.host, port), handler) as httpd:
            url = f"http://localhost:{port}/"
            print(f"\n  Bunga Telang server running")
            print(f"  -> {url}")
            print(f"  serving {ROOT}")
            print("  Ctrl+C to stop\n")
            if not args.no_open:
                threading.Timer(0.5, webbrowser.open, args=[url]).start()
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
    except OSError as exc:
        raise SystemExit(f"Could not start server: {exc}")


if __name__ == "__main__":
    main()
