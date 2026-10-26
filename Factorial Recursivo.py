def factorial_recursivo(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def mostrar_pasos_recursivos(n: int, nivel: int = 0) -> int:
    indentacion = "  " * nivel

    # Caso Base
    if n == 0 or n == 1:
        print(f"{indentacion}--> Base alcanzada: {n}! = 1")
        return 1

    # Caso Recursivo
    print(f"{indentacion}--> Llama a: {n} * factorial({n - 1})")
    subresultado = mostrar_pasos_recursivos(n - 1, nivel + 1)
    resultado = n * subresultado
    print(f"{indentacion}<-- Retorna: {n} * {subresultado} = {resultado}")

    return resultado

if __name__ == "__main__":
    print("==================================================")
    print("   MATEMÁTICA DISCRETA: FACTORIAL RECURSIVO")
    print("==================================================\n")

    # Ejemplos predefinidos de prueba
    ejemplos = [0, 1, 5, 7]
    print("--- 1. Ejemplos Rápidos ---")
    for num in ejemplos:
        print(f"El factorial de {num}! es: {factorial_recursivo(num)}")

    print("\n--- 2. Traza Paso a Paso de la Pila Recursiva (Ejemplo n = 4) ---")
    mostrar_pasos_recursivos(4)

    print("\n--- 3. Modulo Interactivo ---")
    try:
        entrada = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
        if entrada < 0:
            print("Error: El factorial no está definido para números enteros negativos.")
        else:
            res = factorial_recursivo(entrada)
            print(f"\nResultado final: {entrada}! = {res}")
    except ValueError: