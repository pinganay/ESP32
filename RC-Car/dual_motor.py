from machine import Pin as gpio, PWM
import time

class Motor():
    
    def __init__(self, enable_pin, in1_pin, in2_pin):
        self.enable = gpio(enable_pin, gpio.OUT)
        self.in1 = gpio(in1_pin, gpio.OUT)
        self.in2 = gpio(in2_pin, gpio.OUT)
    
    def stop_1(self):
        self.enable.off()
        self.in1.off()
        self.in2.off()
        print("Stopped")
    

    def forward(self, ms):
        self.enable.on()
        print("enable1 on")
        self.in1.on()
        print("input1 on")
        self.in2.off()
        print("input2 off")
        time.sleep_ms(ms)
        self.stop_1()

    def backward(self, ms):
        self.enable.on()
        print("enable1 on")
        self.in1.off()
        print("input1 off")
        self.in2.on()
        print("input2 on")
        time.sleep_ms(ms)
        self.stop_1()

enable_pin_1 = gpio(0, gpio.OUT)
in1_pin_1 = gpio(1, gpio.OUT)
in2 = gpio(4, gpio.OUT)

motor1 = Motor(0, 1, 4)
motor2 = Motor(10, 5, 6)

motor1.forward(2000)
motor1.backward(2000)

motor2.forward(2000)
motor2.backward(2000)

