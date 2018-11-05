import socket

def client_exec():
    host = socket.gethostname()
    port = 2999

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" Input address and search term -> ")

    while message.lower().strip() != 'close':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        message = input(" Input address and search term -> ")
    
    client_socket.close()

if __name__ == '__main__':
    client_exec()