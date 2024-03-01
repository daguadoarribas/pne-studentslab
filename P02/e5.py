from Client0 import Client
from P01.Seq1 import Seq
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.97" # your IP server address
PORT = 8081

c = Client(IP, PORT)
print(c)
s = Seq()
s.read_fasta("../Sequences/FRAT1.txt")
msg = (f"Sending FRAT1 Gene to the server, in fragments of 10 bases...")
first_message = c.talk(msg)
msg2 = str(s)
second_message = c.talk(f"Gene FRAT1: {msg2}")
print(f"Gene FRAT1: {msg2}")

for i in range (1, 6):
    index = (i-1) * 10
    fragment = msg2[index: index + 10]
    message = c.talk(f"Fragment {i}: {fragment}")
    print(f"Fragment {i}: {fragment}")