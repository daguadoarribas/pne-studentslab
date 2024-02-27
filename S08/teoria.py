import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8081
IP = "212.128.255.64" # it depends on the machine the server is running -- the one from the teacher: 212.128.255.64


# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       ##AF INET: internet socket - it understand ip protocols

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))       ##Tuple: one parametre with two values, which connects the ip and the port (client-server)

# Send data. No strings can be sent, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))      ##str.encode: transform the text into bytes

# Close the socket
s.close()
