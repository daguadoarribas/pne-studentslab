import http.client
import json
import termcolor

server = "rest.ensembl.org"
source = "/sequence/id/ENSG00000207552"
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
print("MIR633")

termcolor.cprint("Description: ", "green", end="")
print(gene["desc"])

termcolor.cprint("Bases: ", "green", end="")
print(gene["seq"])
