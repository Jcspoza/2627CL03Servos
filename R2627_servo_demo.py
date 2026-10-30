# Taller Programación y Robótica en CMM BML – 2026-2027
# Lesson / Project : Servos cin POO y con POO
# Goal : Demo of servo 0º - 180º SG90
# Hardware platform: Pico _,2, 2W & W / funciona igual sin cambios
# Montaje #1 : Servo Vcc = +5vol / GDN - GND / Signal - GPIO15
# Librerias : machine -> PWM
# Ref librerias: no
# Autor y Fecha: https://github.com/Jcspoza - 2026 10
# Licencia : CC BY-NC-SA 4.0
# References
#1 https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_servo.html#py-servo

# Informative block - Start
p_ucontroler = "Pico _,W,2,2W"
p_HWdesc = "Servo SG90 on GPIO15 PWM 50Hz"
p_keyLib = "machine -> PWM"
p_project = "SG90-servo demo "
p_file = "R2627_servo_demo.py"
p_version = "1.0"
print(f"Project: {p_project} - Version: {p_version}")
print(f"Extra HW & connections : {p_HWdesc}")
print(f"Key library : {p_keyLib}")
print(f"Fichero del script : {p_file}")
print(f"Valid for Microcontroler: {p_ucontroler}")
# Informative block - End

import machine
import utime

# Initialize PWM on pin GP15
SERVO_PIN = 15
servo = PWM(Pin(SERVO_PIN))
servo.freq(50) # Set the frequency to 50Hz

# Function to map angle to duty cycle
def angle_to_duty(angle):
    min_duty = 1638  # Corresponds to 0.5ms pulse (0°)
    max_duty = 8192  # Corresponds to 2.5ms pulse (180°)
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    return duty
try:    
    while True:
        # Move servo from 0° to 180°
        for angle in range(0, 181, 1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(10)
        # Move servo from 180° back to 0°
        for angle in range(180, -1, -1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(10)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM
    sleep_ms(100)
    servo.deinit()
servo.deinit()