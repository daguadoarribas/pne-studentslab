import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from P01.Seq1 import Seq

PORT = 8080

sequences = ["ACGT", "ACCCGGTA", "TACATG", "ACACG", "ACCT"]
genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
operations = ["info", "comp", "rev"]


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def for_get(arguments):
    number = int(arguments['number'][0])
    contents = read_html_file('get.html')
    context = {'number': number, 'sequence': sequences[number]}
    contents = contents.render(context=context)
    return contents


def for_gene(arguments):
    gene = arguments['name'][0]
    contents = read_html_file('gene.html')
    s = Seq()
    s.read_fasta(gene)
    context = {'name': gene, 'sequence': str(s)}
    contents = contents.render(context=context)
    return contents


def info_function(s):
    result = f"Total length: {s.len()}"
    result += f"<br><br>A:{s.seq_count_base('A')} ({s.seq_count_base('A') / s.len() * 100}%)"
    result += f"<br><br>C:{s.seq_count_base('C')} ({s.seq_count_base('C') / s.len() * 100}%)"
    result += f"<br><br>G:{s.seq_count_base('G')} ({s.seq_count_base('G') / s.len() * 100}%)"
    result += f"<br><br>T:{s.seq_count_base('T')} ({s.seq_count_base('T') / s.len() * 100}%)"
    return result


def for_operation(arguments):
    seq = arguments['seq'][0]
    operation = arguments['operation'][0]
    contents = read_html_file('operation.html')
    s = Seq(seq)
    if operation == "info":
        result = info_function(s)
    elif operation == "comp":
        result = s.seq_complement()
    else:
        result = s.seq_reverse()
    context = {'seq': seq, 'operation': operation, 'result': result}
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
            self.send_response(200)
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
