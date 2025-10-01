precio = int(input("Dime un precio"))
descuento = int(input("Dime el % de descuento"))

print(f"el precio final es {precio-(precio*descuento/100):.2f} €")