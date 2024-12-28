import usocket as socket
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
ip_address = sta_if.ifconfig()[0]
print("IP actual:", ip_address)

# Configura el socket del servidor
s = socket.socket()                # Crea el socket
s.bind((ip_address, 80))          # Asocia la dirección IP y el puerto
s.listen(1)                        # Escucha conexiones

print("Esperando conexiones en", (ip_address, 80))

while True:
    cl, addr = s.accept()          # Acepta una conexión
    print('Cliente conectado desde:', addr)
    request = cl.recv(1024)        # Recibe la solicitud
    print('Solicitud:', request)
    
    # Respuesta HTTP con "Hello, World!"
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    cl.send(response)               # Envía la respuesta
    cl.close()                      # Cierra la conexión
