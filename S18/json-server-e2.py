import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is called derived from BaseHTTPRequestHandler
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Parse the path
        # NOTE: self.path already contains the requested resource
        list_resource = self.path.split('?')
        resource = list_resource[0]

        if resource == "/":
            # Read the file
            contents = Path('index.html').read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listusers":
            # Read the file
            contents = Path('people-e1.json').read_text()
            content_type = 'application/json'
            error_code = 200
        else:
            # Read the file
            contents = Path('error.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# Server MAIN program
Handler = TestHandler

# Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # Main loop: Attend the client. Whenever there is a new
    # client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
