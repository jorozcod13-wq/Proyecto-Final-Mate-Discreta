def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i
    return resultado
def permutaciones(n, r):
    if n < 0 or r < 0 or r > n:
        return None
    return factorial(n) // factorial(n - r)
n = int(input("Ingrese el valor de n: "))
r = int(input("Ingrese el valor de r: "))
resultado = permutaciones(n, r)
if resultado is None:
    print("Error: debe cumplirse 0 <= r <= n.")
else:
    print("P(", n, ",", r, ") =", resultado)