import http.client
import json
import termcolor
from Seq1 import Seq

genes = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296", "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}

name = str(input("Write the gene name:"))
server = "rest.ensembl.org"
source = f"/sequence/id/{genes[name]}"
parameters = "?content-type=application/json"
url = server + source + parameters

print()
print(f"Server: {server}")
print(f"URL : {url}")

connection = http.client.HTTPConnection(server)

try:
    connection.request("GET", source + parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = connection.getresponse()

print(f"Response received!: {response.status} {response.reason}\n")

str_data = response.read().decode("utf-8")
gene = json.loads(str_data)

print()
termcolor.cprint("Gene: ", "green", end="")
print(name)

termcolor.cprint("Description: ", "green", end="")
print(gene["desc"])

s = Seq(gene["seq"])
termcolor.cprint("Total length: ", "green", end="")
print(s.len())

termcolor.cprint("A", "blue", end="")
print(f": {s.seq_count_base('A')} ({round((s.seq_count_base('A') / s.len() * 100),1)}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {s.seq_count_base('C')} ({round((s.seq_count_base('C') / s.len() * 100),1)}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {s.seq_count_base('G')} ({round((s.seq_count_base('G') / s.len() * 100),1)}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {s.seq_count_base('T')} ({round((s.seq_count_base('T') / s.len() * 100),1)}%)")

termcolor.cprint("Most frequent Base", "green", end="")
print(f": {s.processing_the_genes(name)}")
