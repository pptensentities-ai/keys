#!/usr/bin/env python3
"""
Web-based on-screen arrow keys.
Requires: xdotool
Run: python3 web_arrows.py
Then open http://localhost:8765 in a browser on the VM.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import urllib.parse

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arrow Keys</title>
<style>
body { background:#111; color:#fff; font-family:sans-serif; text-align:center; margin:0; padding:20px; }
button { font-size:36px; width:90px; height:90px; margin:12px; background:#333; color:#fff; border:none; border-radius:12px; cursor:pointer; }
button:active { background:#555; }
h2 { margin-top:10px; }
</style>
</head>
<body>
<h2>Arrow Keys</h2>
<button onclick="send('Up')">↑</button><br>
<button onclick="send('Left')">←</button>
<button onclick="send('Down')">↓</button>
<button onclick="send('Right')">→</button>
<script>
function send(key) {
  fetch('/key?k=' + key);
}
</script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/key'):
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            key = params.get('k', [''])[0]
            if key in ('Up', 'Down', 'Left', 'Right'):
                subprocess.run(['xdotool', 'key', key], check=False)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'ok')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML.encode())

    def log_message(self, format, *args):
        return  # silence logs

if __name__ == '__main__':
    print('Open http://localhost:8765 in the browser on the VM')
    HTTPServer(('127.0.0.1', 8765), Handler).serve_forever()
