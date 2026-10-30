# 2627CL03_Servos - sin y con POO <u>clase en borrador</u>

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/26_27Prog_RobotCMMBML_Index: Indice - Taller Programacion y Robotica 2026 - 2027 en CMM Benito Martin Lozano · GitHub](https://github.com/Jcspoza/26_27Prog_RobotCMMBML_Index)

## Clase x : Robotica Servos- Resumen inicial

### Tópicos que se van a cubrir

1. Que es un servo 0-180º y como controlarlo con ondas cuadradas PWM
   
   1. Hoja de datos del servo mas típico de robotica [SG90](SG90_a.pdf)
   
   2. Básico sobre señal de control PWM

2. Calibración de servos 0-180º

3. Control de servo ( sin usar POO)

4. Iniciación a POO : Programación orientada a objetos

5. Control de servos con POO

#### Materiales necesarios

| Material      | Descripcion | Kit SF | Montaje |
| ------------- | ----------- | ------ | ------- |
| uC PICO       |             | SI     |         |
| Servo 0-180º  |             | SI     |         |
| Cables dupond |             | SI     |         |
| Protoboard    |             | SI     |         |

### Montaje usado en esta clase ServoM#1

Alimentar el servo a +5volt y conectar el cable de control del servo SIG al GPIO15 o pin 20 lado izquierdo de la PICO.

![](.\wiring_swing_servo.webp)

### Enlaces a tutoriales e información

| Tutorial                                                                                                                                 | Nivel  | Notas                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------------------------------------------------------------- |
| [Tutorial SF servo](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_servo.html)                           | Básico | programa : [R2627_servo_demo.py](R2627_servo_demo.py)           |
| https://www.luisllamas.es/micropython-servomotores-pwm/                                                                                  | Medio  |                                                                 |
| https://learn.sparkfun.com/tutorials/hobby-servo-tutorial/                                                                               |        | Muy completo                                                    |
| https://robots-argentina.com.ar/didactica/manejo-preciso-de-servos-en-arduino-grados-y-milisegundos/                                     |        | Para explicar calibración                                       |
| [tutorial de POO en nuestra referencia Python 'el libro de Python'](https://ellibrodepython.com/programacion-orientada-a-objetos-python) | Medio  | para explicar POO en Python, pero vale para micropython tambien |

### Programas importantes de la clase

| Programa                                                   | Montaje  | Objetivo                                                                    | Notas                      |
| ---------------------------------------------------------- | -------- | --------------------------------------------------------------------------- | -------------------------- |
| [R2627_servo_demo.py](R2627_servo_demo.py)                 | ServoM#1 | Ver movimiento de un servo                                                  | Sin calibrar               |
| [R2627_servo_calibra_v1_0.py](R2627_servo_calibra_v1_0.py) | ServoM#1 | Calibrar un servo de 0º a 180º con 3 parámetros                             |                            |
| [R2627_servo_in_deg_v1_4.py](R2627_servo_in_deg_v1_4.py)   | ServoM#1 | Mover de 0º a 180º un servo con precision usando los valores de calibracion | Calibrado con 3 parametros |

---

## Documentación de soporte

Clases 6 y 7 de robotica CMM BML de 2023

- Que es un servo 0-180º y como controlarlo con ondas cuadradas PWM
  
  1. Hoja de datos del servo mas típico de robotica [SG90](SG90_a.pdf)
  
  2. Básico sobre señal de control PWM

- Calibración de servos 0-180º

- Control de servo ( sin usar POO)

## Iniciación a POO : Programación orientada a objetos

Las entidades de la vida real se pueden modelar en Python como objetos, y a eso se le denomina **Programación orientada a objetos POO**

La definición de un modelo para ciertos objetos se denomina clase. —> es solo la definición NO crea ningún objeto, es como un molde

**Las clases tienen atributos y métodos**

- Los **atributos** son como propiedades dentro de las clases, que se guardan en variables. se definen con la sintaxis de las variables, dentro del cuerpo de definición una clase.

- Los **métodos**son como operaciones en los objetos de la case. Se definen con la sintaxis de las funciones, dentro del cuerpo de definición una clase.

- Hay un método especial que es el **constructor**: 
  El método constructor se define mediante la función `__init__()`  y establece explícitamente los valores predeterminados de los atributos, o asigna los valores de los atributos
  esenciales a través de argumentos de método `__init__()`

Ver el [tutorial  de POO en nuestra referencia Python 'el libro de Python'](https://ellibrodepython.com/programacion-orientada-a-objetos-python)

## Control de servos con POO

---

Todo:
