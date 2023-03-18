import socket, threading
from time import sleep

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

sock = socket.socket()
sock.connect((HOST, PORT))
sock.sendall(b"Hello, world")
def sock_send(data):
    sock.send(data)

def sock_recieve():
    while True:
        data_in = sock.recv(1024)
        print(data_in.decode('ascii'))

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

while True:
    data = input()
    sock_send(f"Evgenii_client: {data}".encode('ascii'))

# 127,0,0,1, 11111