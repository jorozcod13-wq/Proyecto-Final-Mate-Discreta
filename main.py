from combinaciones import combinaciones

n = int(input("Ingrese el total de elementos: "))
r = int(input("Ingrese cuántos desea elegir: "))

try:
    resultado = combinaciones(n, r)
    print("Número de combinaciones:", resultado)
except ValueError as error:
    print("Error:", error)