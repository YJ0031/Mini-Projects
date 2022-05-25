# echo-server.py

import socket
from rsa import *

HOST = "192.168.1.106"  # Standard loopback interface address 
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        #if not data:
        #    break



        p = (conn.recv(1024)).decode()

        #conn.close()

        q = (conn.recv(1024)).decode()
        
        print(" - Recieved p and q....")

        print(" - Generating your public / private key-pairs now . . .")

        public, private = generate_key_pair(int(p), int(q))

        conn.send(bytes(str(public), encoding='utf-8'))
        conn.send(bytes(str(private), encoding='utf-8'))

        message = (conn.recv(1024).decode())

        encrypted_msg = encrypt(public, message)

        print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))

        print(" - Decrypting message with private key ", private, " . . .")
        print(" - Your message is: ", decrypt(private, encrypted_msg))



