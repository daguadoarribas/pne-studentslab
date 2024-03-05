import socket

PORT = 8080
IP = "212.128.255.103" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

count = 0
while True: ##To keep listening to different clients
    count += 1
    (rs, address) = ls.accept() ##Returns A taple that is the socket and the address. The server is waiting for a client to make a request
    print("CONNECTION", str(count), "Client ID, PORT: " + str(address))      ## if I write this in the terminal u get the client printed: echo "Hi!" | nc 212.128.255.103 8081

    msg = rs.recv(2048).decode("utf-8")  ##this message is in bytes and we need to convert them to code as a string
    print("The client says..." + msg)

    new_msg = "ECHO: " + msg        #We create a string that we are going to send to the server
    rs.send(new_msg.encode())

    rs.close() ##We close the socket of the client
# -- Close the socket
ls.close()