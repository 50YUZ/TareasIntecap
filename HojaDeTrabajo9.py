# Ejercicio1
#Crear un bucle for que cuente del 0 a 10, e imprima números impares en la pantalla
#for i in range(1,11):
#    if not i % 2 == 0:
#        print(F"Números impares: {i}")



#Ejercicio2
#n=1
#while n < 11:
#    if not n % 2 == 0:
#        print(f"Números impares: {n}")
#    n+=1






#Esenario 1
#L a instrucción break se implemeta para sali/terminar bucle
#Diseña un programa que use un bucle whiley le pida continuamente al usuario que
#Ingrese una palabra a menos que ingrese "chupacabras" como palabra de salida secreta,
#en cuyo caso el mensaje "Has dejado el bucle con éxito". Debe imprimirse en la pantalla y
#el bucle debe terminar.

#salida_secreta="chupacabras"
#while True:
#    palabra=input("Escribe una palabra")
#    if palabra == salida_secreta:
#        print("Has dejado el bucle con éxito")
#        break
#    else:
#        continue










#Esenario 2
#La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración,
#sin ejecutar las sentencias dentro del bucle.
#Se pued usar tanto con whle como for.
#Tu tarea aqui es muy especiañ, ¡Debes diseñar un devorador de vocales! Escribe un
#programa que use
#   Un bucle for
#   un concepto de ejecución condicional (if-elif-else)
#   La sentencia continue
#Tu programa debe:
#   Pedir al usuario que ingrese una palabra
#   Utiliza user_word=user_word.upper() para convertir las palabras ingresadas por el usuario en mayúsculas
#   Utiliza ejecución condicional y la instrucción continue para "comer" las siguientes vocales "A-U" de la palabra ingresada
#   Imprime las letras no consumidas en la pantalla. cada una de ellas en una linea
#   Prueba tu programa con los datos que proporcionamos

#palabra=input("Ingresda una palabra: ")
#vocales="AEIOU"
#mayus=palabra=palabra.upper()
#for i in palabra:
#    if i in vocales:
#        continue
#    print(i)





#Escenario 3
#Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.
#Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
#La figura ilustra la regla utilizada por los constructores:

#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
#Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.


blo=int(input("Ingrese el núero de bloques: "))

al=0
blo_ne=1

while blo>=blo_ne:
    blo -= blo_ne
    al += 1
    blo_ne += 1
print(f"La altura de la piramide es de: {al}")