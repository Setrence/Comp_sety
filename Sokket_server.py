# echo-server.py
import threading
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
sock = socket.socket()

sock.bind((HOST, PORT))
sock.listen()
conn, addr = sock.accept()

print(f"Connected by {addr}")

def sock_send(data):
    sock.send(data)
def sock_recieve():
    while True:
        data_in = conn.recv(1024)
        print(data_in.decode('ascii'))

rec_thread = threading.Thread(target = sock_recieve())
rec_thread.start()

while True:
    data = input()
    sock_send(f"Evgenii_server: {data}".encode('ascii'))