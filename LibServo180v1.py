# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 3 - 21
# Goal : Sevo SG90 class
# Ref : https://picockpit.com/raspberry-pi/es/how-to-control-servo-with-raspberry-pi-pico-w-and-pulse-width-modulation-pwm/
# 1.0 -> 1.1 : add center setting for 90º

from machine import Pin, PWM

class Servo:
    def __init__(self, c0degus=700, c90degus=1500, c180degus=2500, pin=15, freq=50):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.MIN_DUTY_ns = c0degus * 1000 # time pulse for 0 deg
        self.CEN_DUTY_ns = c90degus * 1000 # time pulse for 90 deg
        self.MAX_DUTY_ns = c180degus * 1000 # time pulse for 180 deg
        
    def RotateDeg(self, deg, show=False):    
        if deg < 0:
            deg = 0
    
        if deg > 180:
            deg = 180
        
        if deg < 90:
            duty_ns = int(self.MIN_DUTY_ns + deg * (self.CEN_DUTY_ns - self.MIN_DUTY_ns) / 90)    
        else:
            duty_ns = int(self.CEN_DUTY_ns + (deg-90) * (self.MAX_DUTY_ns - self.CEN_DUTY_ns) / 90)
        
        if show:
            print(f"Grados: {deg} - Duty nanosconds : {duty_ns}")
        self.pwm.duty_ns(duty_ns)
        
    def ShowDuty_ns(self):
        return self.pwm.duty_ns()
    
    def off(self):
        self.pwm.deinit()
