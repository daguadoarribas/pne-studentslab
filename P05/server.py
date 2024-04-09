import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        if self.requestline.startswith("GET / ") or self.requestline.startswith("GET /index"):
            contents = Path("../P05/html/index.html").read_text()
        elif self.requestline.startswith("GET /info/A"):
            contents = Path("../P05/html/info/A.html").read_text()
        elif self.requestline.startswith("GET /info/C"):
            contents = Path("../P05/html/info/C.html").read_text()
        elif self.requestline.startswith("GET /info/G"):
            contents = Path("../P05/html/info/G.html").read_text()
        elif self.requestline.startswith("GET /info/T"):
            contents = Path("../P05/html/info/T.html").read_text()
        else:
            contents = Path("../S14/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()