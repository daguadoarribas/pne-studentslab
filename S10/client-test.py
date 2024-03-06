from Client0 import Client
import termcolor

IP = "212.128.255.149"
PORT = 8080
c = Client(IP, PORT)

for i in range(5):
    msg = "Message" + str(i)
    response = c.talk(msg)

    print(f"To server:" + termcolor.colored(msg,"blue"))
    print(f"From server:" + termcolor.colored(response,"green"))