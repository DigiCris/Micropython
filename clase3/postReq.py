import urequests
import network
import time
import json

# Configura la conexión Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("TeleCentro-66b5", "jdasjdaldas")

# Espera a que se establezca la conexión
while not sta_if.isconnected():
    print("Conectando...")
    time.sleep(1)

print("Conexión establecida:", sta_if.ifconfig())
print("IP actual:", sta_if.ifconfig()[0])

# Datos a enviar
data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "eth_getBalance",
    "params": ["0x7e2Bf2537086d1A22791CE00015BbE34Ed2D301c", "latest"]
}

# Encabezados para la solicitud
headers = {
    "Content-Type": "application/json"
}

# Realiza la solicitud POST
try:
    response = urequests.post("https://comunyt.co/repost.php", json=data, headers=headers)
    result = response.json()
    print("Resultado:", result["result"])
except Exception as e:
    print("Ocurrió un error:", e)