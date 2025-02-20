import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the socket to the port
server_socket.bind(('localhost',65432))

# listen for connections
server_socket.listen()

print("Server is listening for incomming connection on port 65432")
# accept connections from outside
connection,client_address = server_socket.accept()
try:
    print(f"Connected to {client_address}")
    data = connection.recv(1024)
finally:
    connection.close()