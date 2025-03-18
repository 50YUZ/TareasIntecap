from math import sqrt
import math
menup="""
                 Menú
    1. Comparación de tres números
    2. Relación entre dos números
    3. Evaluación de operaciones complejas
    4. Comprobar un año mágico
    5. Año espejo
    6. Número balanceado de cuatro dígitos
    7. Fecha con propiedad secreta
"""
print(menup)

menup=input("¿Que opción que desea utilizar?")

if menup == "1":
    print("Comparación de tres números")
    cant=int(input("Digíte una cantidad de tres dígitos: "))
    cantstr= str(cant)
    num1=int(cantstr[0])
    num2=int(cantstr[1])
    num3=int(cantstr[2])
    if (num1==num2) and (num1==num3) and (num2 == num1) and (num2 == num3) and (num3 == num1) and (num3 == num2):#igual a todos
        print("Los tres dígitos son iguales. :)")
    elif (num1==num2) and (num1!=num3):#igual a los dos primeros
        print("Solo los dos primeros dígitos son iguales. :)")
    elif (num1!=num2) and (num2==num3):
        print("Solo los ultimos dos dígitos son iguales. :)")
    elif (num1!=num2) and (num1==num3):
        print("Solo el primer y último dígito son iguales. :)")
    elif (num1!=num2) and (num2!=num3):
        print("Ningun dígito es igual. :)")
    elif cant > 999 and cant <100:
        print("El número ingresado no es de tres dígitos")
    else:
        print("ERROR ")
elif menup == "2":
    print("Relación entre dos números")
    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))
    num1d=num1*2
    num2d=num2*2
    if num1 == num2d:
        print("El primer numero es el doble del segundo número.")
    elif num2 == num1d:
        print("El segundo número es el doble del primer número.")
    else:
        print("Niguno de los dos número es el doble del otro.")

    if num1+num2 % 2 == 0:
        print("La suma de los dos números ingresados es: ",num1+num2,"y es un numero par")
    else:
        print("La suma de los dos números ingresados es: ",num1+num2,"y es numero impar")
elif menup == "3":
    print("Evaluación de operaciones complejas")
    x=int(input("Ingrese el valor de X: "))
    y=int(input("Ingrese el valor de Y: "))
    z=int(input("Ingrese el valor de Z: "))
    if ((x + y)*z % x - y == 0) and (x > z):
        print("(",x," + ",y,")","*",z," %",x," -",y," es multiplo de ",x ,"y ",x," es mayor que ",z)
    else:
        print("(""(",x," + ",y,")","*",z," %",x," -",y," no es multiplo de ",x, "y ",x," es menor que ",z)
elif menup == "4":
    print("Comprobar un año mágico")
    an=int(input(" Ingrese un año: "))
    primeros2= an // 100
    ultimos2= an % 100
    if primeros2 + ultimos2 == 100:
        print("Es un año mágico")
    else:
        print("No esw un año mágico :(")
elif menup == "5":
    print("Año espejo")
    anesp=int(input("Ingrese un año: "))
    anesptext= str(anesp)
    anInvertido= int(anesptext[3]+anesptext[2]+anesptext[1]+anesptext[0])

    if anInvertido == anesp:
        print("Es un año espejo.")
    else:
        print("No es un año espejo.")
elif menup == "6":
    print("Número balanceado de cuatro dígitos")
    num=int(input("Ingrese un número de cuatro dígitos: "))
    numstr= str(num)
    num1= int(numstr[0])
    num2= int(numstr[1])
    num3= int(numstr[2])
    num4= int(numstr[3])
    op1= num1+num4
    op2= num2+num3
    if op1 == op2:
        print("Es un número balanceado.")
    else:
        print("No es un número balanceado.")
elif menup == "7":
    print("Fecha con propiedad secreta")
    fecha=int(input("ingrese la fecha DD/MM/AAAA: "))
    fecha_str= str(fecha)
    d= int(fecha_str[0]+fecha_str[1])
    m= int(fecha_str[2]+fecha_str[3])
    a= int(fecha_str[4]+fecha_str[5])
    a2=int(fecha_str[6]+fecha_str[7])

    suma=d+m
    diferencia=a-a2
    
    op=suma*diferencia

    if op >= 0:
        raiz=math.sqrt(op)
        if raiz == int(raiz):
            print("El total de ",fecha," es ",op,"y es un cuadrado perfecto.")
        else:
            print("El total de ",fecha," es ", op," y no es cuadrado perfecto.")
    else:
        print("El total de ",fecha," es ", op," y no es cuadrado perfecto.")
else:
    print("ERROR Opción Invalida")