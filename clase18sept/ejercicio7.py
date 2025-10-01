frase = input("Introduce una frase\n")
caracteres = len(frase)
lista = frase.split()
num_palabras = len(lista)
mas_larga = ""
for palabra in lista:
    if (len(palabra) > len(mas_larga)):
        mas_larga = palabra

print(f"Número de carácteres: {caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Palabra más larga: {mas_larga}")