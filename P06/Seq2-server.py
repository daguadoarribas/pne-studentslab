from pathlib import Path
import termcolor
from P06.Seq1 import Seq
import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080

genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
sequences = ["ACGT", "ACCCGGTA", "TACATG", "ACACG", "ACCT"]
operations = ["info", "comp", "rev"]


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def for_get(arguments):
    number = int(arguments["number"][0])
    contents = read_html_file("get.html")
    context = {"number": number, "sequence": sequences[number]}
    contents = contents.render(context=context)  # dict context pasa datos a una plantilla, renderiza la plantilla con esos datos - contenido final se almacena en contents
    return contents


def for_gene(arguments):
    gene = arguments["name"][0]
    contents = read_html_file("gene.html")
    s = Seq()
    s.read_fasta(gene)
    context = {"name": gene, "sequence": str(s)}
    contents = contents.render(context=context)
    return contents


def info_function(s):
    result = "Total length: {}".format(len(s))
    # <br><br> agrega 2 saltos de línea HTML -> 2 líneas vacías
    result += f"<br><br>A:{s.seq_count_base('A')} ({s.seq_count_base('A') / s.len() * 100}%)"
    result += f"<br><br>C:{s.seq_count_base('C')} ({s.seq_count_base('C') / s.len() * 100}%)"
    result += f"<br><br>G:{s.seq_count_base('G')} ({s.seq_count_base('G') / s.len() * 100}%)"
    result += f"<br><br>T:{s.seq_count_base('T')} ({s.seq_count_base('T') / s.len() * 100}%)"
    return result


def for_operation(arguments):
    seq = arguments["seq"][0]
    operation = arguments["operation"][0]
    contents = read_html_file("operation.html")
    s = Seq(seq)
    if operation == "info":
        result = info_function(s)
    elif operation == "comp":
        result = s.seq_complement()
    else:
        result = s.seq_reverse()
    context = {"seq": seq, "operation": operation, "result": result}
    contents = contents.render(context=context)
    return contents


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        if path == "/":
            contents = Path("html/index.html").read_text()
            self.send_response(200)  # código de estado 200 HTTP -> "OK": server procesa bien la solicitud del cliente
        elif path == "/ping":
            contents = Path("html/ping.html").read_text()
            self.send_response(200)
        elif path == "/get":
            contents = for_get(arguments)
            self.send_response(200)
        elif path == "/gene":
            contents = for_gene(arguments)
            self.send_response(200)
        elif path == "/operation":
            contents = for_operation(arguments)
            self.send_response(200)
        else:
            contents = Path("html/error.html").read_text()
            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(contents.encode())  # envío los datos de "contents" de vuelta al cliente que realizó la solicitud HTTP

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
