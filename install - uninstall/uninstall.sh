#!/bin/bash

echo "Welcome to the Crypto Printer V2 auto uninstaller !"
echo "Starting ..."

cd ~

echo " "
echo "Removing adafruit driver for thr ZJ-58 thermal printer ..."
rm -R -f zj-58

echo " "
echo "Deleting the folder (directory) called Crypto_Printer_V2 ..."
rm -R -f Crypto_Printer_V2

echo " "
echo "Uninstallation completed successfuly !"
echo "Closing in 20 seconds."
sleep 20


