## Clone VashProject
git clone: ```git clone https://github.com/krumaska/VashProject.git```

## Installing

`sudo apt-get update`

`sudo apt-get upgrade`

`sudo apt-get install libusb-dev libpcsclite-dev i2c-tools`

`sudo pip3 install gTTS`

`sudo pip3 install pygame`

`cd VashProject`

`make init`

## RUN
First, check i2c connects: `i2cdetect -y 1`

`python3 ~/VashProject/main.py`

## ETC
- [PN532 example](https://github.com/hoanhan101/pn532)
- [PN532 Setting Pin](http://wiki.sunfounder.cc/index.php?title=PN532_NFC_Module_for_Raspberry_Pi)
- [TTS](https://wikidocs.net/15213)