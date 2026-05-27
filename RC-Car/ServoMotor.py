from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(9))

servo.freq(50)



def set_angle(angle):
    duty = int(((angle / 180) * (123 - 26)) + 26)
    servo.duty(duty)

# Loop to sweep back and forth

count = 0

while count != 100:
    for angle in range(0, 181, 10):
        set_angle(angle)
        sleep(0.1)
    for angle in range(180, -1, -10):
        set_angle(angle)
        sleep(0.1)
    
    count += 1

