# Client-Server Application

This repository contains two programs, a server and a client, that communicate over TCP/IP. The server listens for requests from the client and processes three commands: `MSGGET`, `MSGSTORE`, and `QUIT`.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
  - [Server](#server)
  - [Client](#client)
- [Commands](#commands)
  - [MSGGET](#msgget)
  - [MSGSTORE](#msgstore)
  - [QUIT](#quit)
- [Notes](#notes)

## Requirements

- Python 3.x
- A network environment that allows communication between the server and client.

## Usage

### Server

1. Start the server by running the `server.py` script.

```bash
python server.py
The server will listen on port 44880 for incoming connections.

### Client
Start the client by running the client.py script with the server's IP address as an argument.
bash

python client.py <Server IP Address>
For example:

bash
python client.py 10.0.0.111
The client will connect to the server on port 44880.

Commands
MSGGET
The MSGGET command requests the current message of the day from the server.

Client:
MSGGET

Server:
200 OK
An apple a day keeps the doctor away.
MSGSTORE
The MSGSTORE command allows the client to update the server's message of the day.

Client:
MSGSTORE

Server:
200 OK
Client sends the new message:


Imagination is more important than knowledge.
Server confirms the update:

200 OK
QUIT
The QUIT command terminates the connection with the server.

Client:
QUIT

Server:
200 OK

### Notes
The server prints all messages received from clients on the screen.
The server stores a default message of the day, which can be updated by the client using the MSGSTORE command.
The client can continuously send commands to the server until the QUIT command is issued.
Example Client-Server Interaction
Start the server:
bash

python server.py
Start the client:
bash
python client.py 10.0.0.111

Client sends MSGGET:
Client:
MSGGET

Server:
200 OK
An apple a day keeps the doctor away.

Client sends MSGSTORE:
Client:
MSGSTORE

Server:
200 OK

Client sends the new message:
Imagination is more important than knowledge.

Server confirms the update:
200 OK

Client sends QUIT:
Client:
QUIT

Server:
200 OK
The connection is closed.

This README provides instructions for setting up and running the client-server application, as well as details on the supported commands and their usage.

vbnet
Copy code

This `README.md` file provides a comprehensive guide to setting up and running the client-server application, as well as examples of how to use the supported commands.




