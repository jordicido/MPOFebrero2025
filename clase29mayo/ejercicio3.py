'''
Ejercicio 3 - Inventario de productos¶
Escribe un programa que gestione un inventario de productos utilizando un diccionario.
El programa debe permitir al usuario añadir productos con su nombre y cantidad, 
eliminar productos, y consultar la cantidad de un producto específico. El programa 
debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".
'''
inventario = {}
opcion = -1

while opcion != 4:
    print("Escoge una opción:")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Consultar producto")
    print("4. Salir")
    opcion = int(input("Introduce una opción: "))
    
    if opcion == 1:
        nombre = input("Introduce un producto: ")
        cantidad = int(input("Introduce una cantidad: "))
        inventario[nombre] = cantidad
    elif opcion == 2:
        nombre = input("Introduce el producto a eliminar: ")
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto {nombre} eliminado del inventario")
        else:
            print(f"No existe el producto {nombre} en el inventario")
    elif opcion==3:
        nombre = input("Introduce el producto a consultar: ")
        if nombre in inventario:
            print(f"El producto {nombre} tiene una cantidad de {inventario[nombre]} unidades")
        else:
            print(f"No existe el producto {nombre} en el inventario")
    elif opcion > 4 or opcion < 1:
        print(f"La opción {opcion} no existe en la lista de comandos")
            
print("Saliendo...")
            