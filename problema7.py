print("----------------------------")
print("Precio con descuento")
print("----------------------------")
P = float(input("Ingresa el PP: "))
if P > 100:
    Des = P * 0.10
    PF = P - Des
    print("El precio final del descuento es.")
else:
    print("El precio sin descuento es.")
    
