from machine import Pin, PWM
import time

# Configurar el pin GPIO2 como salida
led = Pin(2, Pin.OUT)

# Configurar PWM en el pin GPIO2
pwm = PWM(led)
pwm.freq(1000)  # Establecer frecuencia a 1 kHz

for n in range(3):
    pwm.duty(0)  # Ajustar el ciclo de trabajo
    time.sleep(1)   # Esperar 1 segundo
    pwm.duty(512)  # Ajustar el ciclo de trabajo
    time.sleep(1)   # Esperar 1 segundo
    pwm.duty(1023)  # Ajustar el ciclo de trabajo
    time.sleep(1)   # Esperar 1 segundo
    
pwm.duty(1023)  # Ajustar el ciclo de trabajo
