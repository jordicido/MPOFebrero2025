edad = int(input("Dime tu edad: "))
if edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Senior")