#Averiguar si el numero ingresado es multiplo de 2 o 3 y de 2 y 3
print("Averiguaremos si el número que ingreses es múltiplo de 2y3 o solo de 2o3")
n=int(input("Ingrése un número "))

if n % 2 == 0 and n % 3 == 0:
    print("El número ingresado es múltiplo de dos y tres.")
elif n % 2 == 0:
    print("El número ingresado solo es múltiplo de dos.")
elif n % 3 == 0:
    print ("El número ingresado solo es múltiplo de tres.")
else:
    print("El número ingresado no es múltiplo de dos ni de tres.")