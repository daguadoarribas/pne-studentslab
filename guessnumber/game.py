import socket
import random
class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []
        IP = "212.128.255.99"
        PORT = 8080
        MAX_OPEN_REQUESTS = 5
        number_con = 0  #al principio no hay nada conectado

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            serversocket.listen(MAX_OPEN_REQUESTS)
            while True:
                print("Waiting for connections at {}, {} ".format(IP, PORT))
                (clientsocket, address) = serversocket.accept()
                number_con += 1
                print("CONNECTION: {}. From the IP: {}".format(number_con, address))
                msg = clientsocket.recv(2048).decode("utf-8")  # msg es el mensaje que el cliente manda al servidor-- lo que va despues de echo
                print("Message from client: {}".format(msg))
                message = self.return_response(str(msg))  # respuesta del servidor al msg del cliente
                send_bytes = str.encode(message)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()
        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))
        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()
    def guess(self, number):
        self.attempts.append(number)
        if number == self.secret_number:
            return f'You won after {len(self.attempts)} attempts'
        elif number < self.secret_number:
            return 'Higher'
        else:
            return 'Lower'

c = NumberGuesser()