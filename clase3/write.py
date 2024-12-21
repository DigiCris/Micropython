import time

# Abre el archivo en modo de anexado con codificación UTF-8
with open('workfile.txt', 'a', encoding="utf-8") as f:
    i = 0

    while True:
        dato = "24°C"
        i += 1
        f.write("Temperatura: {}\n".format(dato))  # Agrega un salto de línea
        time.sleep(2)
        
        if i >= 5:  # Cambia a mayor o igual para cerrar después de 5 iteraciones
            break  # Sale del bucle cuando i es mayor o igual a 5
    
    f.close()