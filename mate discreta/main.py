#Esta versión corresponde a la interfaz gráfica definitiva del proyecto MathLab.
#Con todos los cambios ya realizados, el diseño ya establecido
#Se organizaron los resultados para mostrar los procedimientos matemáticos de forma clara y ordenada.
#Funciones trabajando correctamente
#Se integraron los módulos de MCD, división, permutaciones,
#combinaciones y recursividad con la interfaz gráfica.



import tkinter as tk
import math

from modulos.mcd import calcular_mcd_pasos
from modulos.division import calcular_division
from modulos.permutacion import permutaciones, factorial_permutaciones
from modulos.combinacion import combinaciones, factorial_combinaciones
from modulos.recursividad import obtener_pasos_recursivos

#Paleta de Colores---
FONDO = "#0B1020"
PANEL = "#14213A"
TARJETA = "#1B2B48"
CIAN = "#27DFFF"
VIOLETA = "#8B7CFF"
BLANCO = "#EAF2FF"
SECUNDARIO = "#8FA3BF"
BORDE = "#30415F"
ERROR = "#FF8B9A"

#Ventana principal----
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

botones_menu = {}
pantalla_activa = "Inicio"

#Componentes reutilizables----
def crear_etiqueta(parent, texto, **kwargs):
    opciones = {
        "text": texto,
        "bg": kwargs.pop("bg", FONDO),
        "fg": kwargs.pop("fg", BLANCO),
        "font": kwargs.pop("font", ("Helvetica", 11)),
    }
    opciones.update(kwargs)
    return tk.Label(parent, **opciones)


def crear_boton(parent, texto, comando, color=CIAN, ancho=None):
    opciones = {
        "text": texto,
        "command": comando,
        "font": ("Helvetica", 10, "bold"),
        "bg": color,
        "fg": FONDO if color == CIAN else BLANCO,
        "activebackground": VIOLETA,
        "activeforeground": BLANCO,
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2",
        "padx": 16,
        "pady": 10,
    }
    if ancho:
        opciones["width"] = ancho
    boton = tk.Button(parent, **opciones)
    boton.bind("<Enter>", lambda evento: boton.configure(bg=VIOLETA, fg=BLANCO))
    boton.bind(
        "<Leave>",
        lambda evento: boton.configure(bg=color, fg=FONDO if color == CIAN else BLANCO),
    )
    return boton

#Funcion para mostrar los resultados-----
def configurar_estilos_resultado(widget):
    widget.tag_configure(
        "titulo", font=("Helvetica", 15, "bold"), foreground=CIAN,
        justify="center", spacing3=10
    )
    widget.tag_configure(
        "subtitulo", font=("Helvetica", 11, "bold"), foreground=VIOLETA,
        spacing1=8, spacing3=5
    )
    widget.tag_configure(
        "resultado", font=("Helvetica", 14, "bold"), foreground=CIAN,
        justify="center", spacing1=8, spacing3=8
    )
    widget.tag_configure(
        "error", font=("Helvetica", 11, "bold"), foreground=ERROR, spacing1=5
    )


def poner_resultado(widget, texto, error=False):
    widget.configure(state="normal")
    widget.delete("1.0", "end")
    configurar_estilos_resultado(widget)
    if error:
        widget.insert("end", "NO SE PUDO REALIZAR EL CÁLCULO\n\n", "error")
        widget.insert("end", texto, "error")
    else:
        widget.insert("end", texto)
    widget.configure(state="disabled")


def poner_resultado_mcd(widget, resultado_mcd, pasos, a, b):
    widget.configure(state="normal")
    widget.delete("1.0", "end")
    configurar_estilos_resultado(widget)
    widget.insert("end", "MÁXIMO COMÚN DIVISOR\n\n", "titulo")
    widget.insert("end", f"Calcularemos el MCD de {a} y {b}.\n\n")
    widget.insert("end", "ALGORITMO DE EUCLIDES\n", "subtitulo")
    widget.insert("end", "Dividendo = divisor × cociente + residuo\n\n")
    widget.insert("end", str(pasos) + "\n\n")
    widget.insert("end", "INTERPRETACIÓN\n", "subtitulo")
    widget.insert("end", f"El mayor divisor común de {a} y {b} es {resultado_mcd}.\n\n")
    widget.insert("end", "RESULTADO FINAL\n", "subtitulo")
    widget.insert("end", f"MCD({a}, {b}) = {resultado_mcd}", "resultado")
    widget.configure(state="disabled")


def poner_resultado_tema(widget, titulo, introduccion, secciones):
    widget.configure(state="normal")
    widget.delete("1.0", "end")
    configurar_estilos_resultado(widget)
    widget.insert("end", titulo.upper() + "\n\n", "titulo")
    if introduccion:
        widget.insert("end", introduccion + "\n\n")
    for encabezado, texto in secciones:
        widget.insert("end", encabezado.upper() + "\n", "subtitulo")
        etiqueta = "resultado" if encabezado.lower() == "resultado final" else None
        widget.insert("end", texto + "\n\n", etiqueta) if etiqueta else widget.insert("end", texto + "\n\n")
    widget.configure(state="disabled")

#El menú lateral
def mostrar_pantalla(nombre):
    global pantalla_activa
    pantalla_activa = nombre
    for widget in contenido.winfo_children():
        widget.destroy()
    for titulo_menu, label in botones_menu.items():
        if titulo_menu == nombre:
            label.configure(bg=VIOLETA, fg=BLANCO)
        else:
            label.configure(bg=CIAN, fg=FONDO)
    if nombre == "Inicio":
        mostrar_inicio()
    else:
        mostrar_tema(nombre)


def crear_boton_menu(texto, simbolo):
    label = tk.Label(
        menu, text=f"  {simbolo}   {texto}", font=("Helvetica", 12, "bold"),
        bg=CIAN, fg=FONDO, anchor="w", padx=15, pady=14, cursor="hand2"
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


logo = tk.Label(menu, text="∑  MATHLAB", font=("Helvetica", 23, "bold"), bg=PANEL, fg=CIAN)
logo.pack(pady=(32, 5))
tk.Label(menu, text="MATEMÁTICA DISCRETA", font=("Helvetica", 9), bg=PANEL, fg=SECUNDARIO).pack(pady=(0, 30))
tk.Frame(menu, bg=BORDE, height=1).pack(fill="x", padx=20, pady=(0, 20))

crear_boton_menu("Inicio", "⌂")
crear_boton_menu("Permutaciones", "P")
crear_boton_menu("Combinaciones", "C")
crear_boton_menu("División", "÷")
crear_boton_menu("MCD", "∴")
crear_boton_menu("Recursividad", "↻")

pie = tk.Frame(menu, bg=PANEL)
pie.pack(side="bottom", fill="x", padx=20, pady=22)
tk.Frame(pie, bg=BORDE, height=1).pack(fill="x", pady=(0, 12))
tk.Label(pie, text="PROYECTO FINAL", font=("Helvetica", 9, "bold"), bg=PANEL, fg=SECUNDARIO).pack(anchor="w")
tk.Label(pie, text="Aprende · Calcula · Comprueba", font=("Helvetica", 9), bg=PANEL, fg=CIAN).pack(anchor="w", pady=(5, 0))


#Parte principal con las tarjetas
def mostrar_inicio():
    encabezado = tk.Frame(contenido, bg=FONDO)
    encabezado.pack(fill="x", padx=35, pady=(35, 20))
    crear_etiqueta(encabezado, "BIENVENIDO A MATHLAB", font=("Helvetica", 10, "bold"), fg=CIAN).pack(anchor="w")
    crear_etiqueta(encabezado, "Explora las matemáticas.", font=("Helvetica", 28, "bold")).pack(anchor="w", pady=(10, 5))
    crear_etiqueta(encabezado, "Selecciona un tema para comenzar a resolver.", fg=SECUNDARIO, font=("Helvetica", 12)).pack(anchor="w")

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
        tarjeta = tk.Frame(area_tarjetas, bg=TARJETA, highlightbackground=BORDE, highlightthickness=1)
        tarjeta.grid(row=fila, column=columna, sticky="nsew", padx=10, pady=10)
        crear_etiqueta(tarjeta, simbolo, bg=TARJETA, fg=color, font=("Helvetica", 23, "bold")).pack(anchor="w", padx=18, pady=(15, 5))
        crear_etiqueta(tarjeta, nombre, bg=TARJETA, font=("Helvetica", 15, "bold")).pack(anchor="w", padx=18)
        crear_etiqueta(tarjeta, descripcion, bg=TARJETA, fg=SECUNDARIO, font=("Helvetica", 10), wraplength=300, justify="left").pack(anchor="w", padx=18, pady=(6, 12))
        crear_boton(tarjeta, "ABRIR TEMA  →", lambda t=nombre: mostrar_pantalla(t)).pack(anchor="w", padx=18, pady=(0, 16))
        area_tarjetas.rowconfigure(fila, weight=1)

#Información de cada tema
DATOS_TEMAS = {
    "MCD": ("Máximo común divisor", "Encuentra el mayor divisor común de dos enteros.", "Ingresa dos números enteros."),
    "División": ("Algoritmo de la división", "Comprueba la igualdad dividendo = divisor × cociente + residuo.", "Ingresa el dividendo y un divisor distinto de cero."),
    "Recursividad": ("Factorial recursivo", "Observa cómo una función se llama a sí misma hasta llegar al caso base.", "Ingresa un entero no negativo."),
    "Permutaciones": ("Permutaciones", "Calcula cuántas formas hay de ordenar r elementos elegidos entre n.", "Ingresa n y r, donde 0 ≤ r ≤ n."),
    "Combinaciones": ("Combinaciones", "Calcula cuántas formas hay de seleccionar r elementos entre n cuando el orden no importa.", "Ingresa n y r, donde 0 ≤ r ≤ n."),
}

#Parte de calculos de todo los temas
def mostrar_tema(nombre):
    titulo, descripcion, instruccion = DATOS_TEMAS[nombre]
    panel = tk.Frame(contenido, bg=FONDO)
    panel.pack(fill="both", expand=True, padx=40, pady=28)
    crear_etiqueta(panel, f"MATHLAB  /  {nombre.upper()}", font=("Helvetica", 10, "bold"), fg=CIAN).pack(anchor="w")
    crear_etiqueta(panel, titulo, font=("Helvetica", 27, "bold")).pack(anchor="w", pady=(12, 7))
    crear_etiqueta(panel, descripcion, fg=SECUNDARIO, font=("Helvetica", 11), wraplength=760, justify="left").pack(anchor="w")

    tarjeta = tk.Frame(panel, bg=TARJETA, highlightbackground=BORDE, highlightthickness=1)
    tarjeta.pack(fill="x", pady=(22, 14))
    crear_etiqueta(tarjeta, "ÁREA DE TRABAJO", bg=TARJETA, fg=CIAN, font=("Helvetica", 10, "bold")).pack(anchor="w", padx=22, pady=(18, 5))
    crear_etiqueta(tarjeta, instruccion, bg=TARJETA, fg=BLANCO, font=("Helvetica", 10)).pack(anchor="w", padx=22, pady=(0, 12))
    campos = tk.Frame(tarjeta, bg=TARJETA)
    campos.pack(fill="x", padx=22, pady=(0, 18))

    resultado_frame = tk.Frame(panel, bg=PANEL, highlightbackground=BORDE, highlightthickness=1)
    resultado_frame.pack(fill="both", expand=True, pady=(0, 10))
    crear_etiqueta(resultado_frame, "RESULTADO", bg=PANEL, fg=VIOLETA, font=("Helvetica", 10, "bold")).pack(anchor="w", padx=20, pady=(15, 5))
    zona_texto = tk.Frame(resultado_frame, bg=PANEL)
    zona_texto.pack(fill="both", expand=True, padx=20, pady=(0, 15))
    resultado_texto = tk.Text(zona_texto, height=7, wrap="word", bg=PANEL, fg=BLANCO, insertbackground=BLANCO, font=("Helvetica", 11), bd=0, relief="flat", padx=5, pady=5)
    barra = tk.Scrollbar(zona_texto, orient="vertical", command=resultado_texto.yview)
    resultado_texto.configure(yscrollcommand=barra.set)
    barra.pack(side="right", fill="y")
    resultado_texto.pack(side="left", fill="both", expand=True)
    poner_resultado(resultado_texto, "Aquí aparecerán el procedimiento y el resultado.")

    entradas = {}
    if nombre == "MCD":
        etiquetas = [("a", "Primer número"), ("b", "Segundo número")]
    elif nombre == "División":
        etiquetas = [("a", "Dividendo"), ("b", "Divisor")]
    elif nombre == "Recursividad":
        etiquetas = [("n", "Número (n)")]
    else:
        etiquetas = [("n", "Total de elementos (n)"), ("r", "Elementos elegidos (r)")]

    for indice, (clave, etiqueta) in enumerate(etiquetas):
        columna = tk.Frame(campos, bg=TARJETA)
        columna.grid(row=0, column=indice, sticky="ew", padx=(0, 14))
        campos.columnconfigure(indice, weight=1)
        crear_etiqueta(columna, etiqueta, bg=TARJETA, fg=BLANCO, font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 6))
        entrada = tk.Entry(columna, font=("Helvetica", 13), bg=FONDO, fg=BLANCO, insertbackground=BLANCO, relief="flat", bd=0)
        entrada.pack(fill="x", ipady=10)
        entradas[clave] = entrada

    def leer_entero(clave, nombre_campo):
        valor = entradas[clave].get().strip()
        if not valor:
            raise ValueError(f"Escribe el valor de «{nombre_campo}».")
        try:
            return int(valor)
        except ValueError:
            raise ValueError(f"«{nombre_campo}» debe ser un número entero.")

#Funcion para calcular los datos que se ingresan, dependiendo que tema escogio el usuario
    def calcular():
        try:
#MCD y algoritmo de euclides 
            if nombre == "MCD":
                a = leer_entero("a", "Primer número")
                b = leer_entero("b", "Segundo número")
                resultado_mcd, pasos = calcular_mcd_pasos(a, b)
                poner_resultado_mcd(resultado_texto, resultado_mcd, pasos, a, b)
                return
#Algoritmo de la división
            if nombre == "División":
                a = leer_entero("a", "Dividendo")
                b = leer_entero("b", "Divisor")
                if b == 0:
                    raise ValueError("El divisor no puede ser cero.")
                q, r = calcular_division(a, b)
                poner_resultado_tema(resultado_texto, "Algoritmo de la división", f"Dividiremos {a} entre {b} y comprobaremos que se cumple el algoritmo de la división.", [
                    ("Datos", f"Dividendo: {a}\nDivisor: {b}"),
                    ("Cociente y residuo", f"Cociente = {q}\nResiduo = {r}"),
                    ("Comprobación", f"Dividendo = divisor × cociente + residuo\n{a} = ({b} × {q}) + {r}\n{a} = {b * q + r}"),
                    ("Condición del residuo", f"0 ≤ {r} < {abs(b)}"),
                    ("Resultado final", f"Cociente = {q}  |  Residuo = {r}"),
                ])
                return
#Recursividad
            if nombre == "Recursividad":
                n = leer_entero("n", "Número")
                if n < 0:
                    raise ValueError("El factorial solo se calcula para enteros no negativos.")
                texto = obtener_pasos_recursivos(n)
                poner_resultado_tema(resultado_texto, "Factorial recursivo", f"Calcularemos el factorial de {n} mediante llamadas recursivas.", [
                    ("Procedimiento recursivo", str(texto)),
                    ("Interpretación", "La función se llama a sí misma hasta alcanzar un caso base."),
                    ("Resultado final", f"{n}! = {math.factorial(n)}"),
                ])
                return
#Permutaciones
            if nombre == "Permutaciones":
                n = leer_entero("n", "Total de elementos (n)")
                r = leer_entero("r", "Elementos elegidos (r)")
                valor = permutaciones(n, r)
                factorial_n = factorial_permutaciones(n)
                factorial_restante = factorial_permutaciones(n - r)
                poner_resultado_tema(resultado_texto, "Permutaciones", f"Calcularemos las formas de ordenar {r} elementos elegidos de un grupo de {n}.", [
                    ("Fórmula", "P(n, r) = n! / (n - r)!"),
                    ("Sustitución", f"P({n}, {r}) = {n}! / ({n} - {r})!"),
                    ("Desarrollo", f"P({n}, {r}) = {factorial_n} / {factorial_restante}"),
                    ("Interpretación", f"Existen {valor} formas diferentes de elegir y ordenar {r} elementos de un grupo de {n}."),
                    ("Resultado final", f"P({n}, {r}) = {valor}"),
                ])
                return
#Combinaciones
            if nombre == "Combinaciones":
                n = leer_entero("n", "Total de elementos (n)")
                r = leer_entero("r", "Elementos elegidos (r)")
                valor = combinaciones(n, r)
                factorial_n = factorial_combinaciones(n)
                factorial_r = factorial_combinaciones(r)
                factorial_restante = factorial_combinaciones(n - r)
                poner_resultado_tema(resultado_texto, "Combinaciones", f"Calcularemos las formas de seleccionar {r} elementos de un grupo de {n}, sin importar el orden.", [
                    ("Fórmula", "C(n, r) = n! / (r! × (n - r)!)"),
                    ("Sustitución", f"C({n}, {r}) = {n}! / ({r}! × ({n} - {r})!)"),
                    ("Desarrollo", f"C({n}, {r}) = {factorial_n} / ({factorial_r} × {factorial_restante})"),
                    ("Interpretación", f"Existen {valor} formas de seleccionar {r} elementos de un grupo de {n}, sin considerar el orden."),
                    ("Resultado final", f"C({n}, {r}) = {valor}"),
                ])
                return
        except ValueError as error:
            poner_resultado(resultado_texto, str(error), error=True)
        except Exception as error:
            poner_resultado(resultado_texto, f"Ocurrió un error inesperado: {error}", error=True)


#Boton para limpiar las casillas y borrar los resultados anteriores
    def limpiar():
        for entrada in entradas.values():
            entrada.delete(0, "end")
        poner_resultado(resultado_texto, "Aquí aparecerán el procedimiento y el resultado.")
        if entradas:
            next(iter(entradas.values())).focus_set()

#Diseño para los botones calcular y limpiar
    botones = tk.Frame(panel, bg=FONDO)
    botones.pack(anchor="w", pady=(0, 5))
    lbl_calcular = tk.Label(botones, text="CALCULAR  →", font=("Helvetica", 10, "bold"), bg=CIAN, fg=FONDO, cursor="hand2", padx=16, pady=10)
    lbl_calcular.pack(side="left", padx=(0, 10))
    lbl_calcular.bind("<Button-1>", lambda evento: calcular())
    lbl_calcular.bind("<Enter>", lambda evento: lbl_calcular.configure(bg=VIOLETA, fg=BLANCO))
    lbl_calcular.bind("<Leave>", lambda evento: lbl_calcular.configure(bg=CIAN, fg=FONDO))
    lbl_limpiar = tk.Label(botones, text="LIMPIAR", font=("Helvetica", 10, "bold"), bg=VIOLETA, fg=BLANCO, cursor="hand2", padx=16, pady=10)
    lbl_limpiar.pack(side="left")
    lbl_limpiar.bind("<Button-1>", lambda evento: limpiar())
    lbl_limpiar.bind("<Enter>", lambda evento: lbl_limpiar.configure(bg=CIAN, fg=FONDO))
    lbl_limpiar.bind("<Leave>", lambda evento: lbl_limpiar.configure(bg=VIOLETA, fg=BLANCO))
    if entradas:
        next(iter(entradas.values())).focus_set()

#Iniciar el programa
mostrar_pantalla("Inicio")
ventana.mainloop()
