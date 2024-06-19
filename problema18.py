print("----------------------------")
print("3 y 5 divisible")
print("----------------------------")
numero = int(input("Ingrese un número entero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("Es divisible por 3 y por 5.")
elif numero % 3 == 0:
    print("Es divisible por 3 pero no por 5.")
elif numero % 5 == 0:
    print("Es divisible por 5 pero no por 3.")
else:
    print("No es divisible ni por 3 ni por 5.")


