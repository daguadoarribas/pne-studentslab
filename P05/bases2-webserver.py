from pathlib import Path
import termcolor
import http.server
import socketserver

PORT = 8080


def read_html_file(filename):
    directory = "html/info/"
    file_contents = Path(directory + filename).read_text()
    return file_contents


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, "green")

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
            my_file = self.path[1:]  # parte de la URL de la solicitud HTTP después del primer carácter
            try:
                contents = Path(f"html/{my_file}").read_text()
                self.send_response(202)  # envía una respuesta HTTP con el código de estado 202 -> Aceptado
            except FileNotFoundError:
                contents = Path("html/error.html").read_text()
                self.send_response(404)  # envía una respuesta HTTP con el código de estado 404 -> No encontrado

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
        print("Server stopped by the user")
        httpd.server_close()
