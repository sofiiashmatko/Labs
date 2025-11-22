import socket
import os

HOST = "127.0.0.1"
PORT = 9000

filename = "example.txt"   # ТУТ вкажи свій текстовий файл

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    # Спочатку надсилаємо ім’я файлу
    client.sendall(filename.encode("utf-8"))

    # Тепер надсилаємо вміст файлу
    with open(filename, "rb") as f:
        data = f.read(4096)
        while data:
            client.sendall(data)
            data = f.read(4096)

print(f"File '{filename}' sent to server!")
