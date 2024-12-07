import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

def blink():
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)

for n in range(3):
    blink()