#arr=int(input("Ingrese el tamaño del arreglo: "))
#base=int(input("Ingrese la base: "))

#lista=[]

#for i in range(1,arr + 1):
#    lista.append(base*i)

#print(lista)





#EJERCICIO 2
#tam=int(input("Ingrese el tamaño: "))
#nombres=[]
#long=[]
#for i in range(1,tam):
#    nombre=input("Ingresa un nombre:")
#    lon=len(nombre)
#    long.append(lon)
#    nombres.append(nombre)
#print(nombres)
#print(long)










#Escenario1



n = int(input("Ingresa la cantidad de clientes atendidos: "))          # Solicitar cantidad de clientes

respuestas = []

print("Ingresa las respuestas de atención (del 1 al 5):")              # Pedir las respuestas de cada cliente
for i in range(n):
    valor = int(input("Cliente " + str(i + 1) + ": "))
    respuestas.append(valor)

# 
contadores = [0, 0, 0, 0, 0]  # Índices: 0=Malo, 1=Regular, ..., 4=Excelente Contadores para cada tipo de respuesta

for respuesta in respuestas:
    if 1 <= respuesta <= 5:
        contadores[respuesta - 1] += 1


tipos = ["Malo", "Regular", "Buena", "Muy Buena", "Excelente"] # Mostrar totales por tipo
print("Respuestas:")
for i in range(5):
    print(tipos[i] + ": " + str(contadores[i]))


max_frecuencia = max(contadores)                            # Encontrar respuesta más frecuente
indice_frecuente = contadores.index(max_frecuencia)
respuesta_mas_frecuente = indice_frecuente + 1
print("b) Más frecuente: " + str(respuesta_mas_frecuente))


suma = 0                                   # Calcular promedio
for valor in respuestas:
    suma += valor
promedio = suma / n
print("c) Promedio: " + str(round(promedio, 2)))


menores = 0                                            # Calcular porcentaje de respuestas menores al promedio
for valor in respuestas:
    if valor < promedio:
        menores += 1

porcentaje_menores = (menores / n) * 100
print("Porcentaje menor al promedio: " + str(round(porcentaje_menores)) + "%")