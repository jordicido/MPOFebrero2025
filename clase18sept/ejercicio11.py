# Don Quijote de la Mancha[a]​ es una novela escrita por el español Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es la obra más destacada de la literatura española y una de las principales de la literatura universal.[1]​ En 1615 apareció su continuación con el título de Segunda parte del ingenioso caballero don Quijote de la Mancha.


texto = input("Introduce el texto\n").lower().split()
palabra = input("Introduce la palabra a buscar\n").strip()


print(f"El numero de veces que aparece la palabra {palabra} en el texto es {texto.count(palabra)}")
