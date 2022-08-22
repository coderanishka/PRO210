import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print('\n\n\n\n\n\n IP Messenger\n')

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print('Server is Waiting for Incoming Connections..')
    print('\n')

    acceptConnections()

def handleClient():
    pass

def acceptConnections():
    global SERVER
    global clients 

    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4094).decode().lower()
        client[client_name] = {
            "client"        : client,
            "address"       : addr,
            "connected_with": '',
            "file_name"     : '',
            "file_size"     : 4096
        }
        print(f"Connection established with {client_name} : {addr}")

        thread = Thread(target = handleClient, args = (client, client_name))
        thread.start()

setup_thread = Thread(target = setup)
setup_thread.start()
