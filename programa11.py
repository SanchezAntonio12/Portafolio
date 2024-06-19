print("----------------------------")
print("Es primo o no es primo")
print("----------------------------")
def Nprimo(numero):
    if numero <= 1:
        print("no es primo")
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print("Es primo")
    
numero= int(input("Ingrese un número: "))
if Nprimo(numero):
    
    
    print("es primo.")
else:
    print("No es primo.")
    
#Programa con ayuda de ChatPGT 👾😢
    