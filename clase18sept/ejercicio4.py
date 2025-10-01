texto = input("Dime una frase\n")
mayus = 0
minus = 0
for letra in texto:
    if letra.isupper():
        mayus += 1
    elif letra.islower():
        minus += 1

print(f"Hay {mayus} mayúsculas y {minus} minúsculas")