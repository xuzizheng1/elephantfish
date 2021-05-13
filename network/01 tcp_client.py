"""
tcp客户端的创建步骤：
    1. create a socket
    2. connect to server
    3. send data to server (only bytes can be sent)
    4. receive data (only bytes can be received)
    5. close the socket
"""
import socket

from network.config import PORT

if __name__ == '__main__':
    # 1. create a socket
    cli_socket = socket.socket()

    # 2. connect to server (addr is a tuple class)
    address = ('', PORT)
    cli_socket.connect(address)

    while True:
        # 4. receive data(bytes)
        recv_data = cli_socket.recv(1024).decode()
        print(recv_data)
        # 3. send data(bytes) to server
        data = input('your move:\n')
        cli_socket.send(data.encode())


    # 5. close the socket
    # cli_socket.close()
