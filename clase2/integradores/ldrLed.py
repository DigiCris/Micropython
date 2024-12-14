from machine import Pin
from machine import ADC
import time

adc = ADC(0)  # Inicializa el ADC en el canal 0
led = Pin(2,Pin.OUT)

while True:
    val = adc.read()
    if val>=512:
        led.off()
    else:
        led.on()