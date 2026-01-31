from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import requests
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "web")

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve files from web/
        rel = path.lstrip("/")
        return os.path.join(ROOT, rel or "index.html")

    def do_GET(self):
        if self.path.startswith("/api/"):
            target = "http://127.0.0.1:6900" + self.path
            resp = requests.get(target, timeout=20)
            self.send_response(resp.status_code)
            self.send_header("Content-Type", resp.headers.get("Content-Type", "application/json"))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resp.content)
            return
        return super().do_GET()

if __name__ == "__main__":
    os.chdir(ROOT)
    print("Serving on http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
