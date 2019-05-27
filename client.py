
from socket import *

HEADERSIZE = 10
serverName = "localhost"
serverPort = 4444
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect((serverName, serverPort))

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(BUFFER_SIZE)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("UTF-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full nsg recieved")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
    print(full_msg)