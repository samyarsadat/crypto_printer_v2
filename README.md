# Crypto Printer V2
Get a paper hard copy of the price for some crypto currencies at the push of a button.

# Documentation in progress !

## Components :

1. Raspberry Pi 4B 4GB RAM (Tested on a pi4, but it should also work with a pi3 or pi2)
2. [Mini Thermal Receipt Printer](https://www.adafruit.com/product/597) (From adafruit)
3. 2 Pin momentary push button 
4. 5mm LED (Any color)
6. 9V 2A Power supply
7. 16GB (or higher) class 10 micro SD card
8. A suitable 5V power supply for the Raspberry Pi
9. A mouse and keyboard for the Raspberry Pi
10. A suitable HDMI cable for the Raspberry Pi
11. A suitable display or monitor for the Raspberry Pi

**For Raspberry Pi 2 users (Without wifi) :**
1. Option : A USB wifi dongle
2. Option : A direct connection with an ethernet cable
    
    
    
## Hardware :
### Wiring diagram :

![wiring_diagram_v2](https://user-images.githubusercontent.com/79406608/113473772-53eb9f80-9474-11eb-8e1f-35f840ca145b.jpg)


The thermal printer's RX pin (usualy the yellow wire) connects to GPIO 14 on the Raspberry pi. 
**DO NOT CONNECT THE TX (USUALY GREEN) WIRE OF THE THERMAL PRINTER TO THE PI. IT IS 5V AND IT MIGHT PERMANENTLY DAMAGE YOUR RASPBERRY PI.**

The led's cathode connects to a ground (GND) pin on the pi and the anode to GPIO 24.

One of the pins on the button connects to a ground (GND) pin on the pi and the other to GPIO 23.

## Software :
