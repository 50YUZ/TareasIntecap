#0 Evaluar si un número es múltiplo de 2 o 3
#Dado un número determinar si es múltiplo de 2y3 o 2o3
#print("Averiguaremos si el número que ingreses es múltiplo de 2y3 o solo de 2o3")
#n=int(input("Ingrése un número "))
#
#if n % 2 == 0 and n % 3 == 0:
#    print("El número ingresado es múltiplo de dos y tres.")
#elif n % 2 == 0:
#    print("El número ingresado solo es múltiplo de dos.")
#elif n % 3 == 0:
#    print ("El número ingresado solo es múltiplo de tres.")
#else:
#    print("El número ingresado no es múltiplo de dos ni de tres.")


#1. Escribe un pseudocodigo que recibe un número entero y determine:}
#Si es positivo, negativo o 0
#Si es par o inpar
#si es múltiplo de 5

#n=int(input("Ingrese un número: "))
#
#if n < 0:
#    print("El número ingresado es negativo.")
#elif n >=1:
#    print("El número ingresado es positivo.")
#else:
#    print("El número ingresado es 0")
#
#if n % 2 == 0:
#    print("El número ingresado es par.")
#else:
#    print("El número ingresado es impar.")    
#
#if n % 5 == 0:
#    print("El número ingresado es múltiplo de 5.")
#else:
#    print("El número ingresado no es múltiplo de 5.")




#2. Determinar si un Número es Capicúa Un número es capicúa si se lee igual de izquierda a derecha
# que de derecha a izquierda. Escribe un pseudocódigo que determine si un número de tres cifras es capicúa. 

#n=int(input("Ingrese un nuero de tres digitos: "))
#
#a=n % 100
#dig1= n // 100
#dig3= a % 10
#
#if dig1==dig3:
#    print("Es número capicua.")
#else:
#    print("No es número capicua.")




#3. Escribe un pseudocódigo que reciba un número de cuatro dígitos y determine:
#  • Si todos sus dígitos son pares.
#  • Si la suma de sus dígitos es mayor a 20.
#  • Utiliza operadores lógicos y acumuladores para resolverlo. 

#n=int(input("Ingrese un número de 4 dígitos: ")) # 1 2 3 4
#nstr=str(n)
#digit1= int(nstr[0])       #Separacion de los digitos
#digit2= int(nstr[1])     #Separacion de los digitos
#digit3= int(nstr[2])     #Separacion de los digitos
#digit4= int(nstr[3])     #Separacion de los digitos
#
#Deterinar si son par o impar
#if (digit1 % 2 == 0) and (digit2 % 2 == 0) and (digit3 % 2 == 0) and (digit4 % 2 == 0):
#    print("Son pares")
#else:
#    print("Son impares")
#Si la suma de todos los números es mayor a 20
#
#if (digit1+digit2+digit3+digit4)> 20:
#    print("La suma de todos los digitos son mayor a 20")
#else:
#    print("La suma de los 4 digitos no son mayor a 20")

#4. Suma de los Dos Números Mayores Dado tres números distintos, encuentra la suma de los dos mayores. 
#num1=int(input("Ingrese el primer número: "))
#num2=int(input("Ingrese el segundo número: "))
#num3=int(input("Ingrese el tercer número: "))
#
#if (num1==num2 and num1==num3) or (num2==num1 and num2==num3) or (num3==num1 and num3==num2):
#    print("Los 3 números son iguales",num1,num2,num3)
#else:
#    if num1<num2 and num1<num3:
#        suma1=num2+num3
#        print("la suma de los dos mayores son:",suma1)
#    elif num2<num1 and num2<num3:
#        suma2=num1+num3
#        print("la suma de los dos mayores son:",suma2)
#    else:
#        suma3=num1+num2
#        print("la suma de los dos mayores son:",suma3)


#5. Dado un número n, determina si es divisible por 3, por 5 o por ambos usando el operador módulo. 
 
#n= int(input("Ingresa un número"))
#
#if (n % 3 == 0) and (n % 5 == 0):
#    print("El número ingresado es divisor de 3 y 5")
#elif (n % 3 == 0):
#    print("El numero infresado es divisor de 3 pero no de 5")
#elif (n % 5 == 0):
#    print("El numero infresado es divisor de 5 pero no de 3")
#else:
#    print("El numero ingresado no es divisor de 3 ni de 5")


#6. Dada una edad edad, clasifica la persona en uno de los siguientes grupos: 
#  • Si la edad es menor o igual a 18: es un menor de edad.
#  • Si la edad está entre 19 y 65 años: es un adulto.
#  • Si la edad es mayor de 65 años: es un adulto mayor.
#  • Además, si la persona tiene más de 18 años, verifica si es mayor de 30 y, si lo es, imprime "Mayor de 30". 

#edad=int(input("Ingresa tu edad: "))
#
#if edad <= 18:
#    print("Es menor de edad.")
#elif (edad >= 19) and (edad <= 65):
#    print("Es adulto.")
#else:
#    print("Es adulto mayor.")
#
#if (edad > 18) and (edad > 30):
#    print("Es ayor de 30 años.")
#else:
#    print("Es menor de 30 años.")



#7. Dado un número n, clasifícalo en el siguiente rango: 
#A. Si el número es menor que 0, imprímelo como "Número negativo". 
#B. Si el número es mayor o igual a 0 y menor a 10, verifica si es par o impar: 
# a. Si es par, imprímelo como "Número pequeño y par". 
# b. Si es impar, imprímelo como "Número pequeño e impar". 
#C. Si el número es mayor o igual a 10: 
#D. Verifica si es divisible por 2, 3 o 5: 
# a. Si es divisible por 2 y 3, imprímelo como "Número grande, múltiplo de 2 y 3". 
# b. Si es divisible por 5, imprímelo como "Número grande, múltiplo de 5". 
# c. Si no es divisible por 2, 3 ni 5, imprímelo como "Número grande, no es múltiplo de 2, 3 ni 5". 

#n=int(input("Ingrese un número: "))
#
#if n <0:
#    print("Número negativo")
#elif n >=0 and n <=9:
#    if n % 2 == 0:
#        print("Número pequeño par")
#    else:
#        print("Número pequeño impar")
#elif n >= 10:
#    if (n % 2 == 0) and (n % 3 == 0):
#        print("Número grande y es múltiplo de 2, 3.")
#    elif (n % 5 == 0):
#        print("Número grande, es múltiplo de 5")
#    else:
#        print("Número grande no es múltiplo de 2, 3 ni 5.")
#else:
#    print("Número Invalido")


