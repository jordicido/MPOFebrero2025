from datetime import datetime

usuarios = {
    "jordi":"c0ntr4s3n4",
    "asires": "seguridad",
    "damdawers":"prototipo"
}

def verify_user(user, passw):
    with open("log.txt", "a") as file:
        if user not in usuarios.keys():
            file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha intentado loguear un usuario NO EXISTENTE con nombre {user}\n")
            raise ValueError("Acceso denegado")
        if passw != usuarios[user]:
            file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha intentado loguear el usuario {user} pero HA FALLADO EL PASSWORD\n")
            raise ValueError("Acceso denegado")

        file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha logueado EXISTOSAMENTE el usuario {user}\n")

while True:
    user = input("Introduce tu usuario:\n")
    passw = input("Introduce tu password:\n")

    try:
        verify_user(user, passw)
    except Exception as e:
        print(e)