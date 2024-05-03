import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    client_socket.sendall(guess.encode())
    response = client_socket.recv(1024).decode()

    if response == "higher":
        print("Try a higher number.")
    elif response == "lower":
        print("Try a lower number.")
    elif response == "correct!":
        print("Congratulations you guessed the number!")
        attempts = client_socket.recv(1024).decode()
        print(f"Number of attempts: {attempts}")
        break
    else:
        print("Invalid input. Please enter a number.")

client_socket.close()
