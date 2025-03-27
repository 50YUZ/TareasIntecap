contrasena=int(7878)
i=3


while True:
    menu="""
      CAJERO AUTOMATICO
    0. Finalizar proceso
    1. Retirar dinero
    """
    print(menu)

    selector=input("Elige una opción: ")
    
    if selector == "0":
        print("Proceso finalizado")
        break
    elif selector == "1":
        usuaruio=int(input("Ingrese la cotraseña "))
        if usuaruio == contrasena:
            print("Contraseña correcta, BIENVENIDO:)")
            saldo=3000
            retirar=int(input("¿Cuanto deseas retira? "))
            if retirar > saldo:
                i=i-1
                print(f"Saldo insuficiente, intentos restantes: {i}")
            else:
                saldo=saldo-retirar
                print(f"Acabas de retirar {retirar} tu saldo reswtante es de {saldo}")
            if saldo==0:
                print("Ya no tienes dinero en tu cuenta :(")
                break
            if i<0:
                print("Limite de intentos alcanzado, cuenta bloqueada")
                break
    else:
        print("Opción invalida, por favor intentelo de nuevo")