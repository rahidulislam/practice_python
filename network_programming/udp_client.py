import socket

# create a udp socket
client_socket  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.sendto(b"Hello Server",("localhost",65432))
data,server_address = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")
client_socket.close()