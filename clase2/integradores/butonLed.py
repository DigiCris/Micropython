from machine import Pin

button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(2,Pin.OUT)

while True:
    val = button.value()
    if val==1:
        led.on()
    else:
        led.off()