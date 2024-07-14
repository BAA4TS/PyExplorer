import tkinter as tk

import ttkbootstrap as ttk
from src.core.Cargador import Cargador


class Config:
    def __init__(self, visualizador, argumento_visualizador):
        self.argumento_visualizador = argumento_visualizador
        self.visualizador = visualizador

        self.lista_temas = [
            "superhero",
            "united",
            "cosmo",
            "solar",
            "pulse",
            "darkly",
            "journal",
            "lumen",
            "minty",
            "vapor",
        ]

        # Instancia del Cargador para manejar la configuración
        self.core = Cargador()

        # Obtener y establecer tema actual
        self.tema_actual = self.core.obtener("Tema")
        self.core.establecer_tema(self.tema_actual)

    def view(self, home):
        """
        Configura y muestra la interfaz de usuario principal.

        Args:
            home (tk.Tk): Ventana principal de la aplicación.
        """
        # Frame superior que contiene los botones y el combobox
        contenedor = ttk.Frame(home)
        contenedor.pack(fill="x", padx=10, pady=10)

        # Configurar grid para centrado
        for i in range(5):
            contenedor.columnconfigure(i, weight=1)

        # Botón Volver
        boton_volver = ttk.Button(
            contenedor, text="Volver", command=self.volver
        )
        boton_volver.grid(row=0, column=0)

        # Texto de Tema
        texto_tema = ttk.Label(contenedor, text="Tema: ", font=(10))
        texto_tema.grid(row=0, column=1)

        # Selector Tema
        self.combo_box_selector = ttk.Combobox(
            contenedor, values=self.lista_temas
        )
        self.combo_box_selector.grid(row=0, column=2)
        self.combo_box_selector.set(
            self.tema_actual
        )  # Establecer el tema actual en el combobox

        # Botón Guardar
        boton_guardar = ttk.Button(
            contenedor,
            text="Guardar",
            command=self.guardar_configuracion,
        )
        boton_guardar.grid(row=0, column=3)

        # Separador
        separador = ttk.Separator(contenedor, style="secondary")
        separador.grid(
            row=2, column=0, columnspan=5, sticky="we", pady=10
        )

        # Información de manejo
        titulo = ttk.Label(contenedor, text="Información")
        titulo.grid(row=3, column=0)

        # TextBox para las clasificaciones
        clasificaciones_text_box = tk.Text(
            home, wrap="word", height=5, width=50
        )
        clasificaciones_text_box.pack(fill="both", expand=True)

        # Añadir texto de las clasificaciones al TextBox
        clasificaciones = (
            " - - Clasificacion - - \n"
            "(Win) Archivos de Windows [.DAT, .LOG1, .LOG2,.LOG3, etc]\n"
            "(A) Archivos [exe, png, jpg, etc]\n\n"
            "(C) Carpetas\n"
            "\n"
            " - - Boton crear - - \n"
            "- Las entradas de a continuacion el PATH \n"
            "-> Para crear una carpeta: $NombreCarpeta\n"
            "-> Para crear un archivo: &Archivo.txt\n"
        )
        clasificaciones_text_box.insert("1.0", clasificaciones)
        clasificaciones_text_box.config(
            state="disabled"
        )  # Hacer que el TextBox sea de solo lectura

    def volver(self):
        """
        Función para manejar el evento del botón Volver.
        """
        self.visualizador(self.argumento_visualizador)

    def guardar_configuracion(self):
        """
        Función para manejar el evento del botón Guardar.
        """
        tema_seleccionado = self.combo_box_selector.get()
        self.core.establecer_tema(tema_seleccionado)
        self.core.modificar("Tema", tema_seleccionado)
