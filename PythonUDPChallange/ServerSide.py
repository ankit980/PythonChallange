import socket

# Server configuration
host = '127.0.0.1'
port = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

print(f"Server listening on {host}:{port}")

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)

    # Decode the received data
    message = data.decode('utf-8')

    # Process the message (in this example, just print it)
    print(f"Received from {client_address}: {message}")

    # Send a response back to the client
    response = "Registration successful!"
    server_socket.sendto(response.encode('utf-8'), client_address)
