# PALABRA
# *RB*L*P

palabra = input("Introduce la palabra a invertir: ")

for i in range(len(palabra)-1, -1, -1):
    if palabra[i].lower() in ("a","e","i","o","u"):
        print("*", end="")
    else:
        print(palabra[i], end="")
print()