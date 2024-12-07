import machine
import time


led_rojo = machine.Pin(16,machine.Pin.OUT)
led_azul = machine.Pin(2,machine.Pin.OUT)

def blink():
    led_rojo.off()
    led_azul.off()
    time.sleep(1)
    led_rojo.on()
    led_azul.on()
    time.sleep(1)

for n in range(2):
    blink()