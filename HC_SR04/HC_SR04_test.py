#The code below use a HC-SR04 driver from awesome-micropython
#This code uses the HC-SR04 sensor to detect distance using ultrasonic waves in millimeters
#Connect Vcc pin on the sensor to 5v pin on the ESP32 , Gnd on the sensor to Gnd on the ESP32, echo pin on sensor to GPIO 1 on the ESP32, and trig pin on the sensor to GPIO 0 on the ESP32


from HC_SR04.HC_SR04_driver import HCSR04
from machine import Pin
from utime import sleep

sensor = HCSR04(trigger_pin=Pin(0), echo_pin=Pin(1))

while True:
    #Uncomment the line below to see the distance in centimeters
    #print("Distance:", sensor.distance_cm(), "cm")
    print("Distance:", sensor.distance_mm(), "mm")
    sleep(0.1)