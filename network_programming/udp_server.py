import socket

# create a UDP socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# bind the socket to a specific address and port
server_socket.bind(("localhost",65432))
while True:
    data,client_address  = server_socket.recvfrom(1024)
    print(f"Received: {data.decode()} from {client_address}")
    server_socket.sendto(b"Hello Client",client_address)
    