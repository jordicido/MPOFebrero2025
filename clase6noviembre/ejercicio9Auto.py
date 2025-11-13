import sys
import os

def rm_files_with_extension(path, extension):
    if not os.path.isdir(path):
        raise NotADirectoryError("La ruta proporcionada no corresponde a un directorio")
    
    result = 0
    dir_items = os.listdir(path)
    for item in dir_items:
        new_path = os.path.join(path, item)
        if os.path.isfile(new_path) and new_path.endswith(extension):
            os.remove(new_path)
            result += 1
    
    return result

try:
    if len(sys.argv) != 3:
        raise IndexError("El programa debe llamarse con dos argumentos")

    print(f"Numero de archivos eliminados en el directorio: {rm_files_with_extension(sys.argv[1], sys.argv[2])}")
except Exception as e:
    print(e)