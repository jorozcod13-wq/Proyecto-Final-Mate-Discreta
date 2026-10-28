
import tkinter as tk
from tkinter import messagebox
from math import factorial
from modulos.mcd import calcular_mcd
from modulos.division import calcular_division
from modulos.permutacion import permutaciones, factorial_permutaciones
from modulos.combinacion import combinaciones, factorial_combinaciones
from modulos.recursividad import (
    factorial_recursivo,
    obtener_pasos_recursivos
)

# Paleta de colores
FONDO = "#0B1020"
PANEL = "#14213A"
TARJETA = "#1B2B48"
CIAN = "#27DFFF"
VIOLETA = "#8B7CFF"
BLANCO = "#EAF2FF"
SECUNDARIO = "#8FA3BF"
BORDE = "#30415F"


# Ventana principal
ventana = tk.Tk()
ventana.title("MathLab | Matemática Discreta")
ventana.geometry("1200x760")
ventana.minsize(950, 620)
ventana.configure(bg=FONDO)

menu = tk.Frame(ventana, bg=PANEL, width=245)
menu.pack(side="left", fill="y")
menu.pack_propagate(False)

contenido = tk.Frame(ventana, bg=FONDO)
contenido.pack(side="left", fill="both", expand=True)


# Menú lateral
logo = tk.Label(
    menu, text="∑  MATHLAB", font=("Helvetica", 23, "bold"),
    bg=PANEL, fg=CIAN
)
logo.pack(pady=(32, 5))

subtitulo = tk.Label(
    menu, text="MATEMÁTICA DISCRETA", font=("Helvetica", 9),
    bg=PANEL, fg=SECUNDARIO
)
subtitulo.pack(pady=(0, 30))

tk.Frame(menu, bg=BORDE, height=1).pack(
    fill="x", padx=20, pady=(0, 20)
)

botones_menu = {}
pantalla_activa = "Inicio"


def mostrar_pantalla(nombre):
    global pantalla_activa
    pantalla_activa = nombre

    for widget in contenido.winfo_children():
        widget.destroy()

    for titulo, label in botones_menu.items():
        if titulo == nombre:
            label.configure(bg=VIOLETA, fg=BLANCO)
        else:
            label.configure(bg=CIAN, fg=FONDO)

    if nombre == "Inicio":
        mostrar_inicio()
    else:
        mostrar_tema(nombre)


def crear_boton_menu(texto, simbolo):
    label = tk.Label(
        menu, text=f"  {simbolo}   {texto}",
        font=("Helvetica", 12, "bold"), bg=CIAN, fg=FONDO,
        anchor="w", padx=15, pady=14, cursor="hand2"
    )
    label.pack(fill="x", padx=12, pady=5)

    def entrar(evento):
        label.configure(bg=VIOLETA, fg=BLANCO)

    def salir(evento):
        if pantalla_activa == texto:
            label.configure(bg=VIOLETA, fg=BLANCO)
        else:
            label.configure(bg=CIAN, fg=FONDO)

    label.bind("<Enter>", entrar)
    label.bind("<Leave>", salir)
    label.bind("<Button-1>", lambda evento, nombre=texto: mostrar_pantalla(nombre))
    botones_menu[texto] = label


crear_boton_menu("Inicio", "⌂")
crear_boton_menu("Permutaciones", "P")
crear_boton_menu("Combinaciones", "C")
crear_boton_menu("División", "÷")
crear_boton_menu("MCD", "∴")
crear_boton_menu("Recursividad", "↻")

pie = tk.Frame(menu, bg=PANEL)
pie.pack(side="bottom", fill="x", padx=20, pady=22)

tk.Frame(pie, bg=BORDE, height=1).pack(fill="x", pady=(0, 12))
tk.Label(
    pie, text="PROYECTO FINAL", font=("Helvetica", 9, "bold"),
    bg=PANEL, fg=SECUNDARIO
).pack(anchor="w")
tk.Label(
    pie, text="Aprende · Calcula · Comprueba", font=("Helvetica", 9),
    bg=PANEL, fg=CIAN
).pack(anchor="w", pady=(5, 0))



# Componentes reutilizables
def crear_etiqueta(parent, texto, **kwargs):
    opciones = {
        "text": texto, "bg": kwargs.pop("bg", FONDO),
        "fg": kwargs.pop("fg", BLANCO),
        "font": kwargs.pop("font", ("Helvetica", 11))
    }
    opciones.update(kwargs)
    return tk.Label(parent, **opciones)


def crear_boton(parent, texto, comando, color=CIAN, ancho=None):
    opciones = {
        "text": texto, "command": comando,
        "font": ("Helvetica", 10, "bold"),
        "bg": color, "fg": FONDO if color == CIAN else BLANCO,
        "activebackground": VIOLETA, "activeforeground": BLANCO,
        "bd": 0, "relief": "flat", "cursor": "hand2",
        "padx": 16, "pady": 10
    }
    if ancho:
        opciones["width"] = ancho
    boton = tk.Button(parent, **opciones)
    boton.bind("<Enter>", lambda e: boton.configure(bg=VIOLETA, fg=BLANCO))
    boton.bind("<Leave>", lambda e: boton.configure(
        bg=color, fg=FONDO if color == CIAN else BLANCO
    ))
    return boton



# Inicio
def mostrar_inicio():
    encabezado = tk.Frame(contenido, bg=FONDO)
    encabezado.pack(fill="x", padx=35, pady=(35, 20))

    crear_etiqueta(
        encabezado, "BIENVENIDO A MATHLAB",
        font=("Helvetica", 10, "bold"), fg=CIAN
    ).pack(anchor="w")

    crear_etiqueta(
        encabezado, "Explora las matemáticas.",
        font=("Helvetica", 28, "bold")
    ).pack(anchor="w", pady=(10, 5))

    crear_etiqueta(
        encabezado, "Selecciona un tema para comenzar a resolver.",
        fg=SECUNDARIO, font=("Helvetica", 12)
    ).pack(anchor="w")

    area_tarjetas = tk.Frame(contenido, bg=FONDO)
    area_tarjetas.pack(fill="both", expand=True, padx=25, pady=10)

    temas = [
        ("Permutaciones", "P", "Calcula formas de ordenar.", CIAN),
        ("Combinaciones", "C", "Calcula formas de seleccionar.", VIOLETA),
        ("División", "÷", "Calcula cociente y residuo.", CIAN),
        ("MCD", "∴", "Encuentra el máximo común divisor.", CIAN),
        ("Recursividad", "↻", "Explora el factorial recursivo.", VIOLETA),
        
    ]

    for columna in range(2):
        area_tarjetas.columnconfigure(columna, weight=1)

    for indice, (nombre, simbolo, descripcion, color) in enumerate(temas):
        fila, columna = divmod(indice, 2)
        tarjeta = tk.Frame(
            area_tarjetas, bg=TARJETA,
            highlightbackground=BORDE, highlightthickness=1
        )
        tarjeta.grid(row=fila, column=columna, sticky="nsew", padx=10, pady=10)

        crear_etiqueta(
            tarjeta, simbolo, bg=TARJETA, fg=color,
            font=("Helvetica", 23, "bold")
        ).pack(anchor="w", padx=18, pady=(15, 5))

        crear_etiqueta(
            tarjeta, nombre, bg=TARJETA,
            font=("Helvetica", 15, "bold")
        ).pack(anchor="w", padx=18)

        crear_etiqueta(
            tarjeta, descripcion, bg=TARJETA, fg=SECUNDARIO,
            font=("Helvetica", 10), wraplength=300, justify="left"
        ).pack(anchor="w", padx=18, pady=(6, 12))

        crear_boton(
            tarjeta, "ABRIR TEMA  →",
            lambda t=nombre: mostrar_pantalla(t)
        ).pack(anchor="w", padx=18, pady=(0, 16))

        area_tarjetas.rowconfigure(fila, weight=1)

    area_tarjetas.columnconfigure(0, weight=1)
    area_tarjetas.columnconfigure(1, weight=1)


# Pantallas de calculo
DATOS_TEMAS = {
    "MCD": (
        "Máximo común divisor",
        "Encuentra el mayor divisor común de dos enteros.",
        "Ingresa dos números enteros."
    ),
    "División": (
        "Algoritmo de la división",
        "Comprueba la igualdad dividendo = divisor × cociente + residuo.",
        "Ingresa el dividendo y un divisor distinto de cero."
    ),
    "Recursividad": (
        "Factorial recursivo",
        "Observa cómo una función se llama a sí misma hasta llegar al caso base.",
        "Ingresa un entero no negativo."
    ),
    "Permutaciones": (
        "Permutaciones",
        "Calcula cuántas formas hay de ordenar r elementos elegidos entre n.",
        "Ingresa n y r, donde 0 ≤ r ≤ n."
    ),
    "Combinaciones": (
        "Combinaciones",
        "Calcula cuántas formas hay de seleccionar r elementos entre n cuando el orden no importa.",
        "Ingresa n y r, donde 0 ≤ r ≤ n."
    )
}


def mostrar_tema(nombre):
    titulo, descripcion, instruccion = DATOS_TEMAS[nombre]

    panel = tk.Frame(contenido, bg=FONDO)
    panel.pack(fill="both", expand=True, padx=40, pady=28)

    crear_etiqueta(
        panel, f"MATHLAB  /  {nombre.upper()}",
        font=("Helvetica", 10, "bold"), fg=CIAN
    ).pack(anchor="w")

    crear_etiqueta(
        panel, titulo, font=("Helvetica", 27, "bold")
    ).pack(anchor="w", pady=(12, 7))

    crear_etiqueta(
        panel, descripcion, fg=SECUNDARIO, font=("Helvetica", 11),
        wraplength=760, justify="left"
    ).pack(anchor="w")

    tarjeta = tk.Frame(
        panel, bg=TARJETA,
        highlightbackground=BORDE, highlightthickness=1
    )
    tarjeta.pack(fill="x", pady=(22, 14))

    crear_etiqueta(
        tarjeta, "ÁREA DE TRABAJO",
        bg=TARJETA, fg=CIAN, font=("Helvetica", 10, "bold")
    ).pack(anchor="w", padx=22, pady=(18, 5))

    crear_etiqueta(
        tarjeta, instruccion, bg=TARJETA, fg=BLANCO,
        font=("Helvetica", 10)
    ).pack(anchor="w", padx=22, pady=(0, 12))

    campos = tk.Frame(tarjeta, bg=TARJETA)
    campos.pack(fill="x", padx=22, pady=(0, 18))

    resultado_frame = tk.Frame(
        panel, bg=PANEL, highlightbackground=BORDE, highlightthickness=1
    )
    resultado_frame.pack(fill="both", expand=True, pady=(0, 10))

    crear_etiqueta(
        resultado_frame, "RESULTADO",
        bg=PANEL, fg=VIOLETA, font=("Helvetica", 10, "bold")
    ).pack(anchor="w", padx=20, pady=(15, 5))

    resultado_texto = tk.Text(
        resultado_frame, height=7, wrap="word",
        bg=PANEL, fg=BLANCO, insertbackground=BLANCO,
        font=("Helvetica", 11), bd=0, relief="flat",
        padx=2, pady=2
    )
    resultado_texto.pack(fill="both", expand=True, padx=20, pady=(0, 15))
    resultado_texto.insert("1.0", "Aquí aparecerán el procedimiento y el resultado.")
    resultado_texto.configure(state="disabled")

    entradas = {}

    if nombre in ("MCD", "División"):
        etiquetas = (
            [("a", "Primer número"), ("b", "Segundo número")]
            if nombre == "MCD"
            else [("a", "Dividendo"), ("b", "Divisor")]
        )
    elif nombre == "Recursividad":
        etiquetas = [("n", "Número (n)")]
    else:
        etiquetas = [("n", "Total de elementos (n)"), ("r", "Elementos elegidos (r)")]

    for indice, (clave, etiqueta) in enumerate(etiquetas):
        columna = tk.Frame(campos, bg=TARJETA)
        columna.grid(row=0, column=indice, sticky="ew", padx=(0 if indice == 0 else 14, 14))
        campos.columnconfigure(indice, weight=1)

        crear_etiqueta(
            columna, etiqueta, bg=TARJETA, fg=BLANCO,
            font=("Helvetica", 10, "bold")
        ).pack(anchor="w", pady=(0, 6))

        entrada = tk.Entry(
            columna, font=("Helvetica", 13), bg=FONDO,
            fg=BLANCO, insertbackground=BLANCO,
            relief="flat", bd=0
        )
        entrada.pack(fill="x", ipady=10)
        entradas[clave] = entrada

    def poner_resultado(texto, error=False):
        resultado_texto.configure(state="normal")
        resultado_texto.delete("1.0", "end")
        resultado_texto.insert("1.0", texto)
        resultado_texto.configure(
            state="disabled",
            fg="#FF8B9A" if error else BLANCO
        )

    def leer_entero(clave, nombre_campo):
        valor = entradas[clave].get().strip()
        if not valor:
            raise ValueError(f"Escribe el valor de «{nombre_campo}».")
        try:
            return int(valor)
        except ValueError:
            raise ValueError(f"«{nombre_campo}» debe ser un número entero.")

    def calcular():
        try:
            if nombre == "MCD":
                a = leer_entero("a", "Primer número")
                b = leer_entero("b", "Segundo número")
                if a == 0 and b == 0:
                    raise ValueError("El MCD de 0 y 0 no está definido.")
                r = calcular_mcd(a, b)
                texto = (
                    f"MCD({a}, {b}) = {r}\n\n"
                    "El máximo común divisor es el mayor entero positivo "
                    "que divide exactamente a ambos números."
                )

            elif nombre == "División":
                a = leer_entero("a", "Dividendo")
                b = leer_entero("b", "Divisor")

                if b == 0:
                    raise ValueError("El divisor no puede ser cero.")

                q, r = calcular_division(a, b)

                texto = (
                    f"Dividendo: {a}\nDivisor: {b}\n\n"
                    f"Cociente: {q}\nResiduo: {r}\n\n"
                    f"Comprobación: {a} = ({b} × {q}) + {r}\n"
                    f"{a} = {b * q + r}\n"
                    f"Condición: 0 ≤ residuo < |divisor| → "
                    f"0 ≤ {r} < {abs(b)}"
    )

           
            elif nombre == "Recursividad":
                n = leer_entero("n", "Número")

                if n < 0:
                    raise ValueError(
                        "El factorial solo se calcula para enteros no negativos."
                    )

                texto = obtener_pasos_recursivos(n)


            
            elif nombre == "Permutaciones":
                n = leer_entero("n", "Total de elementos (n)")
                r = leer_entero("r", "Elementos elegidos (r)")

                valor = permutaciones(n, r)

                texto = (
                    "Fórmula: P(n,r) = n! / (n-r)!\n\n"
                    f"P({n},{r}) = {n}! / ({n}-{r})!\n"
                    f"P({n},{r}) = {factorial_permutaciones(n)} / "
                    f"{factorial_permutaciones(n-r)}\n\n"
                    f"Resultado: {valor}"
    )

            
            else:  # Combinaciones
                n = leer_entero("n", "Total de elementos (n)")
                r = leer_entero("r", "Elementos elegidos (r)")

                valor = combinaciones(n, r)

                texto = (
                    "Fórmula: C(n,r) = n! / (r!(n-r)!)\n\n"
                    f"C({n},{r}) = {n}! / ({r}! × ({n}-{r})!)\n"
                    f"C({n},{r}) = {factorial_combinaciones(n)} / "
                    f"({factorial_combinaciones(r)} × "
                    f"{factorial_combinaciones(n-r)})\n\n"
                    f"Resultado: {valor}"
    )


            poner_resultado(texto)

        except ValueError as error:
            poner_resultado(str(error), error=True)

    def limpiar():
        for entrada in entradas.values():
            entrada.delete(0, "end")
        poner_resultado("Aquí aparecerán el procedimiento y el resultado.")
        if entradas:
            next(iter(entradas.values())).focus_set()


    botones = tk.Frame(panel, bg=FONDO)
    botones.pack(anchor="w", pady=(0, 5))

    # Calcular
    lbl_calcular = tk.Label(
        botones,
        text="CALCULAR  →",
        font=("Helvetica", 10, "bold"),
        bg=CIAN,
        fg=FONDO,
        cursor="hand2",
        padx=16,
        pady=10
    )
    lbl_calcular.pack(side="left", padx=(0, 10))
    lbl_calcular.bind("<Button-1>", lambda evento: calcular())

    # Limpiar
    lbl_limpiar = tk.Label(
        botones,
        text="LIMPIAR",
        font=("Helvetica", 10, "bold"),
        bg=VIOLETA,
        fg=BLANCO,
        cursor="hand2",
        padx=16,
        pady=10
    )
    lbl_limpiar.pack(side="left")
    lbl_limpiar.bind("<Button-1>", lambda evento: limpiar())


    if entradas:
        next(iter(entradas.values())).focus_set()



# Iniciar
mostrar_pantalla("Inicio")
ventana.mainloop()
