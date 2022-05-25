# echo-client.py

import socket
import re

def user_input_key(): #input the key from the console
    tha_key = str(input('Enter a 64-bit key: '))
    if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
            return tha_key
    else:
            while(len(tha_key) != 64 and not re.match("^([01])+", tha_key)):
                    if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
                            return tha_key
                    tha_key = str(input('Enter a 64-bit key: '))
    return tha_key

def user_input_plaintext(): #input plaintext in console
    try:
            someIn = str(input('Enter the plaintext: '))
    except:
             someIn = str(input('Try again: '))
    return someIn


HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    key = str(user_input_key())
    s.send(bytes(key, encoding='utf-8'))

    plaintext = str(user_input_plaintext())
    s.send(bytes(plaintext, encoding ='utf-8'))
    
