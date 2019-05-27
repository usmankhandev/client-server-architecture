import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}

def recieve_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False
        else:
            message_length = int(message_header.decode('utf-8').strip())
            return {"header":message_header, "data":client_socket.recv(message_length)}
    except:
        return False

while True:
    read_sockets, _, expection_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = recieve_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf_8')}")
        else:
            message = recieve_message(notified_socket)
            if message is False:
                print(f"closed connection {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f"recieved msg from {user['data'].decode('utf-8')}:{message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    for notified_socket in expection_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]








# from socket import *
# import time
# import pickle




# HEADERSIZE = 10

# serverName = "localhost"
# serverPort = 4444
# BUFFER_SIZE = 1024

# s = socket(AF_INET, SOCK_STREAM)
# s.bind((serverName, serverPort))
# s.listen(5)

# print("Server is ready to receive data...")

# while 1:
#         clientsocket, address = s.accept()
#         print(f"connection from {address} is established")

#         d = {1: "Hey", 2: "There"}
#         msg = pickle.dumps(d)
#         # print(msg)
#         msg = bytes(f'{len(msg):<{HEADERSIZE}}', "UTF-8") + msg
#         clientsocket.send(msg)

