#!/usr/bin/python3

from pn532.api import PN532


if __name__== "__main__":
    nfc = PN532()

    # setup the device
    nfc.setup(enable_logging=False)

    # keep reading until a value is returned
    while True:
        if(nfc.read()):
            read = nfc.read()
            print("New NFC READ!")
            print(read)