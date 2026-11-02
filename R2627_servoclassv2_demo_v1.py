# Taller Programación y Robótica en CMM BML – 2026-2027
# Lesson / Project : Servos sin POO y con POO
# Goal : Demo of servo 0º - 180º SG90 - using class Servo v2
# Hardware platform: Pico _,2, 2W & W / funciona igual sin cambios
# Montaje #1 : Servo Vcc = +5vol / GDN - GND / Signal - GPIO15
# Librerias : Servo v2
# Ref librerias: yes
# Autor y Fecha: https://github.com/Jcspoza - 2026 10
# Licencia : CC BY-NC-SA 4.0
# References

# Informative block - Start
p_ucontroler = "Pico _,W,2,2W"
p_HWdesc = "Servo SG90 on GPIO15 PWM 50Hz"
p_keyLib = "Servo v2"
p_project = "SG90-servo demo - with lib Servo v2 "
p_file = "R2627_servoclassv2_demo_v1.py"
p_version = "1.0"
print(f"Project: {p_project} - Version: {p_version}")
print(f"Extra HW & connections : {p_HWdesc}")
print(f"Key library : {p_keyLib}")
print(f"Fichero del script : {p_file}")
print(f"Valid for Microcontroler: {p_ucontroler}")
# Informative block - End

from LibServo180v2 import *
from time import sleep_ms

servo = Servo(15, 600, 2550, 1550)
DELAY = 20

servo.angle = 0 # initial position 0º
try:    
    while True:
        # Move servo from 0° to 180°
        for deg in range(0, 181, 1):
            servo.angle = deg
            sleep_ms(DELAY)
        # Move servo from 180° back to 0°
        for deg in range(180, -1, -1):
            servo.angle = deg
            sleep_ms(DELAY)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    sleep_ms(1000)
    
    
servo.off()