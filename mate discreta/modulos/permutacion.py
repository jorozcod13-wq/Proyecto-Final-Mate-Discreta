
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
