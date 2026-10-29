# CÓDIGO ADAPTADO PARA MATHLAB
# Se modificó la función para recibir los datos
# desde la interfaz gráfica y devolver el cociente
# y el residuo para mostrarlos en pantalla.

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
 



# CÓDIGO ORIGINAL
# Autor: Josué Fuentes
# Se conserva como referencia del código inicial.

#def algoritmo_division_interactivo():
    #print("=== CÁLCULO DEL ALGORITMO DE LA DIVISIÓN ===")

    #try:
        # Entrada manual de datos por el usuario
       # a = int(input("Ingresa el valor del dividendo (a): "))
       # b = int(input("Ingresa el valor del divisor (b): "))

        # Validación del divisor cero
       # if b == 0:
           # print("Error: El divisor (b) no puede ser cero.")
           # return

        # Cálculo del cociente y residuo usando operadores de Python
       # q = a // b  # Cociente entero
        #r = a % b   # Residuo

        # Resultados en pantalla
       # print("\n--- RESULTADOS ---")
        #print(f"Dividendo (a) : {a}")
       # print(f"Divisor (b)   : {b}")
        #print(f"Cociente (q)  : {q}")
        #print(f"Residuo (r)   : {r}")

        # Comprobación de la igualdad a = b * q + r
        #calculo = b * q + r
       # print(f"\nComprobación: {b} * ({q}) + {r} = {calculo}")

        # Validación estricta de las condiciones del residuo ($0 \le r < |b|$)
        #condicion_residuo = 0 <= r < abs(b)
        #igualdad_correcta = (calculo == a)

       # if igualdad_correcta and condicion_residuo:
           # print("¡Validación exitosa! Se cumple la igualdad y la condición del residuo.")
       # else:
           # print("Atención: Los valores no cumplen con las restricciones matemáticas.")

    #except ValueError:
        #print("Error: Por favor, introduce únicamente números enteros válidos.")

#if __name__ == "__main__":
   #algoritmo_division_interactivo()


