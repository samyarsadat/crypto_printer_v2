#!/bin/bash

echo "Welcome to the Crypto Printer V2 auto uninstaller !"
echo "Starting ..."

cd ~

echo " "
echo "Removing adafruit driver for the ZJ-58 thermal printer ..."
rm -R -f zj-58

echo " "
echo "Deleting the folder (directory) called crypto_printer_v2 ..."
rm -R -f crypto_printer_v2

echo " "
echo "Uninstallation completed successfuly !"
echo "Closing in 20 seconds."
sleep 20


