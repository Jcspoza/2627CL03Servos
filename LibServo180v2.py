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
# https://www.luisllamas.es/micropython-servomotores-pwm/
# 1.0 -> 1.1 : add center setting for 90º
# 2.0 varios cambios despues de ejemplos inspirados por copilot-IA

from machine import Pin, PWM

class Servo:
    def __init__(self, pin_num=15, c0degus=500, c180degus=2500, c90degus=None):
        """
        pin_num : GPIO conectado al servo
        c0degus  : pulso correspondiente a 0°, obtenido en calibracion
        c180degus  : pulso correspondiente a 180°, obtenido en calibnracion
        c90degus  : pulso correspondiente a 90°, obtenido en calibracion
            o mitad entre 0 y 180º
        """
        self.spwm = PWM(Pin(pin_num))
        self.spwm.freq(50)
        self.MIN_DUTY_ns = c0degus * 1000 # time pulse for 0 deg
        self.MAX_DUTY_ns = c180degus * 1000 # time pulse for 180 deg
        if c90degus is None: # time pulse for 90 deg
            self.CEN_DUTY_ns = (c0degus + (c180degus - c0degus)/2) * 1000
        else:
            self.CEN_DUTY_ns = c90degus * 1000 # time pulse for 90 deg
            
        self._angle = 90
        self._dutyns = 0
            
    def relax(self):
        self.spwm.duty_ns(0)
        
    def off(self):
        self.spwm.deinit()

    def WriteAngle(self, deg, show=False):
        
        deg = max(0, min(180, deg))
        #   
        if deg < 90:
            self._dutyns = int(self.MIN_DUTY_ns + deg * (self.CEN_DUTY_ns - self.MIN_DUTY_ns) / 90)    
        else:
            self._dutyns = int(self.CEN_DUTY_ns + (deg-90) * (self.MAX_DUTY_ns - self.CEN_DUTY_ns) / 90)
                      
        self.spwm.duty_ns(self._dutyns) # move servo to new position
        self._angle = deg
        if show:
            print(f"Grados: {self._angle} - Duty nanoseconds : {self._dutyns}")

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self.WriteAngle(value)
