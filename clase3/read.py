import time

# Abre el archivo en modo de anexado con codificación UTF-8
with open('workfile.txt', 'r', encoding="utf-8") as f:
    i = 0

    while True:
        i += 1
        dato = f.readline()  # Agrega un salto de línea
        print(dato)
        time.sleep(1)
        
        if i >= 5:  # Cambia a mayor o igual para cerrar después de 5 iteraciones
            break  # Sale del bucle cuando i es mayor o igual a 5
    
    f.close()
