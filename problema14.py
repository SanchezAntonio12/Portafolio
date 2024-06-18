print("----------------------------")
print("Las del triangulo")
print("----------------------------")
LD1 = float(input("Ingrese la longitud del primer lado: "))
LD2 = float(input("Ingrese la longitud del segundo lado: "))
LD3 = float(input("Ingrese la longitud del tercer lado: "))


if ((LD1 + LD2) > LD3) or ((LD1 + LD3) > LD2) or ((LD2 + LD3) > LD1):
    print("Los lados forman un triángulo válido.")
else:
    print("Los lados No forman un triángulo válido.")