parqueaderoCarros = 5
totalEspacio = 10
minimoCarros = 0

print("* BIENVENIDO AL PARQUEADERO *")
print(f"Estado actual: {parqueaderoCarros}/{totalEspacio} espacios ocupados")

while True:

    decision = input("Que desea hacer? Ingresar un carro, retirarlo o salir (i/r/s)? ").lower()

    
    if decision == "i":
        if parqueaderoCarros < totalEspacio:
            parqueaderoCarros += 1
            print(f"Su carro ha sido guardado correctamente, Estado: {parqueaderoCarros}/{totalEspacio} carros en el parqueadero")
        else:
            print("Error: No hay mas espacio en el parqueadero.")

    elif decision == "r":
        if parqueaderoCarros > minimoCarros:
            parqueaderoCarros -= 1
            print(f"Su carro ha sido retirado correctamente, Estado: {parqueaderoCarros}/{totalEspacio} carros en el parqueadero")
        else:
            print("Error: No hay carros disponibles.")

    elif decision == "s":
        print("Hasta luego, vuelva pronto")
        break
    
    else:
        print("Opcion no valida, intente nuevamente.")
        