import random

def generar_password(longitud):
    password = ""
    if (longitud < 8):
        raise ValueError("La longitud debe ser mayor o igual a 8")
    
    letras = "".join(chr(random.randint(97, 122)) for i in range(longitud-2))
    for i in range(len(letras)):
        if i%2 == 0:
            password += letras[i].upper()
        else:
            password += letras[i].lower()
    
    password += str(random.randint(0,9))
    password += chr(random.randint(33, 47))

    
    password_lista = list(password)
    random.shuffle(password_lista)

    return "".join(password_lista)

print(generar_password(8))
