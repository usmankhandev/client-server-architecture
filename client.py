import socket
import select
import errno
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking

username = my_username.encode('UTF-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('UTF-8')
client_socket.send(username_header+username)

while True:
    message = input(f"{my_username} > ")
    if message:
        message = message.encode('UTF-8')
        message_header = f"{len(message): < {HEADER_LENGTH}}".encode('UTF-8')
        client_socket.send(message_header + message)

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode("UTF-8").strip())
            username = client_socket.recv(username_length).decode("UTF-8")
            message_header = client_socket.recv(message_header).decode("UTF-8")
            message_length = int(message_header.decode("UTF-8").strip())
            message = client_socket.recv(message_length).decode("UTF-8")

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading Error', str(e))
            sys.exit()
        continue


    except Exception as e:
        print('General Error', str(e))
        sys.exit()




























# from socket import *
# import pickle


# HEADERSIZE = 10
# serverName = "localhost"
# serverPort = 4444
# BUFFER_SIZE = 1024

# s = socket(AF_INET, SOCK_STREAM)
# s.connect((serverName, serverPort))

# while True:

#     full_msg = b''
#     new_msg = True
#     while True:
#         msg = s.recv(BUFFER_SIZE)
#         if new_msg:
#             print(f"new message length: {msg[:HEADERSIZE]}")
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False

#         full_msg += msg

#         if len(full_msg)-HEADERSIZE == msglen:
#             print("full nsg recieved")
#             print(full_msg[HEADERSIZE:])
#             d = pickle.loads(full_msg[HEADERSIZE:])
#             print(d)
#             new_msg = True
#             full_msg = b''
#     print(full_msg)