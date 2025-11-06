import os

'''
1- Comprobar que sea un archivo
2- Comprobar que la nueva ruta es un directorio
3- new_path = directorio/nombre_fichero
5- Comprobar que path y new_path no son iguales
6- Mover el archivo a new_path
'''
def move_file(path, new_path):
    path_without_filename = new_path
    new_filename = ""
    if not os.path.isfile(path):
        raise FileNotFoundError("No existe el archivo")
    if not os.path.isdir(new_path):
        if len(new_path.split("/")) > 1:
            path_without_filename = new_path.rsplit("/",maxsplit=1)[0]
            new_filename = new_path.rsplit("/",maxsplit=1)[1]
            if not os.path.isdir(path_without_filename):
                raise FileNotFoundError("No existe el directorio de destino")
        else:
            new_filename = new_path
        
        
    if len(new_filename) == 0:
        raise ValueError("No se ha pasado un nombre de fichero")
    else:
        with open(path, 'r') as old_file:
            old_file_data = old_file.read()
        
        with open(new_path, 'w') as new_file:
            new_file.write(old_file_data)
        
        os.remove(path)

path = input("Introduce el archivo que quieres mover\n")
new_path = input("Introduce la ruta donde quieres moverlo\n")

try:
    move_file(path, new_path)
except Exception as e:
    print(e)