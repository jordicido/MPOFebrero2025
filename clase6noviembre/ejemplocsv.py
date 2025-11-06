import csv

data = list()

'''
1- Leer el archivo
2- Generamos un iterable con todas las filas del archivo csv
3- Coger la fila del encabezado
4- Vamos recorriendo cada fila del iterable
    4.1 Generamos un item -> diccionario con la clave = posicion encabezado y valor = valor del dato
    4.2 Agregamos el item a la lista data
'''

with open('clase6noviembre/customers-1000.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        item = dict()
        for i in range(len(header)):
            item[header[i]] = row[i]
        data.append(item)
    
    print(data)
        
