# Abre el archivo en modo de anexado con codificación UTF-8
f= open('workfile.txt', 'r', encoding="utf-8")
dato = f.read()  # Agrega un salto de línea
print(dato)
f.close()