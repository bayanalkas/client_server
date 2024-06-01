import socket
import sys

# Check if server IP address is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python client.py <Server IP Address>")
    sys.exit(1)

serverName = sys.argv[1]
PORT = 44880

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, PORT))

while True:
    sentence = input('Client: ')
    clientSocket.send((sentence + '\n').encode())

    if sentence == "MSGGET":
        response = clientSocket.recv(1024).decode()
        print(response)
    elif sentence == "MSGSTORE":
        response = clientSocket.recv(1024).decode()
        print(response)
        if response.strip() == "200 OK":
            new_message = input("Enter new message of the day: ")
            clientSocket.send((new_message + '\n').encode())
            response = clientSocket.recv(1024).decode()
            print(response)
    elif sentence == "QUIT":
        response = clientSocket.recv(1024).decode()
        print(response)
        clientSocket.close()
        break
    else:
        print("Unknown command")

clientSocket.close()
