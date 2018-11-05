import socket, sys

def client_exec():
    if len(sys.argv) != 2:
        print("Please provide host.")
        return
    host = sys.argv[1]
    port = 2999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    message = input(" Input address and search term -> ")

    while message.lower().strip() != 'close':
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        message = input(" Input address and search term -> ")

    client_socket.close()

if __name__ == '__main__':
    client_exec()