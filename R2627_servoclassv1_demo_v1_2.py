# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 3 - 21
# Goal : Servo SG90 on GPIO15 - using servo class
# Ref : https://picockpit.com/raspberry-pi/es/how-to-control-servo-with-raspberry-pi-pico-w-and-pulse-width-modulation-pwm/
# 1.0 -> 1.1 : add center setting for 90º
# 1.1 -> 1.2 import Servo class V1

from LibServo180v1 import *
from time import sleep_ms

# Informative block - start
p_ucontroler = "Pico W"
p_keyOhw = "Servo SG90 on GPIO15"
p_project = "SG90 - Servo class 1st"
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

servo = Servo(600,1550,2550,pin=15)
DELAY = 20

servo.RotateDeg(0) # initial position 0º
try:    
    while True:
        # Move servo from 0° to 180°
        for deg in range(0, 181, 1):
            servo.RotateDeg(deg)
            sleep_ms(DELAY)
        # Move servo from 180° back to 0°
        for deg in range(180, -1, -1):
            servo.RotateDeg(deg)
            sleep_ms(DELAY)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    sleep_ms(1000)
    
    
servo.off()