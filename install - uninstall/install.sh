#!/bin/bash

echo "Welcome to the Crypto Printer V2 auto installer !"
echo "Starting ..."

cd ~

echo " "
echo "Getting update list ..."
sudo apt-get update

echo " "
echo "Installing pip for python 3 ..."
sudo apt-get install python3-pip -y

echo " "
echo "Installing git, cups, wiringpi, build-essential, libcups2-dev, libcupsimage2-dev, python-serial, python-pil and python-unidecode"
sudo apt-get install git cups wiringpi build-essential libcups2-dev libcupsimage2-dev python-serial python-pil python-unidecode -y

echo " "
echo "Cloning adafruit driver for thr ZJ-58 thermal printer ..."
git clone https://github.com/adafruit/zj-58

echo " "
echo "Installing adafruit driver for thr ZJ-58 thermal printer ..."
cd zj-58
make
sudo ./install

echo " "
echo "Setting the thermal printer as the default printer for the system ..."
sudo lpadmin -p ZJ-58 -E -v serial:/dev/serial0?baud=19200 -m zjiang/ZJ-58.ppd
sudo lpoptions -d ZJ-58

cd ~

echo " "
echo "Installing the pycoingecko and gpiozero python libraries (With pip for python 3) ..."
pip3 install pycoingecko
pip3 install gpiozero

echo " "
echo "Cloning the thermal printer library and the main code from the Crypto Printer V2 github repo ..."
git clone https://github.com/samyarsadat/crypto_printer_v2

echo " "
echo "Installation completed successfuly !"
echo "Closing in 20 seconds"
sleep 20
