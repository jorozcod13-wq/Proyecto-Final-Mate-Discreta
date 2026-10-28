
def calcular_mcd(a, b):
    a = abs(a)
    b = abs(b)

    if a == 0 and b == 0:
        raise ValueError("El MCD de 0 y 0 no está definido.")

    while b != 0:
        a, b = b, a % b

    return a


def calcular_mcd_pasos(a, b):
    if a == 0 and b == 0:
        raise ValueError("El MCD de 0 y 0 no está definido.")

    original_a = a
    original_b = b

    a = abs(a)
    b = abs(b)

    pasos = [
        "ALGORITMO DE EUCLIDES",
        f"Calcularemos MCD({original_a}, {original_b}).",
        "",
        "Regla: dividendo = divisor × cociente + residuo",
        ""
    ]

    if original_a < 0 or original_b < 0:
        pasos.append(
            f"Usamos valores absolutos: MCD({a}, {b})."
        )
        pasos.append("")

    if a == 0 or b == 0:
        resultado = max(a, b)
        pasos.append(
            f"Como uno de los números es 0, "
            f"el MCD es {resultado}."
        )
        return resultado, "\n".join(pasos)

    numero_paso = 1

    while b != 0:
        cociente = a // b
        residuo = a % b

        pasos.append(f"Paso {numero_paso}:")
        pasos.append(
            f"{a} = {b} × {cociente} + {residuo}"
        )

        if residuo != 0:
            pasos.append(
                f"Nuevo par de números: {b} y {residuo}."
            )
        else:
            pasos.append(
                f"El residuo es 0. El MCD es {b}."
            )

        pasos.append("")

        a, b = b, residuo
        numero_paso += 1

    pasos.append(f"RESULTADO FINAL: MCD = {a}")

    return a, "\n".join(pasos)
