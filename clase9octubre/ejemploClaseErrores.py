notas_alumnos = {
    "Kenneth": [6.5, 8, 3],
    "Jorge": [0, 10, 5],
    "Jose el chater": [7, 6, 10],
    "Heber": [10, 10, 10],
    "Victor": [7, 8, 9],
    "Ander": [8, 8, 8]
}

def imprimir_menu():
    return("""Escoge una opción:
            1- Consultar media alumno
            2- Añadir nota a alumno
            3- Añadir alumno    
            4- Eliminar nota de alumno
            5- Eliminar alumno
            6- Salir\n""")

def consultar_media(alumno):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no existe en el sistema")
    if len(notas_alumnos[alumno]) == 0:
        raise ZeroDivisionError(f"El alumno {alumno} no tiene notas registradas")
    
    notas = notas_alumnos[alumno]
    total = 0
    for nota in notas:
        total += nota

    return total/len(notas)

def añadir_nota_alumno(alumno, nota):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no existe en el sistema")
    
    notas_alumnos[alumno].append(nota)

def añadir_alumno(alumno, notas):
    if alumno in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} ya existe en el sistema")

    notas_alumnos[alumno] = notas

def mostrar_notas_alumno(alumno):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no existe en el sistema")
    
    return notas_alumnos[alumno]

def eliminar_nota_alumno(alumno, nota):
    if nota not in notas_alumnos[alumno]:
        raise ValueError(f"El alumno {alumno} no tiene la nota {nota}")
    
    notas_alumnos[alumno].remove(nota)
    
def eliminar_alumno(alumno):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no existe en el sistema")
    
    notas_alumnos.pop(alumno)

def main():
    print("Bienvenidos al gestor de notas!")

    opcion = input(imprimir_menu())

    while opcion != "6":
        match opcion:
            case "1":
                alumno = input("Que media quieres consultar?\n") 
                try:
                    print(f"La media del alumno {alumno} es {consultar_media(alumno)}")
                except Exception as e:
                    print(e)

            case "2":
                try: 
                    alumno = input("A qué alumno quieres añadirle una nota?\n")
                    nota = float(input("Qué nota quieres añadir?\n"))
                    añadir_nota_alumno(alumno, nota)
                except Exception as e:
                    print(e)
            
            case "3":              
                try: 
                    notas = []
                    alumno = input("Cuál es el nombre del alumno?\n")
                    añadir_notas = input("Quieres añadir notas al alumno?\n")
                    if añadir_notas.lower() == "si":
                        notas = [float(num) for num in input("Qué notas tiene el alumno?\n").split()]

                    añadir_alumno(alumno, notas)
                except Exception as e:
                    print(e)

            case "4":
                try:
                    alumno = input("A qué alumno quieres eliminarle una nota?\n")
                    print(f"Las notas del alumno son {mostrar_notas_alumno(alumno)}")
                    nota = float(input("Qué nota quieres elimnar?\n"))
                    eliminar_nota_alumno(alumno, nota)
                    print(f"Las notas del alumno ahora son {mostrar_notas_alumno(alumno)}")
                except Exception as e:
                    print(e)
            
            case "5":
                try:
                    alumno = input("Qué alumno quieres eliminar?\n")
                    eliminar_alumno(alumno)
                except Exception as e:
                    print(e)

            case _:
                print("El valor enviado debe ser entre 1 y 6")
        
        opcion = input(imprimir_menu())

main()