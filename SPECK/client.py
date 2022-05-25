# echo-client.py

import socket
import re
from struct import *

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print(" - Please Enter the following:")
    key = int((input(" - Key: ")), 16)
    s.send(bytes(str(key), encoding='utf-8'))

    key_size = int(input(" - Key Size: "))
    s.send(bytes(str(key_size), encoding='utf-8'))

    block_size = int(input(" - Block size: "))
    s.send(bytes(str(block_size), encoding='utf-8'))

    plaintext = input(" - Plain text: ")
    s.send(bytes(str(plaintext), encoding='utf-8'))

