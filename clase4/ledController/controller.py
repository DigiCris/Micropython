import urequests
import network
import time
import machine

# Configura la conexión Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Redmi", "12349876")

led = machine.Pin(2,machine.Pin.OUT)


# Espera a que se establezca la conexión
while not sta_if.isconnected():
    print("Conectando...")
    time.sleep(1)

print("Conexión establecida:", sta_if.ifconfig())
print("IP actual:", sta_if.ifconfig()[0])

headers = {
    "Content-Type": "application/json"
}

# Prueba con la API de Dolar
while True:
    try:
        response = urequests.get("https://comunyt.co/led.json", headers=headers) # No usar localhost por eso lo subi a comunyt.co
        d = response.json()
        if response.status_code == 200:
            #print("Respuesta de Dolar API:", response.text)
            print("precio: {}".format(d["value"]))
            if d["value"] == "1":
                led.off()
            if d["value"] == "0":
                led.on()
        else:
            print("Error en la solicitud de Dolar API:", response.status_code)
    except Exception as e:
        print("Ocurrió un error al acceder a Dolar API:", e)
    time.sleep(3)

