# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

#REFERENCE FOR PWM: https://www.youtube.com/watch?v=KcOJSa2dNX4&t=8s




from machine import Pin as gpio, PWM
import time

class Motor():
    
    def __init__(self, enable_pin, in1_pin, in2_pin):
        self.enable = gpio(enable_pin, gpio.OUT)
        self.pwmInput = PWM(self.enable, freq=2500)
        self.in1 = gpio(in1_pin, gpio.OUT)
        self.in2 = gpio(in2_pin, gpio.OUT)
    
    def stop_1(self):
        self.pwmInput.duty(0) # Sets duty cycle to 0%, which means voltage is 0% of 3.3v, so speed is 0
        self.in1.off()
        self.in2.off()
        print("Stopped")
    

    def forward(self, ms, speed):
        self.pwmInput.duty(int((speed/100)*1023)) #Sets duty cycle to input (speed), which means the voltage is increased from 0 to the input divided by 100, which means the speed is increased
        print("enable1 on")
        self.in1.on()
        print("input1 on")
        self.in2.off()
        print("input2 off")
        time.sleep_ms(ms)
        self.stop_1()

    def backward(self, ms, speed):
        self.pwmInput.duty(int((speed/100)*1023))
        print("enable1 on")
        self.in1.off()
        print("input1 off")
        self.in2.on()
        print("input2 on")
        time.sleep_ms(ms)
        self.stop_1()
        
        
    def forward_no_stop(self, speed):
        self.pwmInput.duty(int((speed/100)*1023)) #Sets duty cycle to input (speed), which means the voltage is increased from 0 to the input divided by 100, which means the speed is increased
        print("enable1 on")
        self.in1.on()
        print("input1 on")
        self.in2.off()
        print("input2 off")
        
    def backward_no_stop(self, speed):
        self.pwmInput.duty(int((speed/100)*1023))
        print("enable1 on")
        self.in1.off()
        print("input1 off")
        self.in2.on()
        print("input2 on")
        


class Dual_Motor:
    def __init__(self, L_motor, R_motor):
        self.L_motor = L_motor
        self.R_motor = R_motor
        
    def straight_forward(self, ms, speed):
        self.L_motor.forward_no_stop(speed)
        self.R_motor.forward_no_stop(speed)
        time.sleep_ms(ms)
        self.L_motor.stop_1()
        self.R_motor.stop_1()
        
    def straight_backward(self, ms, speed):
        self.L_motor.backward_no_stop(speed)
        self.R_motor.backward_no_stop(speed)
        time.sleep_ms(ms)
        self.L_motor.stop_1()
        self.R_motor.stop_1()
        
    def turn_left(self, ms, speed):
        self.L_motor.backward_no_stop(speed)
        self.R_motor.forward_no_stop(speed)
        time.sleep_ms(ms)
        self.L_motor.stop_1()
        self.R_motor.stop_1()
        
    def turn_right(self, ms, speed):
        self.L_motor.forward_no_stop(speed)
        self.R_motor.backward_no_stop(speed)
        time.sleep_ms(ms)
        self.L_motor.stop_1()
        self.R_motor.stop_1()
        
        
        
        
L_motor = Motor(0, 1, 4)
R_motor = Motor(11, 5, 6)

# L_motor.forward(5000, 75)
# L_motor.forward(5000, 100)
# time.sleep_ms(2000)
# L_motor.backward(5000, 75)
# L_motor.backward(5000, 100)
# 
# R_motor.forward(5000, 75)
# R_motor.forward(5000, 100)
# time.sleep_ms(2000)
# R_motor.backward(5000, 75)
# R_motor.backward(5000, 100)

dual_motor = Dual_Motor(L_motor, R_motor)


dual_motor.straight_forward(3000, 100)
time.sleep_ms(1000)
dual_motor.straight_backward(3000, 100)
time.sleep_ms(1000)
dual_motor.turn_right(3000, 100)
time.sleep_ms(1000)
dual_motor.turn_left(3000, 100)

