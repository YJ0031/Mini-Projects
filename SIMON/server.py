# echo-server.py

import socket
from simon import *
import re
from struct import *

HOST = "192.168.1.106"  # Standard loopback interface address (localhost)
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


        key = (conn.recv(1024)).decode('utf-8')
       
        key = hex(int(key))
        key = int(key, 16)
        print(f" - Key {key} has been recieved!")
        
        key_size = (conn.recv(1024)).decode()
        key_size = hex(int(key_size))
        key_size = int(key_size, 16)
        print(f" - Key Size {key_size} has been recieved!")
        
        block_size = (conn.recv(1024)).decode()
        block_size = hex(int(block_size))
        block_size = int(block_size, 16)
        print(f" - Block size {block_size} has been recieved!")
        
        plaintext = (conn.recv(1024)).decode()
        print(f" - Plaintext {plaintext} has been recieved!")
        
        #key = (format(key, '#x'))
        #key =  int((re.search(r'[a-z0-9]*', key).group()), 16)
        #key = 0x131211100b0a090803020100

        #w = SimonCipher(key, 144, 96)

        w = SimonCipher(key, key_size, block_size)

        plaintext = (plaintext).encode("utf-8")
        h_plaintext = plaintext.hex()
        i_plaintext = int(h_plaintext, 16)

        encrypted = w.encrypt(i_plaintext)
        print(f"Encrypted text: {encrypted}")

        decrypted = w.decrypt(encrypted)
        print(f"Decrypted text: {decrypted}")

        h_plaintext = hex(decrypted)
        b_plaintext = bytes.fromhex(h_plaintext[2:])
        plaintext = b_plaintext.decode("utf-8")

        print(plaintext)





        #conn.send(bytes(str(public), encoding='utf-8'))

