import socket

host = 'localhost'
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

message = sock.recv(1024)

while message:
    print("Mesage: ", message.decode)
    message = sock.recv(1024)

sock.close()