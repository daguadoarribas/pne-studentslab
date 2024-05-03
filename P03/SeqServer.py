import socket
import termcolor
from Seq0 import *


class SeqServer:
    def __init__(self):
        IP = "127.0.0.1"
        PORT = 8080

        MAX_OPEN_REQUESTS = 5

        # Counting the number of connections
        number_con = 0  # al principio no hay nada conectado

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
                msg = clientsocket.recv(2048).decode("utf-8")  # msg es el mensaje que el cliente manda al servidor-- lo que va despues de echo
                print("Message from client: {}".format(msg))

                # Send the message

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

    def return_response(self, msg):  # esto es para que para cada msg del cliente el servidor de una respuesta concreta
        if msg.startswith("PING"):
            termcolor.cprint("PING", "green")  # los prints aperecen en mi pantallita normal
            return self.ping_response()  # los returns aparecen en la terminal
        elif msg.startswith("GET"):
            termcolor.cprint("GET\n", self.get_response(msg), "green")
            return self.get_response()
        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", "green")
            return self.info_response()
        elif msg.startswith("COMP"):
            termcolor.cprint("COMP", "green")
            return self.comp_response()
        elif msg.startswith("REV"):
            termcolor.cprint("REV", "green")
            return self.rev_response()
        elif msg.startswith("GENE"):
            termcolor.cprint("GENE", "green")
            return self.gene_response()

    def ping_response(self):  # aqui no pongo msg porque ping responde SIEMPRE Ok!
        print("PING command!")  # Print message in green
        return "OK!\n"  # Response message

    def get_response(self, msg):
        sequence = ["ACGGTACGATAC", "CATGGGATCAATG", "ACATTAGCGTTGA", "TGGATCCATGCA", "AGTGATTGCTGAT"]
        number = 0
        for i in msg:  # esto itera por las letras hasta que encuentra un numero eg GET 2 --> 2
            if i.isdigit():
                number = i  # esto hace que ese numero (2) ahora sea i
            else:
                pass
        return sequence[int(number)]  # returneo el elemento de la lista con el indice i = number

    def info_response(self, msg):
        gene = msg.split(" ")
        gene = gene[1]
        seq = Seq(gene)
        length = f"Total length: {seq.len()}"
        c_a = f"\nA:{seq.seq_count_base('A')} ({seq.seq_count_base('A') / seq.len() * 100}%)"
        c_c = f"\nC:{seq.seq_count_base('C')} ({seq.seq_count_base('C') / seq.len() * 100}%)"
        c_g = f"\nG:{seq.seq_count_base('G')} ({seq.seq_count_base('G') / seq.len() * 100}%)"
        c_t = f"\nT:{seq.seq_count_base('T')} ({seq.seq_count_base('T') / seq.len() * 100}%)"
        return f"Sequence: {seq} \n{length} {c_a}, {c_c}, {c_g}, {c_t}"

    def comp_response(self, msg):
        seq = msg.split(" ")
        seq = seq[1]
        seq = Seq(seq)
        comp = seq.seq_complement()
        return comp

    def rev_response(self, msg):
        seq = msg.split(" ")
        seq = seq[1]
        seq = Seq(seq)
        rev = seq.seq_reverse()
        return rev

    def gene_response(self, msg):
        which_gene_to_send = msg.split(" ")
        try:
            gene_to_send = which_gene_to_send[1]
            seq = Seq()
            return seq.read_fasta(gene_to_send)
        except IndexError:
            return "Insert a valid sequence"


c = SeqServer()
