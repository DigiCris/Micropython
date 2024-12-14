from machine import Pin, PWM, ADC
import time

adc = ADC(0)  # Inicializa el ADC en el canal 0
led = Pin(2, Pin.OUT)

# Configurar PWM en el pin GPIO2
pwm = PWM(led)
pwm.freq(1000)  # Establecer frecuencia a 1 kHz

for n in range(20):
    pwm.duty(adc.read())  # Ajustar el ciclo de trabajo
    time.sleep(1)   # Esperar 1 segundo
    
pwm.duty(1023)  # Ajustar el ciclo de trabajo

