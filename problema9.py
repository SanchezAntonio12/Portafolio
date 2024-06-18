print("----------------------------")
print("Es letra o es digito")
print("----------------------------")
caracter = input("Ingrese un carácter: ")
if 'a' <= caracter <= 'z':
    print("Es una letra minúscula.")
elif 'A' <= caracter <= 'Z':
    print("Es una letra mayúscula.")
else:
    print("Es un dígito.")

