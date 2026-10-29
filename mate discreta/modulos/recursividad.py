# CÓDIGO ADAPTADO PARA LA INTERFAZ GRÁFICA:
# Se adaptó la presentación de los pasos recursivos para
# mostrarlos en la interfaz en lugar de imprimirlos en la terminal.
# Se incorporó la función obtener_pasos_recursivos(n) para
# generar el procedimiento como texto.
# La interfaz muestra los pasos y el resultado del factorial.
# Se añadieron validaciones para evitar entradas inválidas
# y números negativos.
# Se conserva la lógica recursiva del código original.

def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de n mediante recursividad.

    Caso base:
        0! = 1
        1! = 1

    Caso recursivo:
        n! = n * (n - 1)!
    """
    if n < 0:
        raise ValueError(
            "El factorial no está definido para números negativos."
        )

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursivo(n - 1)



def mostrar_pasos_recursivos(n: int, nivel: int = 0) -> list[str]:
    """
    Registra las llamadas y los retornos del factorial recursivo.
    Cada paso se guarda como una línea independiente.
    """
    if n < 0:
        raise ValueError(
            "El factorial no está definido para números negativos."
        )

    pasos = []
    indentacion = "    " * nivel

    # Caso base
    if n == 0 or n == 1:
        pasos.append(
            f"{indentacion}CASO BASE: factorial({n}) = 1"
        )
        pasos.append(
            f"{indentacion}RETORNO: 1"
        )
        return pasos

    # Llamada recursiva
    pasos.append(f"{indentacion}LLAMADA: factorial({n})")
    pasos.append(
        f"{indentacion}Se calcula {n} * factorial({n - 1})"
    )

    pasos.extend(
        mostrar_pasos_recursivos(n - 1, nivel + 1)
    )

    # Resultado al regresar de la llamada
    subresultado = factorial_recursivo(n - 1)
    resultado = n * subresultado

    pasos.append(
        f"{indentacion}RETORNO: {n} * {subresultado} = {resultado}"
    )

    return pasos




def obtener_pasos_recursivos(n: int) -> str:
    if n < 0:
        raise ValueError(
            "El factorial no está definido para negativos."
        )

    resultado = factorial_recursivo(n)

    lineas = [
        "RECURSIVIDAD: FACTORIAL",
        "",
        "CASO BASE",
        "0! = 1 y 1! = 1",
        "",
        "CASO RECURSIVO",
        "n! = n * (n - 1)!",
        "",
        "PROCEDIMIENTO"
    ]

    if n <= 6:
        for numero in range(n, 0, -1):
            lineas.append(
                f"{numero}! = {numero} * {numero - 1}!"
            )

        lineas.append("0! = 1")
        lineas.append("")
        lineas.append("RETORNO")

        acumulado = 1
        for numero in range(1, n + 1):
            anterior = acumulado
            acumulado *= numero
            lineas.append(
                f"{numero} * {anterior} = {acumulado}"
            )
    else:
        lineas.append(
            f"Se realizan llamadas desde factorial({n})"
        )
        lineas.append("hasta alcanzar el caso base.")
        lineas.append(
            f"Después se multiplican los valores al retornar."
        )

    lineas.extend([
        "",
        "RESULTADO FINAL",
        f"{n}! = {resultado}"
    ])

    return "\n".join(lineas)


# CÓDIGO ORIGINAL
# Autor: Javier Velazquez
# Se conserva como referencia del código inicial.

#def factorial_recursivo(n: int) -> int:
    #if n == 0 or n == 1:
        #return 1
    #return n * factorial_recursivo(n - 1)

#def mostrar_pasos_recursivos(n: int, nivel: int = 0) -> int:
    #indentacion = "  " * nivel

    # Caso Base
    #if n == 0 or n == 1:
        #print(f"{indentacion}--> Base alcanzada: {n}! = 1")
        #return 1

    # Caso Recursivo
    #print(f"{indentacion}--> Llama a: {n} * factorial({n - 1})")
    #subresultado = mostrar_pasos_recursivos(n - 1, nivel + 1)
    #resultado = n * subresultado
    #print(f"{indentacion}<-- Retorna: {n} * {subresultado} = {resultado}")

    #return resultado

#if __name__ == "__main__":
    #print("==================================================")
    #print("   MATEMÁTICA DISCRETA: FACTORIAL RECURSIVO")
    #print("==================================================\n")

    # Ejemplos predefinidos de prueba
    #ejemplos = [0, 1, 5, 7]
    #print("--- 1. Ejemplos Rápidos ---")
    #for num in ejemplos:
       # print(f"El factorial de {num}! es: {factorial_recursivo(num)}")

    #print("\n--- 2. Traza Paso a Paso de la Pila Recursiva (Ejemplo n = 4) ---")
    #mostrar_pasos_recursivos(4)

    #print("\n--- 3. Modulo Interactivo ---")
    #try:
        #entrada = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
        #if entrada < 0:
           # print("Error: El factorial no está definido para números enteros negativos.")
        #else:
            #res = factorial_recursivo(entrada)
            #print(f"\nResultado final: {entrada}! = {res}")
   # except ValueError:

