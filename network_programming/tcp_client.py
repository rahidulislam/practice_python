import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to the server
client_socket.connect(("localhost",65432))
# send data to the server
client_socket.sendall(b"Hello World")
# receive data from the server
data = client_socket.recv(1024)
print(f"Received data from server: {data}")
client_socket.close()