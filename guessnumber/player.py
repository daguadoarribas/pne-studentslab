import socket


IP = "212.128.255.99"
PORT = 8080
player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player_socket.connect((IP, PORT))

print("Player, type a number between 1 and 100")

flag = False
while not flag:
    player_guess = input("Type a number")
    player_socket.send(str.encode(player_guess))
    response = player_socket.recv(2048).decode("utf-8")
    print(response)
    if "won" in response:
        break

player_socket.close()







