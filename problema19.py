print("----------------------------")
print("Su nombre es largo, mediano o corto")
print("----------------------------")
nombre = input("ingrese su nombre:  ")
tmñ = len(nombre)
if tmñ > 5:
    print("nombre largo")
elif 5 < tmñ < 8: 
    print("nombre mediano")
else:
    print("nombre corto")