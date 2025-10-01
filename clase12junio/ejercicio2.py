import os
from colorama import Fore, Style
import sys
sys.path.append('/home/jordicido/Documents/github.com/jordicido/MPOFebrero2025/clase19junio')
# import importlib
# module = importlib.import_module("../clase19junio")

from lectura import leer_entero, leer_string
from escritura import imprimir, imprimir_con_marco

colores_mensajes = {
    "ERROR": Fore.LIGHTRED_EX,
    "MENU": Fore.BLUE,
    "INPUT": Fore.LIGHTYELLOW_EX,
    "SUCCESS": Fore.LIGHTGREEN_EX
}

def listar_archivos(ruta):
    try:
        return os.listdir(ruta)
    except FileNotFoundError:
        raise FileNotFoundError

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

def color_segun_extension(ruta, archivo):
    if os.path.isdir(ruta+archivo):
        return "orange"
    elif len(archivo.split(".")) == 1:
        return "white"
    elif archivo.split(".")[-1] == "txt":
        return "green"
    elif archivo.split(".")[-1] in ["jpg", "png"]:
        return "blue"
    elif archivo.split(".")[-1] in ["mp3", "wav"]:
        return "yellow"
    return "white"

def colorear(color):
    if color == "orange":
        return Fore.MAGENTA
    elif color == "blue":
        return Fore.BLUE
    elif color == "yellow":
        return Fore.YELLOW
    elif color == "green":
        return Fore.GREEN
    return Fore.WHITE

def main():
    opcion = -1
    while opcion != 5:
        menu = "MENU\n1. Listar archivos\n2. Verificar existencia archivo\n3. Crear archivo\n4. Crear directorio\n5. Salir"
    
        imprimir_con_marco(menu, colores_mensajes["MENU"])

        opcion = leer_entero("Introduce una opción:", colores_mensajes["INPUT"])

        if opcion == 1:
            ruta = leer_string("Introduce la ruta que quieres consultar:", colores_mensajes["INPUT"])
            try:
                archivos = listar_archivos(ruta)
                for archivo in archivos:
                    imprimir(archivo, colorear(color_segun_extension(ruta, archivo)))

            except FileNotFoundError:
                imprimir(f"La ruta {ruta} no existe", colores_mensajes["ERROR"])
            except:
                imprimir("Error al consultar la ruta, intenta de nuevo", colores_mensajes["ERROR"]) 
            
        elif opcion == 2:
            archivo = leer_string("Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                imprimir(f"El archivo {archivo} existe", colores_mensajes["SUCCESS"])
            else:
                imprimir(f"El archivo {archivo} no existe", colores_mensajes["ERROR"])
        elif opcion == 3:
            nombre = leer_string("Qué nombre quieres ponerle al archivo?", colores_mensajes["INPUT"])
            if existe_archivo(nombre):
                imprimir(f"Este archivo {archivo} ya existe", colores_mensajes["ERROR"])
            else:
                archivo = crear_archivo(nombre)
                imprimir(f"Archivo {archivo.name} creado con éxito", colores_mensajes["SUCCESS"])
        elif opcion == 4:
            nombre = leer_string("Qué nombre quieres ponerle al directorio?", colores_mensajes["INPUT"])
            try:
                crear_directorio(nombre)
                imprimir(f"Directorio {nombre} creado con éxito", colores_mensajes["SUCCESS"])
            except FileExistsError:
                imprimir(f"El directorio {nombre} ya existe", colores_mensajes["ERROR"])
        elif opcion > 5:
            imprimir("Opción no válida", colores_mensajes["ERROR"])


if __name__ == '__main__':
    main()
