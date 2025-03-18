menu="""
BIENVENIDO AL CONVERSOR DE DINERO

    1. Convertir Quetzales a Pesos.
    2. Convertir Quetzales a Dolares.
    3. Convertir Quetzales a Euros.
    4. Convertir Pesos     a Quetzales.
    5. Convertir Pesos     a Dolares.
    6. Convertir Pesos     a Euros.
"""
print(menu)

menu=input("¿Que opción deseas ejeutar? ")

if menu == "1":
    print("Convertir Quetzales a Pesos.")
    cantidad1=int(input("Ingrese la cantidad que desee convertir a pesos: "))
    conqap=cantidad1*2.63
    print(cantidad1,"Quetzales convertido a pesos da un total de: ", conqap,"Pesos")
elif menu == "2":
    print("Convertir Quetzales a Dolares.")
    cantidad2=int(input("Ingrese la cantidad que desee convertir a dolares: "))
    conqad=cantidad2*0.13
    print(cantidad2,"Quetzales convertido a dolares da un total de: ", conqad,"dolares")
elif menu == "3":
    print("Convertir Quetzales a Euros..")
    cantidad3=int(input("Ingrese la cantidad que desee convertir a euros: "))
    conqae=cantidad3*0.12
    print(cantidad3,"Quetzales convertido a euros da un total de: ", conqae,"euro")
elif menu == "4":
    print("Convertir Pesos a Quetzales.")
    cantidad4=int(input("Ingrese la cantidad que desee convertir a quetzales: "))
    conpaq=cantidad4*2.63
    print(cantidad4,"Pesos convertido a quetzales da un total de: ", conpaq,"quetzales")
elif menu == "5":
    print("Convertir Pesos a Dolares.")
    cantidad5=int(input("Ingrese la cantidad que desee convertir a dolares: "))
    conpad=cantidad5*0.0498
    print(cantidad5,"Pesos convertido a pesos da un total de: ", conpad,"dolares")
elif menu == "6":
    print("Convertir Pesos a Euros.")
    cantidad6=int(input("Ingrese la cantidad que desee convertir a euros: "))
    conpae=cantidad6*0.04
    print(cantidad6,"Pesos convertido a pesos da un total de: ", conpae,"euros")
else:
    print("ERROR  Opición Invalida")