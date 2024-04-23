from Client0 import Client
from P01.Seq1 import Seq
PRACTICE = 2
EXERCISE = 4

SEQUENCES_DIR = "../Sequences/"
GENES = ["U5.txt", "ADA.txt", "FRAT1.txt"]

IP = "212.128.255.29" # your IP server address
PORT = 8081
def get_file_path(gene):
    return SEQUENCES_DIR + gene

def req_response_from_server(client, msg):
    print("To server: {}".format(msg), sep="")
    response = client.talk(msg)
    print(f"From Server: {response}")

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

c = Client(IP, PORT)

for g in GENES:
    s = Seq()
    s.read_fasta(get_file_path(g))
    m = "Sending " + g + " Gene to the server..."
    req_response_from_server(c, m)
    m = str(s)
    req_response_from_server(c, m)


