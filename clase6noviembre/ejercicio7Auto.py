import sys
import os

'''
1- comprobamos que el path sea un directorio
2- Inicializamos el contador
3- Obtener los items del directorio
4- Recorremos los items del directorio
    4.1- Si item == archivo contador+1
5- Devolvemos numero de archivos encontrados
'''
def list_files(path):
    if not os.path.isdir(path):
        raise NotADirectoryError("La ruta proporcionada no corresponde a un directorio")
    
    result = 0
    dir_items = os.listdir(path)
    for item in dir_items:
        if os.path.isfile(os.path.join(path, item)):
            result += 1

    return result


try:
    if len(sys.argv) != 2:
        raise IndexError("El programa debe llamarse con un solo argumento")

    print(f"Numero de archivos en el directorio: {list_files(sys.argv[1])}")
except Exception as e:
    print(e)