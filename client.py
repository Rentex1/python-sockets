import socket

HOST = '10.211.55.3'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("What do you want to send?")
    b = message.encode()
    s.sendall(b)
    #data = s.recv(1024)

#print('Received', repr(data))