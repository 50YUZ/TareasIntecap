#1
#numeros=[7,8,9,10]
#suma=0
#for n in numeros:
#    suma += n
#    promedio=suma / len(numeros)

#print("Promedio:", promedio)

#2
#numeros=[12,45,7,89,23]
#mayor=0
#for num in numeros:
#    if num>mayor:
#        mayor=num
#print("El mayor es: ",mayor)

#3
#num=[1,4,7,8,10,3]
#pares=0
#for n in num:
#    if n%2==0:
#        pares += 1

#print("Cantidad de pares: ", pares)

#4
#lis=[5,10,15,20]
#lis_in=[]
#for i in range(len(lis)-1,-1,-1):
#    lis_in.append(lis[i])
#print("Lista invertida: ", lis_in)

#5
#a=[1,2,3]
#b=[4,5,6]
#resultado=[]
#for i in range(len(a)):
#    resultado.append(a[i]+b[i])
#print("Suma: ", resultado)

#6
#lis=[1,3,5,3,9,3,7]
#buscar=3
#contador=0
#for elemento in lis:
#    if elemento == buscar:
#        contador += 1
#print(f"Aparece {contador} veces")

#7
#ori=[4,15,9,20,2,18]
#nue={}
#for n in ori:
#    if n>10:
#        nue.append(n)
#print(f"Mayores a 10: {nue}")

#8
#nu=[11,22,33,44]
#bus=33
#enc=False
#for n in nu:
#    if n == bus:
#        print("Si esta en la lista.")
#        break
#if n != bus:
#    print("No esta en la lista")

#9
#lis=[2,5,7,8,11]
#suma=0
#for num in lis:
#    if num %2 != 0:
#        suma += num
#print("La suma de impares: ",suma)

#10
#lis=[4,5,4,7,5,8,4]
#lis_sin=[]
#for n in lis:
#    if n not in lis_sin:
#        lis_sin.append(n)
#print("Lista sin duplicados", lis_sin)

#Detecta el bug

#1
#numeros=[3,6,9]
#for i in range(4):#El numero 4 esta fuera de rango en la lista
#for i in range(3): 
#    print(numeros[i])

#2
#frutas=[]
#frutas=["mango","fresa","etc"]
#print(frutas[0])#No puede imprimir una lista vacia

#3
#lista=[2,4,6]
#suma=0
#for num in lista:
#    suma += num#aun no se declara la variable suma
#print=suma

#4
#edades = [15, 22, 30, 18]
#mayores = 0
#for e in edades:
#    if e > 18:
#        mayores =+ 1  # al sumar el contador en lugar de ir =+ deberia ir +=
#print("Mayores de 18:", mayores)


#5
#nombres = ["Ana", "Luis", "María"]
#if nombres == "Luis":  #El dato "Luis" y l avariabl enombres estan en el lugar opuesto
#if "Luis" in nombres:  # En lugar de igualar el dato "Luis" la intruccion seria buscar en la lista  
#    print("Está Luis")


#6
#numeros = [10, 20, 30]
#print("Suma: " + sum(numeros))  # El signo "+" no es una erramienta para concatenar
#print("Suma", sum(numeros))