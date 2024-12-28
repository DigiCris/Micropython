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
    #response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"
    
    response = """
    <html>

    <head>
    <title>ESP Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        h1 {
            color: #0F3376;
            padding: 2vh;
        }

        p {
            font-size: 1.5rem;
        }

        .button {
            display: inline-block;
            background-color: #e7bd3b;
            border: none;
            border-radius: 4px;
            color: white;
            padding: 16px 40px;
            text-decoration: none;
            font-size: 30px;
            margin: 2px;
            cursor: pointer;
        }

        .button2 {
            display: inline-block;
            background-color: #4286f4;
            border: none;
            border-radius: 4px;
            color: white;
            padding: 16px 40px;
            text-decoration: none;
            font-size: 30px;
            margin: 2px;
            cursor: pointer;
        }
        
    </style>
    </head>

    <body>
    <h1>ESP Web Server</h1>
    <p>GPIO state: <strong></strong></p>
    <p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
    </body>

    </html>  """
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)    
    
    cl.send(response)               # Envía la respuesta
    cl.close()                      # Cierra la conexión


