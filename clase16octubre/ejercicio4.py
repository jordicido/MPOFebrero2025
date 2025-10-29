import os

def copy_file(file1, file2):
    if not os.path.exists(file1):
        raise FileNotFoundError("El archivo a copiar no existe")
    
    with open(file1, "r") as file1:
        lines_file1 = file1.readlines()
        if len(lines_file1) == 0:
            raise ValueError("El archivo a copiar está vacío")
    
        if os.path.exists(file2):
            answer = input(f"El archivo {file2} ya existe, desea sobreescribir? S/N\n")
            if answer.upper() != "S":
                return
            
        with open(file2, "w") as file2:
            file2.writelines(lines_file1)
        

file_to_copy = input("Introduce el nombre del archivo a copiar:\n")
new_copied_file = input("Introduce el nombre del nuevo archivo:\n")

try:
    copy_file(file_to_copy, new_copied_file)
except Exception as e:
    print(e)