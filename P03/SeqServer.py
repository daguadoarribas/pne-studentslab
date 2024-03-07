import socket
class SeqServer():
    def __init__(self):
        IP = "127.0.0.1"
        PORT = 8080

        MAX_OPEN_REQUESTS = 5

        # Counting the number of connections
        number_con = 0

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen(MAX_OPEN_REQUESTS)

            while True:
                # accept connections from outside
                print("Waiting for connections at {}, {} ".format(IP, PORT))
                (clientsocket, address) = serversocket.accept()

                # Another connection!e
                number_con += 1

                # Print the connection number
                print("CONNECTION: {}. From the IP: {}".format(number_con, address))

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")   #msg es el mensaje que el cliente manda al servidor-- lo que va despues de echo
                print("Message from client: {}".format(msg))

                # Send the message

                message = self.return_response(str(msg))      #respuesta del servidor al msg del cliente
                send_bytes = str.encode(message)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    sequence = ["ACGGTACGATAC", "CATGGGATCAATG", "ACATTAGCGTTGA", "TGGATCCATGCA", "AGTGATTGCTGAT"]
    def return_response(self, msg):     #esto es para que para cada msg del cliente el servidor de una respuesta concreta
        if msg.startswith("PING"):
            print("PING")
            return self.ping_response()
        elif msg.startswith("GET"):



    def ping_response(self):        ###aqui no pongo msg ##porque ping ##responde ##SIEMPRE Ok!
        print("PING command!")  # Print message in green
        return "OK!\n"  # Response message

    def get_response(self, msg, sequence):
        number = 0
        for i in msg:
            if i.isdigit():
                number = i
            else:
                pass
        return sequence[int(number)]



c = SeqServer()