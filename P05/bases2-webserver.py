import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080


def read_html_file(filename):
    folder = "html/info/"
    file_contents = Path(folder + filename).read_text()
    return file_contents


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_get(self):
        termcolor.cprint(self.requestline, 'green')

        if "/info/A.html" == self.path:
            contents = read_html_file("A.html")
        elif "/info/C.html" == self.path:
            contents = read_html_file("C.html")
        elif "/info/G.html" == self.path:
            contents = read_html_file("G.html")
            self.send_response(200)
        elif "/info/T.html" == self.path:
            contents = read_html_file("T.html")
            self.send_response(200)
        elif self.path == "/" or self.path == "/index.html":
            contents = Path("html/index.html").read_text()
            self.send_response(200)
        else:
            my_file = self.path[1:]
            try:
                contents = Path(f"html/{my_file}").read_text()
                self.send_response(202)
            except FileNotFoundError:
                contents = Path("html/error.html").read_text()
                self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


socketserver.TCPServer.allow_reuse_address = True
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
