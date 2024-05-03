import random
import socket

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "higher"
        elif guess > self.secret_number:
            return "lower"
        else:
            return "correct!"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Waiting for connection...")
connection, address = server_socket.accept()
print("Connected to:", address)

game = NumberGuesser()

while True:
    try:
        data = connection.recv(1024)
        if not data:
            break
        guess = int(data.decode())
        result = game.check_guess(guess)
        connection.sendall(result.encode())
        if result == "correct":
            print(f"Player found the number in {game.attempts} attempts.")
            connection.sendall(str(game.attempts).encode())
            break
    except ValueError:
        connection.sendall("invalid".encode())

connection.close()
server_socket.close()
