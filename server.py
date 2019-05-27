from socket import *
import time

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
        msg = "Welcome to server"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "UTF-8"))

        while True:
            time.sleep(3)
            msg = f"Time is! {time.time()}"
            msg = f'{len(msg):<{HEADERSIZE}}' + msg
            clientsocket.send(bytes(msg, "UTF-8"))