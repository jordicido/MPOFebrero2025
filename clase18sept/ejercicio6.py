palabras_feas = ["perro", "queso", "examen"]
frase = input("Dime una frase:\n")

for palabra in palabras_feas:
    frase = frase.replace(palabra, "*"*len(palabra))

print(frase)