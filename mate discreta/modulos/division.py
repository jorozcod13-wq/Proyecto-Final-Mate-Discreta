
def calcular_division(a, b):
    """
    Calcula el cociente y el residuo de una división entera.
    Devuelve ambos valores para mostrarlos en la interfaz.
    """

    if b == 0:
        raise ValueError("El divisor no puede ser cero.")

    q = a // b
    r = a % b

    calculo = b * q + r
    condicion_residuo = 0 <= r < abs(b)
    igualdad_correcta = calculo == a

    return q, r
