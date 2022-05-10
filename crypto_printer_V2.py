# Written by Samyar Sadat Akhavi.

# Libraries :
from pycoingecko import CoinGeckoAPI
from Adafruit_Thermal import *
from gpiozero import Button, LED
import datetime
import socket
import time

cg = CoinGeckoAPI()
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout = 5)


# The main program:
# Variables:
button = Button(23)
led = LED(24)

led.off()

# Functions:
def internet_stat():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True

    except Exception:
        return False
        

if internet_stat():
    print("INTERNET CONNECTED!")
    print(" ")
    time.sleep(1)

else:  
    led.off()
    print("NO INTERNET !")
    print("Waiting for internet connection...")
    
    while True:
        if internet_stat():
            print("INTERNET CONNECTED!")
            print(" ")
            time.sleep(1)
            break
        
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
 

# Main loop:
while True:
    currency = "usd"
            
    if not internet_stat():   
        led.off()
        print("INTERNET DISCONNECTED!")
        print("Waiting for internet connection...")
        
        while True:
            if internet_stat():
                print("INTERNET RE-CONNECTED!")
                print(" ")
                time.sleep(1)
                break
            
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
            
    if button.is_pressed:
        led.on()
        
        print("Button pressed!")
        print("Requesting prices from the API...")
        print("")
        
        print("Getting bitcoin")
        bitcoin = cg.get_price(ids = "bitcoin", vs_currencies = currency)
        
        time.sleep(0.6)
        
        print("Getting ethereum")
        ethereum = cg.get_price(ids = "ethereum", vs_currencies = currency)
        
        time.sleep(0.6)
        
        print("Getting binance coin")
        binance = cg.get_price(ids = "binance coin", vs_currencies = currency)
        
        time.sleep(0.6)
        
        print("Getting cardano")
        cardano = cg.get_price(ids = "cardano", vs_currencies = currency)
        
        print("Done !")
        print("Converting data to numbers ...")
        print("")
        
        bitcoin = bitcoin["bitcoin"]
        bitcoin = bitcoin[currency]
        print("Price of bitcoin: ", bitcoin)
        
        ethereum = ethereum["ethereum"]
        ethereum = ethereum[currency]
        print("Price of ethereum: ", ethereum)
        
        binance = binance["binancecoin"]
        binance = binance[currency]
        print("Price of binance coin: ", binance)
        
        cardano = cardano["cardano"]
        cardano = cardano[currency]
        print("Price of cardano: ", cardano)
        
        print("Currency: ", currency.upper())
        
        current_time = datetime.datetime.now()
        print("Current date and time: ", current_time)
        print("")
        
        print("Done!")
        print("Starting to print...")
        
        printer.setSize("M")
        printer.justify("C")
        printer.println("The Crypto Printer REV 2.0")
        
        printer.setSize("S")
        printer.println("By Samyar Sadat Akhavi")
        
        printer.feed(2)
        
        printer.justify("L")
        printer.println("Source : CoinGecko")
        printer.print("Currency : ")
        printer.println(currency.upper())
        
        printer.feed(1)
        
        printer.setSize("M")
        printer.println("The Prices:")
        
        printer.setSize("S")
        
        printer.print("1. Bitcoin: ")
        printer.println(bitcoin)
        
        printer.print("2. Ethereum: ")
        printer.println(ethereum)
        
        printer.print("3. Binance Coin: ")
        printer.println(binance)
        
        printer.print("4. Cardano: ")
        printer.println(cardano)
        
        printer.feed(1)
        
        printer.println("Time and date: ")
        printer.boldOn()
        printer.println(current_time)
        printer.boldOff()
        
        printer.feed(2)
        
        printer.justify("C")
        printer.println("Have a nice day!")
        
        printer.feed(3)
        
        print("Printing done!")
        print("Complete!")
        print("")
        
        led.off() 
        
    led.on()
    time.sleep(0.02)
    led.off()
    time.sleep(0.02)
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        

    
