import http.client
import json

server = "rest.ensembl.org"
source = "/info/ping"
parameters = "?content-type=application/json"
url = server + source + parameters

print()
print("Server: {}".format(server))
print("Url: {}".format(url))

connection = http.client.HTTPConnection(server)

try:
    connection.request("GET", source + parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = connection.getresponse()

# -- Print the status line
print(f"Response received!: {response.status} {response.reason}\n")

# -- Read the response's body
data1 = response.read().decode("utf-8")

ping = json.loads(data1)

print()
if ping['ping'] == 1:
    print("PING OK! The database is running!")
