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

**First you must install Raspberry Pi OS on to your micro SD card and then insert it in to your Raspberry Pi.                                                                   
If you don't know how to do this, [Click here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up).**

Next download the installation file :
[install.zip](https://github.com/samyarsadat/crypto_printer_v2/files/6252267/install.zip)

Unzip it on your Raspberry Pi and then double click on **install.sh**. something like this will apear :                                                                        
**If you don't know how to unzip zip files on the pi, [Click here](https://magpi.raspberrypi.org/articles/unzip-and-uncompress-files-on-a-raspberry-pi).**

![2021-04-02-235737_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113474279-c3af5980-9477-11eb-809d-b3d89b798797.png)

Click on "Execute in Terminal". A terminal window will open. Now just wait for all of the libraries and files to be installed.

![2021-04-02-235742_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113474394-6c5db900-9478-11eb-8fca-86f06de5c389.png)

When the installation is completed, you should get a message in the terminal saying "Installation completed successfuly !" "Closing in 20 seconds" 

After that there is only one small thing left to do; Configuring the serial port on the pi :                                                                                     
First open a terminal window. The terminal icon looks like this :    

![Terminal icon](https://user-images.githubusercontent.com/79406608/113474972-aed4c500-947b-11eb-99c3-81124b9149e9.png)

Next type `sudo raspi-config` in the terminal and hit enter :                                                                                                                                                                                        

![2021-04-03-000913_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475102-4b976280-947c-11eb-9cc6-d30caf199e33.png)

The conifiguration tool will open. press the down cursor key twice to select "3 Interface Options". Then hit enter :

![Untitled](https://user-images.githubusercontent.com/79406608/113475246-0de70980-947d-11eb-955d-9c5e50c46af4.png)

When the interface options menu opens, press the down cursor key 5 times to select "P6 Serial Port". Then hit enter :

![2021-04-03-000929_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475480-a205a080-947e-11eb-9d89-5737c7cbb53d.png)

Next this screen will apear. With your left and right cursor keys select No and hit enter :

![2021-04-03-000938_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475739-11c85b00-9480-11eb-90bb-7939810f36c1.png)

After that this screen will apear. With your left and right cursor keys select Yes and hit enter :

![2021-04-03-000942_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475794-46d4ad80-9480-11eb-80a9-8743c6fff674.png)

When this screen apears just hit enter :

![2021-04-03-000945_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475875-7aafd300-9480-11eb-9049-c6c13b912eea.png)





