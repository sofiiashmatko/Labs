import socket
import os

HOST = "127.0.0.1"
PORT = 9000

filename = "Task3.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))


    client.sendall(filename.encode("utf-8"))


    with open(filename, "rb") as f:
        data = f.read(4096)
        while data:
            client.sendall(data)
            data = f.read(4096)

print(f"File '{filename}' sent to server!")
