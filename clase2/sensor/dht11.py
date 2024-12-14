#p1=3v
#p2=d => GPIO4=D2
#p4=gnd

import dht
from machine import Pin

# Crear objeto para el DHT11
d = dht.DHT11(Pin(4))  # Cambia a DHT22 si usas ese sensor

# Medir
d.measure()  # Pedir medición

# Obtener temperatura y humedad
temperature = d.temperature()  # Pedir temperatura
humidity = d.humidity()        # Pedir humedad

# Imprimir resultados
print("Temperatura: {} °C".format(temperature))
print("Humedad: {} %".format(humidity))
