"""Run a minimal HTTP API using the Python standard library."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests and return a JSON response."""
        if self.path == "/health":
            self.send_json(200, {"status": "ok"})
        else:
            self.send_json(404, {"error": "not found"})

    def send_json(self, status_code, payload):
        """Send a status code and a JSON body."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), APIHandler)
    print("API running at http://127.0.0.1:8000 (press Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping API.")
    finally:
        server.server_close()
