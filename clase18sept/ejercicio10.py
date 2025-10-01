# jordi.cidoncha@gmail.com
# jordi.cidoncha@thepower.education
# jordi.cidoncha@edu.gva.es
# kenneth.alonso@gmail.com
# {
# gmail: (jordi.cidoncha@gmail.com, kenneth.alonso@gmail.com),
# thepower: (jordi.cidoncha@thepower.education),
# edu: (jordi.cidoncha@edu.gva.es)
# }

correos = input("Introduce una lista de correos separados por coma\n").split(",")
correos_clas = {}

for correo in correos:
    extension = correo.split("@")[1].split(".")[0]
    if extension not in correos_clas.keys():
        correos_clas[extension] = list()
    
    correos_clas[extension].append(correo)

print(correos_clas)
