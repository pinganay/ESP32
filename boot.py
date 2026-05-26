# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import neopixel
from machine import Pin
from utime import sleep

led_pin = Pin(8, Pin.OUT) 

np = neopixel.NeoPixel(led_pin, 1)

np[0] = (50, 0, 0)
np.write()
sleep(0.5)

np[0] = (0, 50, 0)
np.write()
sleep(0.5)

np[0] = (0, 0, 50)
np.write()
sleep(0.5)

np[0] = (50, 50, 50)
np.write()
sleep(0.5)

np[0] = (0, 0, 0)
np.write()
sleep(0.5)