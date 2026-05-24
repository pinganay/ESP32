#This program lets you check temperature and humidity with a DHT22 sensor
#The dht module is built into micropython, so you can directly import it without installing a driver file.
#Connect + pin on sensor to 5v, - pin on sensor to Ground, Out pin on sensor to GPIO 9
#DHT22 does not work with 3.3v, use 5v instead
#When connected to 3.3V, this error shows up "OSError: [Errno 116] ETIMEDOUT"

from dht import DHT22
from machine import Pin
from time import sleep

dht22 = DHT22(Pin(9))

while True:
    sleep(0.5)
    dht22.measure()
    temp = dht22.temperature()
    humidity = dht22.humidity()
    print(f"Temp: {temp}°C  Humidity: {humidity}%")
