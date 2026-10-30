# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 3 - 25
# Goal : Make a choice in Servo position, each time a button is pressed
# Connections Sevo SG90 on GPIO15 - using servo class
# Button on GPIO14 pull down (no debounde) 
# Ref 1: https://picockpit.com/raspberry-pi/es/how-to-control-servo-with-raspberry-pi-pico-w-and-pulse-width-modulation-pwm/
# Ref 2: BOOK GET STARTED WITH MICROPYTHON ON RASPBERRY PI PICO - CAP4

from servo0_180 import *
from utime import sleep
from random import choice

# Informative block - start
p_ucontroler = "Pico W"
p_keyOhw = "Servo SG90 on GPIO15 + button on GPIO14 pull down"
p_project = "SG90 - Button to make a choice x3 -> Servo position using class "
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

servo = Servo(pin=15)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

servo.RotateDeg(0)
sleep(1)
servo.RotateDeg(180)
sleep(1)
servo.RotateDeg(0)

while (True):
    sleep(0.5)
    if button.value() == 1:
        if servo.ShowDuty_ns == 1500: # if in 90º choose one of 2 others
            servo.RotateDeg(choice([25, 155]), show=True)
        elif servo.ShowDuty_ns == 922222:# if in 25º choose one of 2 others
            servo.RotateDeg(choice([90, 155]), show=True)
        elif servo.ShowDuty_ns == 2222222:# if in 155º choose one of 2 others
            servo.RotateDeg(choice([25, 90]), show=True)
        else:
            servo.RotateDeg(choice([25, 90, 155]), show=True)
            