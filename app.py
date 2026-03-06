# def saludar(nombre):
#     print("Hola", nombre)

# nombre1 = input("Hola, ingresa tu nombre: ")
# saludar(nombre1)

# nombre2 = input("Hola, ingresa tu nombre: ")
# saludar(nombre2)


def calcular_total(precio, cantidad, iva = 0.19):
    print(f"iva -> {iva}")
    subtotal = precio * cantidad
    iva = subtotal * iva
    total = subtotal + iva
    print(total)
    return total

#Producto 1: 2000 - 5
#Producto 2: 5000 - 7

total1= calcular_total(2000, 5)
total2= calcular_total(5000, 7)
# print(total1 + total2)