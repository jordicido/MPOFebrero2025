# Ejercicio 5 - Puede entrar en el servidor de Discord?

rol = input("Dime el rol del usuario: ").lower()
academia = input("En que academia estudias/trabajas? ").lower()

if rol == "estudiante" and academia == "prometeo":
    print("Access granted to: Official and Chill Discord")
elif rol == "profesor" and academia == "prometeo":
    print("Access granted to: Official Discord")
else:
    print("Enroll Prometeo to access to the best Discord servers")