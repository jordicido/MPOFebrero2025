import os

def search_lines(path, word):
    if len(word) == 0:
        raise ValueError("La palabra no puede ser vacía")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe")

    with open(path, "r") as file:
        for num, line in enumerate(file, start=1):
            if word in line:
                line_splitted = line.split()
                for i in range(len(line_splitted)):
                    if word.lower() == line_splitted[i].lower():
                        print(f"Linea {num}: Posición {len(" ".join(line_splitted[0:i+1]))+1-len(line_splitted[i])}")


path = input("Qué archivo quieres imprimir?\n")
word = input("Qué palabra quieres buscar?\n")

try:
    search_lines(path, word)
except Exception as e:
    print(e)