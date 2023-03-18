import socket
import threading
from time import sleep

sock = socket.socket()
addr = ('87.250.250.242', 443)
sock.connect(addr)

def sock_send(data):
    sock.send(data)

def sock_recieve():
    while True:
        data_in = sock.recv(1024)
        print(data_in.encode('ascii'))

sock_send(b'evgenii')


rec_thread = threading.Thread (target = sock_recieve)
rec_thread.start()

while True:
    data = input()
    sock_send(f'evgenii: {data}'.encode('ascii'))

# 127,0,0,1, 11111