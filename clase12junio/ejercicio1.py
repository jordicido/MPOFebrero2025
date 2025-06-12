import os

def listar_archivos():
    return os.listdir(".")

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError

    return nombre

def main():
    opcion = -1
    while opcion != 5:
        print("### MENU ###")
        print("1. Listar archivos")
        print("2. Verificar existencia archivo")
        print("3. Crear archivo")
        print("4. Crear directorio")
        print("5. Salir")

        opcion = int(input("Escoge una opción:\n"))

        if opcion == 1:
            archivos = listar_archivos()
            for archivo in archivos:
                print(archivo)
        elif opcion == 2:
            archivo = input("Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                print("✅ Archivo existe, el pueblo resiste")
            else:
                print("❌ El archivo no existe")
        elif opcion == 3:
            nombre = input("Qué nombre quieres ponerle al archivo?\n")
            if existe_archivo(nombre):
                print("Este archivo ya existe")
            else:
                archivo = crear_archivo(nombre)
                print(f"Archivo {archivo.name} creado con éxito")
        elif opcion == 4:
            nombre = input("Qué nombre quieres ponerle al directorio?\n")
            try:
                crear_directorio(nombre)
                print(f"Directorio {nombre} creado con éxito")
            except FileExistsError:
                print(f"El directorio {nombre} ya existe")
        elif opcion > 5:
            print("Opción no válida")


if __name__ == '__main__':
    main()
