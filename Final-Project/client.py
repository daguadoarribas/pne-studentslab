import http.client
import json
from http import HTTPStatus

PORT = 8081
SERVER = "localhost"
connection = http.client.HTTPConnection(SERVER, port=PORT)

try:
    connection.request("GET", "/chromosomeLength?species=mouse&chromo=18&json=1")
except ConnectionRefusedError:
    print("Error! Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    info = json.loads(data_str)
    print(info)
    chromosome = info["chromosome"]
    length = info["length"]
    print(chromosome, length)

try:
    connection.request("GET", "/geneSeq?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("Error! Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode("utf-8")
    info = json.loads(data_str)
    gene = info["gene"]
    bases = info["bases"]
    print(gene, bases)

try:
    connection.request("GET", "/geneSeq?gene=TEST&json=1")
except ConnectionRefusedError:
    print("Error! Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received: {response.status} {response.reason}\n")
if response.status != HTTPStatus.OK:
    data_str = response.read().decode()
    print(data_str)
