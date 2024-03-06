import socket
from termcolor import colored  # for colored console output

# Define constants
IP = '127.0.0.1'  # Localhost IP address
PORT = 8080  # Port to listen on
BUFFER_SIZE = 1024  # Buffer size for receiving messages


# Function to handle PING command
def handle_ping():
    print(colored("PING command!", "green"))  # Print message in green
    return "OK!\n"  # Response message


# Main server function
def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((IP, PORT))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port", PORT)

    while True:
        # Accept incoming connection
        rs, address = server_socket.accept()
        print("Connected by", address)

        # Receive data from the client
        data = rs.recv(BUFFER_SIZE).decode()

        # Check if the received data is a PING command
        if data.strip() == "PING":
            response = handle_ping()
            rs.sendall(response.encode())  # Send response to the client
        else:
            print("Unknown command received:", data.strip())

        # Close connection
        rs.close()


if __name__ == "__main__":
    main()