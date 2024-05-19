import http.server
from http import HTTPStatus
import termcolor
import jinja2
import os
from pathlib import Path
import socketserver
from urllib.parse import urlparse, parse_qs
from class_seq import Seq

port = 8080
ensembl_server = "rest.ensembl.org"
resource_to_ensembl_server = {
    '/listSpecies': {'resource': "/info/species", 'params': "content-type=application/json"},
    '/karyotype': {'resource': "/info/assembly", 'params': "content-type=application/json"},
    '/chromosomeLength': {'resource': "/info/assembly", 'params': "content-type=application/json"},
    '/geneSeq': {'resource': "/sequence/id", 'params': "content-type=application/json"},
    '/geneInfo': {'resource': "/overlap/id", 'params': "feature=gene;content-type=application/json"},
    '/geneList': {'resource': "/overlap/region/human", 'params': "content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon"}
}


def read_html(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def server_request(SERVER, URL):
    import http.client
    flag = True
    info = None
    try:
        connection = http.client.HTTPConnection(SERVER)
        connection.request("GET", URL)
        response = connection.getresponse()
        if response.status == HTTPStatus.OK:
            json_str = response.read().decode()
            info = json.loads(json_str)
    except Exception:
        flag = False
    return flag, info

def handle_error(endpoint, msg):
    dict_with_errors = {
        "endpoint": endpoint,
        "message": msg
    }
    return read_html("error.html").render(context=dict_with_errors)

def handle_get(arguments):
    try:
        sequence_number = int(arguments['sequence_number'][0])
        contents = read_html("get.html")
        context = {'number': sequence_number, 'sequence': SEQUENCES[sequence_number]}
        contents = contents.render(context=context)
        code = HTTPStatus.OK
    except (KeyError, IndexError, ValueError):
        file_path = os.path.join(HTML_FOLDER, "error.html")
        contents = Path(file_path).read_text()
        code = HTTPStatus.NOT_FOUND
    return contents, code


socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_get(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        resource = parsed_url.path
        print(f"Resource: {resource}")
        arguments = parse_qs(parsed_url.query)
        print(f"Arguments: {arguments}")

        code = HTTPStatus.OK
        if resource == "/":
            contents = read_html("index.html")
            context = {'n_sequences': len(SEQUENCES), 'genes': GENES}
            contents = contents.render(context=context)
        elif resource == "/ping":
            file_path = os.path.join(HTML_FOLDER, "ping.html")
            contents = Path(file_path).read_text()
        elif resource == "/get":
            contents, code = handle_get(arguments)
        elif resource == "/gene":
            try:
                gene_name = arguments['gene_name'][0]
                contents = read_html("gene.html")
                file_name = os.path.join("..", "sequences", gene_name + ".txt.fa")
                s = Seq()
                s.read_fasta(file_name)
                context = {'gene_name': gene_name, 'sequence': str(s)}
                contents = contents.render(context=context)
            except (KeyError, IndexError, FileNotFoundError):
                file_path = os.path.join(HTML_FOLDER, "error.html")
                contents = Path(file_path).read_text()
                code = HTTPStatus.NOT_FOUND
        elif resource == "/operation":
            try:
                bases = arguments['bases'][0]
                op = arguments['op'][0]
                contents = read_html("operation.html")
                s = Seq(bases)
                if op in OPERATIONS:
                    if op == "info":
                        result = s.info().replace("\n", "<br><br>")
                    elif op == "comp":
                        result = s.complement()
                    elif op == "rev":  
                        result = s.reverse()
                    context = {'sequence': str(s), 'op': op, 'result': result}
                    contents = contents.render(context=context)
                else:
                    file_path = os.path.join(HTML_FOLDER, "error.html")
                    contents = Path(file_path).read_text()
                    code = HTTPStatus.NOT_FOUND
            except (KeyError, IndexError):
                file_path = os.path.join(HTML_FOLDER, "error.html")
                contents = Path(file_path).read_text()
                code = HTTPStatus.NOT_FOUND
        else:
            file_path = os.path.join(HTML_FOLDER, "error.html")
            contents = Path(file_path).read_text()
            code = HTTPStatus.NOT_FOUND

        self.send_response(code)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)


with socketserver.TCPServer(("", port), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()
