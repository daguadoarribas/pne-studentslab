from Client0 import Client
from P01.Seq1 import Seq
PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.97"  # your IP server address
PORT = 8081
c1 = Client(IP, PORT)
print(c1)

IP = "212.128.255.97"  # your IP server address
PORT = 8080
c2 = Client(IP, PORT)
print(c2)

s = Seq()
s.read_fasta("../Sequences/FRAT1.txt")
msg = f"Sending FRAT1 Gene to the server, in fragments of 10 bases..."
first_msg_first_server = c1.talk(msg)
first_msg_second_server = c2.talk(msg)

msg2 = str(s)
second_msg_first_server = c1.talk(f"Gene FRAT1: {msg2}")
second_msg_second_server = c2.talk(f"Gene FRAT1: {msg2}")
print(f"Gene FRAT1: {msg2}")

for i in range(1, 11):
    index = (i-1) * 10
    fragment = msg2[index: index + 10]
    print(f"Fragment {i}: {fragment}")
    if i % 2 == 0:
        message = c2.talk(f"Fragment {i}: {fragment}")
    else:
        message = c1.talk(f"Fragment {i}: {fragment}")
