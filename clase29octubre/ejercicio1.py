import os

def list_directory(path):
    if not os.path.exists(path):
        raise FileNotFoundError("No existe el directorio especificado")

    elementos = os.listdir(path)
    resultado = {
        "archivos":[],
        "directorios":[]
        }
    for elem in elementos:
        if os.path.isfile(elem):
            resultado["archivos"].append(elem)
        elif os.path.isdir(elem):
            resultado["directorios"].append(elem)
    
    return resultado

path = input("Introduce la ruta que quieres listar\n")

try:
    print(list_directory(path))
except Exception as e:
    print(e)