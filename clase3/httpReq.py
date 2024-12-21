import urequests
import network
import time

# Configura la conexión Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Redmi", "12349876")

# Espera a que se establezca la conexión
while not sta_if.isconnected():
    print("Conectando...")
    time.sleep(1)

print("Conexión establecida:", sta_if.ifconfig())
print("IP actual:", sta_if.ifconfig()[0])

# Prueba con una conexión HTTP

try:
    response = urequests.get("http://httpbin.org/get")
    print("HTTP ok")
except Exception as e:
    print("Error al acceder a httpbin (HTTP):", e)

"""
# Prueba con una conexión HTTPS
try:
    response = urequests.get("https://httpbin.org/get")
    print("HTTPS ok")
except Exception as e:
    print("Error al acceder a httpbin (HTTPS):", e)

# Definir un User-Agent personalizado
headers = { "Content-Type": "application/json" }


# Prueba con la API de Dolar
try:
    response = urequests.get("https://comunyt.co/dolar.json", headers=headers)
    d = response.json()
    if response.status_code == 200:
        #print("Respuesta de Dolar API:", response.text)
        print("precio: {}".format(d["venta"]))
    else:
        print("Error en la solicitud de Dolar API:", response.status_code)
except Exception as e:
    print("Ocurrió un error al acceder a Dolar API:", e)
"""