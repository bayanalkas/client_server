import socket

PORT = 44880

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', PORT))
serverSocket.listen(1)

print('The server is ready to receive')

# Default message of the day
message_of_the_day = "An apple a day keeps the doctor away.\n"

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode().strip()

    print(f"Received from client: {sentence}")

    if sentence == "MSGGET":
        response = "200 OK\n" + message_of_the_day
        connectionSocket.send(response.encode())
    elif sentence == "MSGSTORE":
        connectionSocket.send("200 OK\n".encode())
        new_message = connectionSocket.recv(1024).decode().strip() + '\n'
        message_of_the_day = new_message
        connectionSocket.send("200 OK\n".encode())
    elif sentence == "QUIT":
        connectionSocket.send("200 OK\n".encode())
        connectionSocket.close()
    else:
        print("Unknown command received")

    connectionSocket.close()
