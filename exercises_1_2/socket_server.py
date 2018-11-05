import socket
import subprocess

def server_exec():
    host = socket.gethostname()
    port = 2999

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    while True:
        data = conn.recv(1024).decode()
        args = data.split(" ")

        if len(args) != 2:
            data = "Incorrect amount of arguments!"
            conn.send("Incorrect amount of arguments!".encode())
        else:
            cmd = "home/socket_server/script.sh " + args[0] + " " + args[1]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()
            data = output
            conn.send(data)

    conn.close()

if __name__ == '__main__':
    server_exec()