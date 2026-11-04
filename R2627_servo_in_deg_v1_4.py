# Taller Programación y Robótica en CMM BML – 2026-2027
# Lesson / Project : Servos cin POO y con POO
# Goal : Move servo SG90 from 0º - 180º - AFTER servo calibration with 3 parameters
# Hardware platform: Pico _,2, 2W & W / funciona igual sin cambios
# Montaje #1 : Servo Vcc = +5vol / GDN - GND / Signal - GPIO15
# Librerias : machine -> PWM
# Ref librerias: no
# Autor y Fecha: https://github.com/Jcspoza - 2026 10
# Licencia : CC BY-NC-SA 4.0
# References CL5 & CL6 2023 in BM Makers
# Note: servos SG90 has a lot of variation, usually 1500microseconds -> 90º
# but 0º can vary 500 - 800 microsec, and 180º can vary 2000 - 2600 microsec
# Ref : https://robots-argentina.com.ar/didactica/manejo-preciso-de-servos-en-arduino-grados-y-milisegundos/
# 1.1. to 1.4 change order of constants and Functions part + check isdigit + try - except

from machine import Pin, PWM
from time import sleep_ms

# Informative block - Start
p_ucontroler = "Pico _,W,2,2W"
p_HWdesc = "Servo SG90 on GPIO15 PWM 50Hz"
p_keyLib = "machine -> PWM"
p_project = "SG90-servo move degrees - AFTER calibration "
p_file = "R2627_servo_in_deg_v1_4.py"
p_version = "1.4"
print(f"Project: {p_project} - Version: {p_version}")
print(f"Extra HW & connections : {p_HWdesc}")
print(f"Key library : {p_keyLib}")
print(f"Fichero del script : {p_file}")
print(f"Valid for Microcontroler: {p_ucontroler}")
# Informative block - End

# START Constants and Functions section
# Following 3 values are obtained using 'Servo_calibra' program
SERVO_CALIBRA_0DEG = 600 # microsec correspond to 90
SERVO_CALIBRA_90DEG = 1550 # microsec correspond to 90
SERVO_CALIBRA_180DEG = 2550  # microsec correspond to 180

def ConverDeg_us(deg):
    if deg < 0 :
        deg = 0
    
    if deg > 180:
        deg = 180
        
    if deg < 90:
        return int(SERVO_CALIBRA_0DEG + deg * (SERVO_CALIBRA_90DEG - SERVO_CALIBRA_0DEG) / 90)    
    else:
        return int(SERVO_CALIBRA_90DEG + (deg-90) * (SERVO_CALIBRA_180DEG - SERVO_CALIBRA_90DEG) / 90)

# END Constants and Functions section

# Initialize PWM on pin GP15
SERVO_PIN = 15
servo = PWM(Pin(SERVO_PIN))
servo.freq(50) # Set the frequency to 50Hz


deg_servo = 90  # initial position
us_servo = ConverDeg_us(deg_servo)

try:
    while (True):
        servo.duty_ns(us_servo*1000)
        deg_servo_str = input("Deg servo (0 a 180)= ")
        if deg_servo_str.isdigit():
            deg_servo = int(deg_servo_str)
            if deg_servo >= 0 and deg_servo <= 180:
                us_servo = ConverDeg_us(deg_servo)
                print('Grados = ', deg_servo, 'corresponde a microsegundos = ', us_servo)
            else:
                print ('Error in Deg, out of range. Deg limitted to 0º or 180º')
        else:
            print(f"Invalid number or none: {deg_servo_str}")
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    sleep_ms(100)
    servo.deinit()
servo.deinit()