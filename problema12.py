print("----------------------------")
print("Salario bruto")
print("----------------------------")
S=float(input("Ingrese el salario bruto: "))

if S > 2000:
    impu = S * 0.20
    SB = S - impu
    print("Su salario neto es:", SB)
    
else:
    SB = S
    print("Su salario neto es:", SB)