import time
from machine import ADC

adc = ADC(0)  # Inicializa el ADC en el canal 0

for n in range(10):
    print(adc.read())  # Usa adc.read() para obtener el valor
    time.sleep(1)