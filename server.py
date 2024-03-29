import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #bind the port
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr, "this server")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("client: ", repr(data))

            