import http.server
import socketserver

PORT = 8000
TEXT_TO_RETURN = "現在の最新バージョンは1.1.0です。"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(TEXT_TO_RETURN.encode("utf-8"))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
