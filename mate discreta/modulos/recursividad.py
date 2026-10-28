
def factorial_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para negativos.")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursivo(n - 1)


def mostrar_pasos_recursivos(n: int, nivel: int = 0) -> int:
    indentacion = "  " * nivel

    if n == 0 or n == 1:
        print(f"{indentacion}--> Base alcanzada: {n}! = 1")
        return 1

    print(f"{indentacion}--> Llama a: {n} * factorial({n - 1})")
    subresultado = mostrar_pasos_recursivos(n - 1, nivel + 1)
    resultado = n * subresultado
    print(f"{indentacion}<-- Retorna: {n} * {subresultado} = {resultado}")

    return resultado


def obtener_pasos_recursivos(n: int) -> str:
    from io import StringIO
    from contextlib import redirect_stdout

    if n < 0:
        raise ValueError("El factorial no está definido para negativos.")

    salida = StringIO()

    with redirect_stdout(salida):
        resultado = mostrar_pasos_recursivos(n)

    return salida.getvalue() + f"\nResultado final: {n}! = {resultado}"
