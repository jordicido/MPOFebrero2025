"""
Vamos a realizar un programa que lea el archivo sistema_log_extenso.txt
y imprima copie en otro archivo errores.txt todos los mensajes del tipo ERROR
"""

log = open("sistema_log_extenso.txt", "r")  # Referencia al archivo
log_errores = open("errores.txt", "w")
log_data = log.readlines() # Lista con todas las lineas en String

for line in log_data:
    if "ERROR" in line:
        log_errores.write(line)


