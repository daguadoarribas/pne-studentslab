import http.server
from http import HTTPStatus
import socketserver
from pathlib import Path
import os
import json
import jinja2
from urllib.parse import urlparse, parse_qs
import termcolor


PORT = 8081
HTML_FOLDER = "html"
ENSEMBL_SERVER = "rest.ensembl.org"
RESOURCE_TO_ENSEMBL_LINK = {"/listSpecies": {"resource": "/info/species", "params": "content-type=application/json"},
                            "/karyotype": {"resource": "/info/assembly", "params": "content-type=application/json"},
                            "/chromosomeLength": {"resource": "/info/assembly", "params": "content-type=application/json"}}
ENSEMBL_CONNECTION_ERROR = "Error in communication with the Ensembl server"
RESOURCE_MISSING_ERROR = "Resource not available"


def read_html_template(file_name):
    file_path = os.path.join(HTML_FOLDER, file_name)
    contents = Path(file_path).read_text()
    contents = jinja2.Template(contents)
    return contents


def server_request(server, url):
    import http.client

    error = False
    data = None
    try:
        connection = http.client.HTTPSConnection(server)
        connection.request("GET", url)
        response = connection.getresponse()
        if response.status == HTTPStatus.OK:
            json_str = response.read().decode()
            data = json.loads(json_str)
        else:
            error = True
    except Exception:
        error = True
    return error, data


def handle_error(endpoint, message):
    context = {"endpoint": endpoint, "message": message}
    return read_html_template("error.html").render(context=context)


def list_species(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_LINK[endpoint]
    url = f"{request['resource']}?{request['params']}"
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        limit = None
        if 'limit' in parameters:
            limit = int(parameters['limit'][0])

        species = data["listSpecies"]
        name_species = []
        for specie in species[:limit]:
            name_species.append(specie["display_name"])
        context = {"number_of_species": len(species), "limit": limit, "name_species": name_species}
        contents = read_html_template("listSpecies.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_CONNECTION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def karyotype(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_LINK[endpoint]
    specie = parameters['species'][0]
    url = f"{request['resource']}/{specie}?{request['params']}"
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        context = {"specie": specie, "karyotype": data['karyotype']}
        contents = read_html_template("karyotype.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_CONNECTION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def chromosome_length(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_LINK[endpoint]
    specie = parameters['species'][0]
    user_chromosome = parameters['chromo'][0]
    url = f"{request['resource']}/{specie}?{request['params']}"
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        length = None
        print(data)
        chromosomes_list = data['top_level_region']
        for chromo in chromosomes_list:
            if chromo['name'] == user_chromosome:
                length = chromo['length']
                break
        context = {"length": length, 'chromosomes_list': chromosomes_list}
        contents = read_html_template("chromosomeLength.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_CONNECTION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_get(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        endpoint = parsed_url.path
        print(f"Endpoint: {endpoint}")
        parameters = parse_qs(parsed_url.query)
        print(f"Parameters: {parameters}")

        code = HTTPStatus.OK
        content_type = "text/html"
        if endpoint == "/":
            file_path = os.path.join(HTML_FOLDER, "index.html")
            contents = Path(file_path).read_text()
        elif endpoint == "/listSpecies":
            code, contents = list_species(endpoint, parameters)
        elif endpoint == "/karyotype":
            code, contents = karyotype(endpoint, parameters)
        elif endpoint == "/chromosomeLength":
            code, contents = chromosome_length(endpoint, parameters)
        else:
            contents = handle_error(endpoint, RESOURCE_MISSING_ERROR)
            code = HTTPStatus.NOT_FOUND

        self.send_response(code)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()
