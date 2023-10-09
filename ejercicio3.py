try:
    nombre_archivo = "archivo_inexistente.txt"
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
