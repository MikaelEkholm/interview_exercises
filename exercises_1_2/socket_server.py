import socket
import socketserver
import subprocess

class SocketHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip().decode()
        args = self.data.split(" ")

        if len(args) != 2:
            self.data = "Incorrect amount of arguments!".encode()
            self.request.sendall(self.data)
        else:
            cmd = "/home/socket_server/script.sh " + args[0] + " " + args[1]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()
            self.data = output
            self.request.sendall(self.data)

if __name__ == '__main__':
    host = 'localhost'
    port = 2999

    server = socketserver.TCPServer((host, port), SocketHandler)

    server.serve_forever()