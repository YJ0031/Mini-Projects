# echo-server.py

import socket
from a51 import *

HOST = "192.168.1.123"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        #if not data:
        #    break
        
        #conn.close()

        k = (conn.recv(1024)).decode()
        print(" - Key has been recieved!")

        set_key(k)

        message = (conn.recv(1024)).decode()
        ciphertext = encrypt(message)
        print(f" - The ciphertext is: {ciphertext}")

        plaintext = decrypt(ciphertext)
        print(f" - Decrypted message is: {plaintext}")

        

        #conn.send(bytes(str(public), encoding='utf-8'))

