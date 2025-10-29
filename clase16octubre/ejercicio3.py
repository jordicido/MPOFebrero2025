def escribir_nombres_en_archivo(nombres, archivo):
    if len(nombres) == 0:
        raise ValueError("No se ha proporcionado ningún nombre")
    
    with open(archivo, "a") as file:
        for name in nombres:
            file.write(f"{name}\n")


nombres = input("Introduce una lista de nombres separados por espacio\n").split()
escribir_nombres_en_archivo(nombres, "nombres.txt")