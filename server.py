from socket import *
import time
import pickle




HEADERSIZE = 10

serverName = "localhost"
serverPort = 4444
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind((serverName, serverPort))
s.listen(5)

print("Server is ready to receive data...")

while 1:
        clientsocket, address = s.accept()
        print(f"connection from {address} is established")

        d = {1: "Hey", 2: "There"}
        msg = pickle.dumps(d)
        # print(msg)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', "UTF-8") + msg
        clientsocket.send(msg)

