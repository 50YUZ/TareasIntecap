# if= si  :=entones if:=si entones  else= si no else:=si no entones elif= si no si

#print("Si la nota del estudiante es mayor a 60 que imprima aprobado, si no que imprima reprobado")

#nota=int(input("Digite la nota del alumno: "))

#if nota>=60:
#    print("Aprobado")
#else:
#    print("Reprobado")

#ejemplo 2
#imprimir el nuero de mayor alor de los 3 ingresados
#num1=int(input("Ingrese el primer número: "))
#num2=int(input("Ingrese el segundo número: "))
#num3=int(input("Ingrese el tercer número: "))

#if (num1>num2) and (num1>num3):
#    print(num1)
#elif (num2>num1) and (num2>num3):
#    print(num2)
#else:
#    print(num3)

#num1=int(input("Ingrese el primer número: "))
#num2=int(input("Ingrese el segundo número: "))
#num3=int(input("Ingrese el tercer número: "))

#if (num1<num2) and (num1<num3):
#    print(num1)
#elif (num2<num1) and (num2<num3):
#    print(num2)
#else:
#    print(num3)

#num1=int(input("Ingrese el primer número: "))
#num2=int(input("Ingrese el segundo número: "))
#num3=int(input("Ingrese el tercer número: "))

#if (num1>num2) and (num1<num3):
#    print(num1)
#elif (num2>num1) and (num2<num3):
#    print(num2)
#else:
#    if (num3>num1) and (num3<num2):
#        print(num3)        

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))
#mayor
if (num1>num2) and (num1>num3):
    print(num1, " Es mayor40")
elif (num2>num1) and (num2>num3):
    print(num2, " Es mayor")
else:
    print(num3, " Es mayor")
#medio
if (num1>num2) and (num1<num3):
    print(num1, " Es medio")
elif (num2>num1) and (num2<num3):
    print(num2, " Es medio")
else:
    if (num3>num1) and (num3<num2):
        print(num3, " Es medio")  


#menor
if (num1>num2) and (num1>num3):
    print(num1," Es menor")
elif (num2>num1) and (num2>num3):
    print(num2, " Es menor")
else:
    print(num3, " Es menor")