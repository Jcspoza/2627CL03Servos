# Taller Programación y Robótica en CMM BML – 2026-2027
# Lesson / Project : Servos cin POO y con POO
# Goal : CALIBRATION of servo SG90 from 0º - 180º - with 3 parameters
# Goal cont: to discover the 0º 90º and 180º, correspondence in microseconds
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
# 1.0 + try - except


from machine import Pin, PWM
from time import sleep_ms


# Informative block - Start
p_ucontroler = "Pico _,W,2,2W"
p_HWdesc = "Servo SG90 on GPIO15 PWM 50Hz"
p_keyLib = "machine -> PWM"
p_project = "SG90-servo CALIBRATION"
p_file = "R2627_servo_calibra_v1_0.py"
p_version = "1.0"
print(f"Project: {p_project} - Version: {p_version}")
print(f"Extra HW & connections : {p_HWdesc}")
print(f"Key library : {p_keyLib}")
print(f"Fichero del script : {p_file}")
print(f"Valid for Microcontroler: {p_ucontroler}")
# Informative block - End


# 3 sentences Convers External servo pin in an output pin to control a servo
SERVO_PIN = 15
servo = PWM(Pin(SERVO_PIN))
servo.freq(50)

print('''Programa para calibrar un Servo
Da valores en microsegundos entre 500 y 2700,
para observar donde acaba el recorriodo del servo de 0 a 180º.
Tambien prueba con 1500 a ver si corresponde a 90º.
Apunta estos 3 valores para programas de uso del ese Servo.''')

us_servo = 1500  # ussually correspond to 90º
try:
    while True:
        servo.duty_ns(us_servo*1000)
        us_servo = int(input("Microseg servo (700 a 2600)= "))

except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    sleep_ms(100)
    servo.deinit()
servo.deinit()
