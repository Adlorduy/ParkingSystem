from functions import writeFile

writeFile("vacio.txt")

with open("vacio.txt") as file:
    archivo = file.read().split("\n")

print(archivo)