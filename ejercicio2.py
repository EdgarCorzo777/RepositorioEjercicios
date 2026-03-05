try:
    estudiantes = int(input("Ingrese la cantidad de estudiantes a evaluar: "))
except ValueError:
    print("Error: Ingrese solo valores numericos")

nota1 = 0
nota2 = 0
nota3 = 0
promedioTotal = 0
estudiantesTotal = 0
aprobados = 0
reprobados = 0

for i in range(1, estudiantes+1):
    nombre = input("Ingresa tu nombre: ")

    try:
        nota1 = float(input("Ingrese la primera nota (0-5)"))
        nota2 = float(input("Ingrese la segunda nota (0-5)"))
        nota3 = float(input("Ingrese la tercera nota (0-5)"))

        if nota1 < 0 or nota1 > 5 or nota2 < 0 or nota2 > 5 or nota3 < 0 or nota3 > 5:
            print("Por favor ingrese solo notas validas (0-5)")
            break

    except ValueError:
        print("Error: Ingresar solo valores numericos")
        break

    promedio = (nota1+nota2+nota3)/3
    promedioTotal += promedio
    estudiantesTotal = i
    if promedio >= 3.0:
        aprobados += 1
        print(f"\n{nombre}, aprobaste con un promedio de: {promedio:.1f}\n")
    else:
        reprobados += 1
        print(f"\n{nombre}, reprobaste con un promedio de: {promedio:.1f}\n")

promedioFinal = promedioTotal/estudiantesTotal

print(f"Aprobaron un total de {aprobados} estudiantes, reprobaron {reprobados} estudiantes, y el promedio final fue de {promedioFinal:.1f}.")
    