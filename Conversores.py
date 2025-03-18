menucon="""
CONVERSORES

    1. Monedas
    2. Tempuraturas
    3. Distancia
"""
print(menucon)
menucon=input("¿Que conversor desea utilizar? ")

if menucon == "1":
    menu="""
        BIENVENIDO AL CONVERSOR DE MONEDAS

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

elif menucon == "2":
    menu2="""
    BIENVENIDO AL CONVERSOR DE TEMPERATURA
        1. °Farenheit a °Kelvin
        2. °Farenheit a °Celsius
        3. °Kelin     a °Celsius
        4. °Kelin     a °Farenheit
    """
    print(menu2)
    menu2 = input("¿Que opción desea utilizar? ")

    if menu2 == "1":
        print("Conertir °Farenheit a °Kelvin:")
        cant1=float(input("Ingrese la cantidad de °F a convertir: "))
        print(f"{cant1} °F convertido a °Kelin es de {(cant1-32)*5/9+273.15} °Kelin")
    elif menu2 == "2":
        print("°Farenheit a °Celsius:")
        cant2=float(input("Ingrese la cantidad de °F a convertir: "))
        print(f"{cant2} °F convertido a °Celsius es de {(cant2-32)*5/9} °Celsius")
    elif menu2 == "3":
        print("°Kelin a °Celsius:")
        cant3=float(input("Ingrese la cantidad de °Kelvin a convertir: "))
        print(f"{cant3} °Kelvin convertido a °Celsius es de {cant3-273.15} °Celsius")
    elif menu2 == "3":
        print("°Kelin a °Farenheit:")
        cant4=float(input("Ingrese la cantidad de °Kelvin a convertir: "))
        print(f"{cant4} °Kelvin convertido a °Celsius es de {(cant4-273.15)*9/5+32} °Farenheit")
    else:
        print("ERROR  Opción invalida")

elif menucon == "3":
    menu3="""
    BIENVENIDO AL CONVERSOR DE DISTANCIAS
        1. Pulgadas    a Cm, M y Pies
        2. Centimetros a Pulgada, m y pies
    """
    print(menu3)

    menu3=input("¿Que opción que desea utilizar?")
    
    if menu3 == "1":
        print("Convertir pulgadas a Cm, M y Pies: ")
        op1=float(input("Ingrese las pulgadas que desea convertir: "))
        print(f"{op1} Pulgadas convertido a Cm da {op1*2.54} Cm")
        print(f"{op1} Pulgadas convertido a Metros da {op1/39.37} M")
        print(f"{op1} Pulgadas convertido a Pies da {op1/12} Pies")
    elif menu3 == "2":
        print("Convertir centimetros a Pulgada, M y Pies: ")
        op2=float(input("Ingrese los centimetros que desea convertir: "))
        print(f"{op2} Centimetros convertido a Pulgadas da {op2/2.54} Pulgadas")
        print(f"{op2} Centimetros convertido a Metros da {op2/100} M")
        print(f"{op2} Centimetros convertido a Pies da {op2/30.48} Pies")
    else:
        print("ERROR Opción invalida")
else:
    print("ERROR Opción invalida")