nombre = input("Cual es tu nombre? ")
palabras = nombre.split()
iniciales = ""
for p in palabras:
    iniciales += p[0].upper()
print(iniciales)