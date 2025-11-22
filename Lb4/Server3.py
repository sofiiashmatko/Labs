import socket

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is running on {HOST}:{PORT} and waiting for file...")

    while True:
        conn, addr = server.accept()
        print("Connected by:", addr)

        with conn:

            filename = conn.recv(1024).decode("utf-8")
            print("Receiving file:", filename)

            
            with open(filename, "wb") as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)

            print(f"File '{filename}' saved successfully!\n")
