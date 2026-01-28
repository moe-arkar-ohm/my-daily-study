import socket

# 1. Create a TCP Socket (SOCK_STREAM means TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to an address (Localhost, Port 9999)
server.bind(('127.0.0.1', 9999))

# 3. Listen for calls
server.listen()
print("Server is listening on 127.0.0.1:9999...")

# 4. Accept the call
client_socket, addr = server.accept()
print(f"Connection from: {addr}")

# 5. Send a message (Bytes)
client_socket.send(b"Hello from the TCP Server!")

# 6. Close
client_socket.close()