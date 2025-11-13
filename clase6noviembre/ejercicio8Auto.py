import sys
import os

def rm_empty_files(path):
    if not os.path.isdir(path):
        raise NotADirectoryError("La ruta proporcionada no corresponde a un directorio")
    
    result = 0
    dir_items = os.listdir(path)
    for item in dir_items:
        new_path = os.path.join(path, item)
        if os.path.isfile(new_path) and os.path.getsize(new_path) == 0:
            os.remove(new_path)
            result += 1
        elif os.path.isdir(new_path) and len(os.listdir(new_path)) == 0:
            os.rmdir(new_path)
            result += 1
    
    return result

try:
    if len(sys.argv) != 2:
        raise IndexError("El programa debe llamarse con un solo argumento")

    print(f"Numero de archivos eliminados: {rm_empty_files(sys.argv[1])}")
except Exception as e:
    print(e)