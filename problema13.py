print("----------------------------")
print("Un año es un siglo")
print("----------------------------")
año = int(input("Ingresa un año: "))

if año % 100 == 0:
    if año % 400 == 0:
        print("El primer año de un siglo (es bisiesto).")
    else:
        print("No es el primer año de un siglo.")
else:
    if año % 4 == 0:
        print("El primer año de un siglo (es bisiesto).")
    else:
        print("No es el primer año de un siglo.")
