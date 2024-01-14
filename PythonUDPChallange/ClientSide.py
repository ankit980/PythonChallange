import socket

# Client configuration
host = '127.0.0.1'
port = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# User registration data
user_data = "Username: Ankit Sharma, Email: ankit071195@gmail.com"

# Send the user data to the server
client_socket.sendto(user_data.encode('utf-8'), (host, port))

# Receive the response from the server
response, server_address = client_socket.recvfrom(1024)

# Decode and print the response
print(f"Response from server: {response.decode('utf-8')}")

# Close the socket
client_socket.close()
