#La suma de los dos números mayores, deterinar los dos núeros mayores y sumarlos

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))

if (num1==num2 and num1==num3) or (num2==num1 and num2==num3) or (num3==num1 and num3==num2):
    print("Los 3 números son iguales",num1,num2,num3)
else:
    if num1<num2 and num1<num3:
        suma1=num2+num3
        print("la suma de los dos mayores son:",suma1)
    elif num2<num1 and num2<num3:
        suma2=num1+num3
        print("la suma de los dos mayores son:",suma2)
    else:
        suma3=num1+num2
        print("la suma de los dos mayores son:",suma3)