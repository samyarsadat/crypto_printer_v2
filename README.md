# Crypto Printer V2
Get a paper hard copy of the price for some crypto currencies at the push of a button.

## About :
Get a paper copy of the price for 4 crypto currencies :                                                                                                                         
**NOTE : The currency for the returned price is settable. For more info, please check the bottom of this document.**
1. Bitcoin
2. Ethereum
3. Binance coin
4. Cardano

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

The thermal printer's GND (black) wire connects to a ground (GND) pin on the pi.

The led's cathode connects to a ground (GND) pin on the pi and the anode to GPIO 24.

One of the pins on the button connects to a ground (GND) pin on the pi and the other to GPIO 23.


## Software :

**First you must install Raspberry Pi OS on to your micro SD card and then insert it in to your Raspberry Pi.                                                                   
If you don't know how to do this, [Click here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up).**

Next download the installation file :
[install.zip](https://github.com/samyarsadat/crypto_printer_v2/files/6252462/install.zip)


Unzip it on your Raspberry Pi and then right click on **install.sh**. Then click on properties. A window will open. Go to the prmissions tab and click on Execute. some options will appear. click on anyone and then click on OK :                                                                                                                             
**If you don't know how to unzip zip files on the pi, [Click here](https://magpi.raspberrypi.org/articles/unzip-and-uncompress-files-on-a-raspberry-pi).**

![2021-04-03-153841_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113479468-f6694a00-9497-11eb-81f7-d6ce0714912e.png)

Now double click on **install.sh**. something like this will appear :                                                                                            

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

Next this screen will apear. With the left and right cursor keys select No and hit enter :

![2021-04-03-000938_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475739-11c85b00-9480-11eb-90bb-7939810f36c1.png)

After that this screen will apear. With the left and right cursor keys select Yes and hit enter :

![2021-04-03-000942_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475794-46d4ad80-9480-11eb-80a9-8743c6fff674.png)

When this screen apears just hit enter :

![2021-04-03-000945_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475875-7aafd300-9480-11eb-9049-c6c13b912eea.png)

Next you will return to this screen. Here using the left and right cursor keys select Finish and hit enter :

![2021-04-03-000955_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113475952-f7db4800-9480-11eb-8872-4f4091c9d55a.png)

Then you will be prompted to reboot, using the left and right cursor keys select Yes and hit enter.                                                                             
If not then type this into the terminal : `sudo reboot now` and hit enter.                                                                                                       
Now the pi will reboot and the software installation will be completed !                                                                                                        

# Runing the code :
To run the code open a terminal window and type :                                                                                                                            
`cd crypto_printer_v2` hit enter. then type `python3 crypto_printer_V2.py` and hit enter. 

Now the code will start runing. To print the prices push the button and wait.                                                                                                   
**Due to the CoinGecko API's slow speed, the program might sometimes get stuck for a bit**                

**To stop the code you can close the terminal or hold the `ctrl` key and then press `c` on the keyboard. now you can release the `ctrl` key. (Or basically `ctrl + c`)**      

**To test the printer, instead of typing `python3 crypto_printer_V2.py` type `python3 printertest.py`**

# Modifying the code :
### Opening the code in the thonny python IDE :

The thonny python IDE by default comes with Raspberry Pi OS. You can view, edit and run python codes with thonny.                                                               
To open the main code for this project open the file manager on the pi. The file managers icon looks like this :

![file manager](https://user-images.githubusercontent.com/79406608/113502306-341bb080-9534-11eb-84ba-d866ed0c4bd1.png)

The file manager window will open. By default file manager opens in the directory that the crypto_printer_v2 folder is. Now open the crypto_printer_v2 folder :

![edited_1](https://user-images.githubusercontent.com/79406608/113502353-95438400-9534-11eb-9b01-8f000bfb3a7c.png)

Inside the folder there are 3 main python codes : 
1. Adafruit_Thermal.py (The "library" for the thermal printer from adafruit)
2. crypto_printer_V2.py (The main code for the project written by me)
3. printertest.py (The test code for the thermal printer from adafruit)                                                                                                         

The rest of the files and folders (directories) are for other purposes :
1. README.md (This file that you are reading right now)
2. gfx (The bitmaps and graphics for the printertest.py code)
3. Wiring (The wiring diagram for this project in .JPG image format and .FZZ fritzing format)
4. install - uninstall (Contains install.sh and uninstall.sh. to run these, follow the steps above for runing install.sh (follow the same steps for uninstall.sh))

![edited_2](https://user-images.githubusercontent.com/79406608/113502577-d5573680-9535-11eb-857b-9886811be490.png)

To open the python code files (.py), right click on them and then click on Thonny python IDE. Now thonny will open and you can edit the code :

![2021-04-03-194243_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113503168-c756e500-9538-11eb-85f9-537396f8cdd9.png)

To save your changes click the Save button :

![thonny 1](https://user-images.githubusercontent.com/79406608/113503245-4ba96800-9539-11eb-8145-31ddba299a1f.png)

To run the code click the Run button and to stop the code click the Stop button :

![thonny 2](https://user-images.githubusercontent.com/79406608/113503296-9c20c580-9539-11eb-9847-55d035403813.png)

**For more information about thonny, [Click here](https://magpi.raspberrypi.org/articles/thonny).**

### Changing the currency of prices :

You can change the currency that the prices are printed in.                                                                                                                     
To do this, open the main (crypto_printer_V2.py) code in thonny (as described above) and scroll down to line 72 :                                                               

![2021-04-03-194317_1920x1080_scrot](https://user-images.githubusercontent.com/79406608/113505999-c62eb380-954a-11eb-8f63-013f74c45cfb.png)

Here you can change the three letters inside the single quotation marks. You can change it to any currency as long as CoinGecko supports it.                                     

Here is the list of supported currencies :                                                                                                                                       
**NOTE : Some of these currencies are actualy crypto currencies themselvs; So as well as normal currencies you can get the prices in some crypto currencies.**

Some popular currencies :
1. usd (US dollars)
2. eur (Euro)
3. cad (Canadian dollars)
4. aud (Australian dollars)
5. btc (Bitcoin)
6. eth (Ethereum)

The rest of supported crypto and normal currencies :
1. ltc
2. bch
3. bnb
4. eos
5. xrp
6. xlm
7. link
8. dot
9. yfi
10. aed
11. ars
12. bdt
13. bhd
14. bmd
15. brl
16. chf
17. clp
18. cny
19. czk
20. dkk
21. gbp
22. hkd
23. huf
24. idr
25. ils
26. inr
27. jpy
28. krw
29. kwd
30. lkr
31. mmk
32. mxn
33. myr
34. ngn
35. nok
36. nzd
37. php
38. pkr
39. pln
40. rub
41. sar
42. sek
43. sgd
44. thb
45. try
46. twd
47. uah
48. vef
49. vnd
50. zar
51. xdr
52. xag
53. xau
54. bits
55. sats

After you have made your changes, save the code with the Save button and run it with the Run button.                                                                             
__*Thanks for following allong and reading this document. I hope that you have enjoyed this project. Have a nice day :)*__
