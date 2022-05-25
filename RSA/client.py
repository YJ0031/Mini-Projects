# echo-client.py

import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    p = int(input(" - Enter a prime number (17, 19, 23, etc): "))
    s.send(bytes(str(p), encoding='utf-8'))

    q = int(input(" - Enter another prime number (Not one you entered above): "))
    s.send(bytes(str(q), encoding='utf-8'))

    public = (s.recv(1024)).decode()
    private = (s.recv(1024)).decode()

    print(f" - Your public key is {public} and your private key is {private}")

    message = input(" - Enter a message to encrypt with your public key: ")

    s.send(bytes(str(message), encoding='utf-8'))

