from colorama import Style


'''
Quiero crear una función imprimir que:
1- reciba el mensaje a imprimir
2- opcionalmente reciba un color para que imprima el mensaje de ese color
'''

def imprimir(mensaje, color=None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    
    print(mensaje)

def imprimir_con_marco(mensaje, color=None):
    '''
    | MENU              |
    | 1- LISTAR         |
    | 2- AÑADIR ARCHIVO |
    |
    '''
    frases = mensaje.split("\n")
    long_frase = [len(frase) for frase in frases]
    long_max = max(long_frase) + 4
    mensaje = ""
    for frase in frases:
        mensaje += "| " + frase + " "*(long_max-(len(frase)+3)) + "|\n"
    barra = "-"*long_max
    imprimir(barra + "\n" + mensaje + barra, color)