import socket

HOST=socket.gethostbyname(socket.gethostname())
PORT=800

print(HOST)

sockets=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockets.bind((HOST,PORT))

sockets.listen(2)

while True:
    comm_port , addr = sockets.accept()
    print(f"connected to {addr}")
    message = comm_port.recv(1024).decode()
    print(f"receved message {message}")
    comm_port.send("received sucess".encode())
    comm_port.close()
    print(f"communication closed {addr}")
