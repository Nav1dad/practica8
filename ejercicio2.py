nombres = []
while True:
    nombre = input("Ingrese un nombre (o escriba 'salir' para finalizar): ")
    if nombre.lower() == 'salir':
        break
    nombres.append(nombre)


with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Nombres escritos en 'nombres.txt'.")