import socket, threading
from time import sleep

sock = socket.socket()
addr = ("127.0.0.1", 55555)
sock.connect(addr)

def sock_send(data):
    sock.send(data)

def sock_recieve():
    while True:
        data_in = sock.recv(30)
        print(data_in.decode('ascii'))

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

while True:
    data = input()
    sock_send(f"Evgenii_client_2: {data}".encode('ascii'))