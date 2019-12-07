## PN532 NFC Module

* Install Adafruit Python PN532:

```
sudo apt-get update
sudo apt-get install build-essential python-dev git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PN532.git
cd Adafruit_Python_PN532
sudo python setup.py install
```

* Clone rpi-examples:

```
cd ~
git clone https://github.com/leon-anavi/rpi-examples.git
```

* Save data to RFID/NFC card

```
cd ~/rpi-examples/PN532/python
sudo python rfid-save.py
```

* Listen and scan for RFID/NFC cards

```
cd ~/rpi-examples/PN532/python
sudo python rfid-scan.py
```