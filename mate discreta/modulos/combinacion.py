def factorial_combinaciones(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_combinaciones(n - 1)


def combinaciones(n, r):
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n debe ser un entero")

    if not isinstance(r, int) or isinstance(r, bool):
        raise ValueError("r debe ser un entero")

    if n < 0 or r < 0 or r > n:
        raise ValueError("Debe cumplirse que 0 <= r <= n")

    resultado = factorial_combinaciones(n) // (
        factorial_combinaciones(r) * factorial_combinaciones(n - r)
    )

    return resultado