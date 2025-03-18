n=int(input("Ingrese un nuero de tres digitos: "))

a=n % 100
dig1= n // 100
dig3= a % 10

if dig1==dig3:
    print("Es número capicua.")
else:
    print("No es número capicua.")