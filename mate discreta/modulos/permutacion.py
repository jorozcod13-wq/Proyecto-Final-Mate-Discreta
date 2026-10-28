# CÓDIGO ADAPTADO PARA MATHLAB
# Se modificó la función para recibir los datos
# desde la interfaz gráfica 
# y se cambio el nombre de las funciones 
def factorial_permutaciones(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


def permutaciones(n, r):
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n debe ser un entero.")

    if not isinstance(r, int) or isinstance(r, bool):
        raise ValueError("r debe ser un entero.")

    if n < 0 or r < 0 or r > n:
        raise ValueError("Debe cumplirse que 0 <= r <= n.")

    return factorial_permutaciones(n) // factorial_permutaciones(n - r)

# CÓDIGO ORIGINAL
# Autor: Melissa Bautista
# Se conserva como referencia del código inicial.

#def factorial(n):
    #resultado = 1

    #for i in range(1, n + 1):
        #resultado *= i
    #return resultado
#def permutaciones(n, r):
    #if n < 0 or r < 0 or r > n:
        #return None
    #return factorial(n) // factorial(n - r)
#n = int(input("Ingrese el valor de n: "))
#r = int(input("Ingrese el valor de r: "))
#resultado = permutaciones(n, r)
#if resultado is None:
    #print("Error: debe cumplirse 0 <= r <= n.")
#else:
    #print("P(", n, ",", r, ") =", resultado)