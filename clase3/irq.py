from machine import Pin

# Configuración del botón y el LED
button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

# Estado del LED
led_on = False

# Función de manejo de la interrupción
def toggle_led(pin):
    global led_on
    led_on = not led_on  # Cambia el estado
    if led_on:
        led.on()  # Enciende el LED
    else:
        led.off()  # Apaga el LED

# Configuración de la interrupción
button.irq(trigger=Pin.IRQ_FALLING, handler=toggle_led)

# Bucle principal vacío
while True:
    pass