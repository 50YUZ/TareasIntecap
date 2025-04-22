vuelos = [] 
reservas = []

#Función para crear un vuelo

def crear_vuelo():
    codigo = input("Ingrese el código del vuelo: ") 
    origen = input("Ingrese el origen del vuelo: ") 
    destino = input("Ingrese el destino del vuelo: ") 
    cantidad_asientos = int(input("Ingrese la cantidad de asientos disponibles: ")) 
    asientos = [1] * cantidad_asientos  # 1 representa asiento disponible, 0 ocupado 
    vuelo = { "codigo": codigo, "origen": origen, "destino": destino, "asientos": asientos } 
    vuelos.append(vuelo) 
    print("\nVuelo creado exitosamente.\n")

#Función para mostrar los vuelos disponibles

def mostrar_vuelos(): 
    print("\nVuelos disponibles:") 
    for i, vuelo in enumerate(vuelos): 
         print(f"{i + 1}. Código: {vuelo['codigo']}, Origen: {vuelo['origen']}, Destino: {vuelo['destino']}")

#Función para reservar un asiento en un vuelo

def reservar_vuelo(): 
    if not vuelos: 
        print("\nNo hay vuelos disponibles.\n") 
        return

    mostrar_vuelos()
    opcion = int(input("Seleccione el número de vuelo a reservar: ")) - 1

    if 0 <= opcion < len(vuelos):
        vuelo = vuelos[opcion]
        print("Asientos disponibles (1=Disponible, 0=Ocupado):")
        print(vuelo["asientos"])
        asiento = int(input("Seleccione el número de asiento (0 a {}): ".format(len(vuelo["asientos"]) - 1)))

        if 0 <= asiento < len(vuelo["asientos"]):
            if vuelo["asientos"][asiento] == 1:
                nombre = input("Ingrese su nombre: ")
                vuelo["asientos"][asiento] = 0  # Marcar asiento como reservado
                reservas.append({
                    "nombre": nombre,
                    "codigo_vuelo": vuelo["codigo"],
                    "asiento": asiento
                })
                print("\nReserva realizada con éxito.\n")
            else:
                print("\nEl asiento ya está ocupado.\n")
        else:
            print("\nNúmero de asiento inválido.\n")
    else:
        print("\nOpción inválida.\n")
#Función para ver las reservas realizadas

def ver_reservas(): 
    if not reservas: 
        print("\nNo hay reservas realizadas.\n") 
        return 
    print("\nReservas realizadas:") 
    for r in reservas: 
        print(f"Pasajero: {r['nombre']}, Vuelo: {r['codigo_vuelo']}, Asiento: {r['asiento']}")

#Menú principal

def menu(): 
    while True: 
        print("\nSistema de Reserva de Vuelos") 
        print("1. Crear vuelo") 
        print("2. Reservar vuelo") 
        print("3. Ver reservas") 
        print("4. Salir") 
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_vuelo()
        elif opcion == "2":
            reservar_vuelo()
        elif opcion == "3":
            ver_reservas()
        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.\n")

#Ejecutar menú

menu()