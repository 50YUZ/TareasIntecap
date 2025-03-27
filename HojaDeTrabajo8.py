                     #1.	Contador de números pares

#contador= 0

#while contador <= 3:
#    print(f"el contador es " {contador})
#    contador+=1

#numero= int(input("Imgrese un número"))
#contador=0
#n=1

#while n < numero:
#    if n % 2 == 0:
#        contador+=1
#    n+=1
#print("Existen", contador, "números pares")


                   #2.	Cálculo de la suma de los primeros N números

#numero=int(input("Ingrese un número: "))
#suma=0
#n=1

#while n <= numero:
#    suma=suma+n
#    n+=1
#print(f"La suma es {suma}")

#numero=int(input("Ingrese un numero: "))
#f=1
#n=1

#while n <= numero:
#    f*=n
#    n+=1
#print(f"El resultado es {f}")




                  #4.	Adivinar un número secreto

#num_secre=45

#while True:
#    num_usuar=int(input("El número secreto esta entre 1 y 100 "))
#    if num_usuar == num_secre:
#        print(f"Felicdades, el numero secreto es {num_secre}")
#        break
#    elif num_usuar < num_secre:
#        print(f"El número secreto es mayor a {num_usuar}")
#    elif num_usuar > num_secre:
#        print(f"El numero secreto es menor que {num_usuar}")






                      #5.	Verificación de contraseña

#contrasena=123789
#i=3

#while True:
#    usuaruio=int(input("Ingrese la cotraseña "))
#    if usuaruio == contrasena:
#        print("Contraseña correcta, BIENVENIDO:)")
#        break
#    else:
#        i= i-1
#        print(f"ERROR Contraseña invorrecta, números de intentos sobrantes : {i} antes de bloquear la cuenta ")
#        if i == 0:
#            print("Limite de intentos alcanzados, cuenta bloqueada")
#            break






              #6.	Validar una contraseña fuerte

#import re
#while True:
#    contra=input("Ingrese una Contraseña: ")
#    if len(contra) < 8:
#        print(f"La contraseña {contra} tiene que tener mínimo 8 carateres")     #re.search = devuelve un objeto match si el patron se encuentra en la cadena o None si no se encuentra
#    elif not re.search("[a-z]",contra):
#        print(f"La contraseña {contra} debe tener como mínimo una minúscula")
#    elif not re.search("[A-Z]",contra):
#        print(f"La contraseña {contra} debe tener como mínimo una mayúscula")
#    elif not re.search("[0-9]",contra):
#        print(f"La contraseña {contra} debe tener como mínimo un número")
#else:
#    print("Contraseña valida")





              #7.	Simulación de propagación de una epidemia

tasa_contagio = 1.5

pobla_total = int(input("Ingresa la población total: "))
infec = int(input("Ingresa la cantidad de infectados actuales: "))
dias = int(input("Ingresa el número de días a simular: "))

for dia in range(1, dias + 1):                #for esta para iterar la secuencia de elementos
    nue_infec = infec * tasa_contagio

    if infec + nue_infec > pobla_total:
        nue_infec = pobla_total - infec

    infec += nue_infec

    print(f"Día {dia}: {int(infec)} infectados")

    if infec >= pobla_total:
        print("Toda la población ha sido infectada.")
        break