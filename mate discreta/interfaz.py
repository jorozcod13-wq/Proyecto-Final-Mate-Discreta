
import tkinter as tk
from tkinter import ttk
# Requires Pillow:  pip install pillow
from PIL import Image, ImageTk


THEME_BG = "#0b1020"
THEME_FG = "#18181b"
THEME_ACCENT = "#52525b"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#eaf2ff"
THEME_FONT = ("Courier New", 10)


def apply_theme(root):
    """Apply the project theme as defaults; per-widget options override these."""
    root.configure(bg=THEME_BG)
    root.option_add("*background", THEME_BG)
    root.option_add("*foreground", THEME_FG)
    root.option_add("*font", THEME_FONT)
    root.option_add("*Entry.background", THEME_FIELD_BG)
    root.option_add("*Text.background", THEME_FIELD_BG)
    root.option_add("*Listbox.background", THEME_FIELD_BG)
    root.option_add("*Button.background", THEME_ACCENT)
    root.option_add("*Button.foreground", THEME_ACCENT_FG)
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    style.configure(".", background=THEME_BG, foreground=THEME_FG, fieldbackground=THEME_FIELD_BG, font=THEME_FONT)


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("1200x770")
        apply_theme(root)

        self.frame3 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.frame3.place(x=0, y=0, width=240, height=770)

        # Kept on self, or Python garbage-collects it and the image goes blank.
        self.image1_image = ImageTk.PhotoImage(Image.open("image.png").resize((190, 90)))
        self.image1 = tk.Label(self.frame3, image=self.image1_image)
        self.image1.place(x=20, y=20, width=190, height=90)

        self.Inicio = tk.Label(self.frame3, text="⌂ Inicio", bg="#27DFFF")
        self.Inicio.place(x=30, y=200, width=180, height=55)

        self.label2 = tk.Label(self.frame3, text="Combinaciones", bg="#27DFFF")
        self.label2.place(x=30, y=280, width=180, height=55)

        self.label3 = tk.Label(self.frame3, text="Permutaciones", bg="#27DFFF")
        self.label3.place(x=30, y=360, width=180, height=55)

        self.label4 = tk.Label(self.frame3, text="MCD", bg="#27DFFF")
        self.label4.place(x=30, y=440, width=180, height=55)

        self.label5 = tk.Label(self.frame3, text="División", bg="#27DFFF")
        self.label5.place(x=30, y=520, width=180, height=55)

        self.label6 = tk.Label(self.frame3, text="Recursividad", bg="#27DFFF")
        self.label6.place(x=30, y=600, width=180, height=55)

        self.label7 = tk.Label(self.frame3, text="Proyecto Final", fg="#EAF2FF", font=("Helvetica", 10))
        self.label7.place(x=10, y=690, width=220, height=30)

        self.label8 = tk.Label(self.frame3, text="Aprende·Calcula·Comprueba", fg="#27DFFF")
        self.label8.place(x=20, y=720, width=200, height=30)

        self.label9 = tk.Label(self.frame3, text=" Matemática Discreta", fg="#EAF2FF", font=("Helvetica", 12))
        self.label9.place(x=10, y=120, width=220, height=30)

        self.tarjeta1 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.tarjeta1.place(x=280, y=170, width=410, height=170)

        self.tarjeta2 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.tarjeta2.place(x=730, y=170, width=410, height=170)

        self.label10 = tk.Label(root, text="Bienvenido a MATHLAB", fg="#27DFFF", font=("Helvetica", 25, "bold italic"))
        self.label10.place(x=290, y=0, width=410, height=80)

        self.label11 = tk.Label(root, text="Explora las Matemáticas", fg="#EAF2FF", font=("Helvetica", 25, "bold"))
        self.label11.place(x=290, y=50, width=470, height=60)

        self.label12 = tk.Label(root, text="Selecciona un tema para comenzar a resolver", fg="#8FA3BF", font=("Helvetica", 15))
        self.label12.place(x=290, y=100, width=520, height=60)

        self.tarjeta3 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.tarjeta3.place(x=280, y=370, width=410, height=170)

        self.tarjeta5 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.tarjeta5.place(x=280, y=570, width=410, height=170)

        self.tarjeta4 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.tarjeta4.place(x=730, y=370, width=410, height=170)

        self.tarjeta6 = tk.Frame(root, bg="#14213A", relief="groove", bd=2)
        self.tarjeta6.place(x=730, y=570, width=410, height=170)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
