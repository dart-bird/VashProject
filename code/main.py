#!/usr/bin/python3

from pn532.api import PN532
from pygame import mixer
import pygame
from time import sleep

if __name__== "__main__":
    nfc = PN532()
    # setup the device
    nfc.setup(enable_logging=False)

    # keep reading until a value is returned   
    clock = pygame.time.Clock()
    while True:
        if(nfc.read()):
            read = nfc.read()
            print("New NFC READ!")
            print(read)
            mixer.init()
            mixer.music.load('./audio/finish.mp3')
            mixer.music.play()
            while pygame.mixer.music.get_busy():
                clock.tick(1000)
            pygame.mixer.music.stop()
            mixer.init()
            mixer.music.load('./audio/1_run.mp3')
            mixer.music.play()

        