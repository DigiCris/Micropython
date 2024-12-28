import network
import time
from umqtt.simple import MQTTClient
import machine

# Configuración de la conexión Wi-Fi
SSID = 'Redmi'
PASSWORD = '12349876'

# Configuración del servidor MQTT
MQTT_BROKER = 'test.mosquitto.org'
MQTT_TOPIC = 'manipularLed'

# Inicializa el LED integrado
led = machine.Pin(2, machine.Pin.OUT)  # GPIO 2 corresponde al LED integrado

# Función para conectar a la red Wi-Fi
def connect_wifi():
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

# Función de callback para manejar los mensajes entrantes
def sub_callback(topic, msg):
    print("Mensaje recibido en el tema {}: {}".format(topic, msg))
    if msg == b'1':
        led.on()  # Enciende el LED
        print("LED Apagado")
    elif msg == b'0':
        led.off()  # Apaga el LED
        print("LED Encendido")

# Conexión al Wi-Fi
connect_wifi()

# Configura y conecta al cliente MQTT
client = MQTTClient("esp8266_client", MQTT_BROKER)
client.set_callback(sub_callback)
client.connect()
client.subscribe(MQTT_TOPIC)

print("Esperando mensajes en el tema:", MQTT_TOPIC)

# Bucle principal

while True:
    try:
        client.check_msg()  # Verifica si hay nuevos mensajes
    except OSError as e:
        print("Error al verificar mensajes:", e)
    time.sleep(10)

