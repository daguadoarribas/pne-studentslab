import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class EchoServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Check if the path is '/'
        if self.path == '/' or self.path.startswith('/echo?'):
            if '?' in self.path:
                string = self.path.split('?', 1)[1]
                parameters = {}
                for param in string.split('&'):
                    key, value = param.split('=')
                    parameters[key] = value
                message = parameters.get('message', '')

                # Generating the response message
                response_html = f"<html><body><p>Message: {message}</p><a href='/'>Return to form</a></body></html>"
            else:
                # Open the form1.html file
                response_html = Path('html/form-1.html').read_text()

            # Generating the response message
            self.send_response(200)  # -- Status line: OK!

            # Define the content-type header:
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(response_html)))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(str.encode(response_html))
        else:
            # Invalid path, return error
            self.send_error(404, "Not Found")

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler
Handler = EchoServer

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()