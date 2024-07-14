import tkinter as tk

import ttkbootstrap as ttk
from src.core.Cargador import Cargador


class Home:
    def __init__(self, Visualisador, ArgumentoVisualizador):
        """
        Constructor de la clase Home.
        """
        self.Visualisador = Visualisador
        self.ArgumentoVisualizador = ArgumentoVisualizador
        # Instancia al Core
        self.Core = Cargador()
        self.PATH_VAR = tk.StringVar()
        self.PATH_UPDATE()

    """
    Funciones Principales de los Botones
    """

    def PATH_UPDATE(self):
        self.PATH_VAR.set(self.Core.obtener("PATH"))

    def Retroceder(self):
        """
        Función para manejar la acción de retroceder.
        """
        self.Core.retroceder(self.contenedor_visual)
        self.PATH_UPDATE()

    def Avanzar(self, event=None):
        """
        Función para manejar la acción de avanzar.
        """
        ItemSeleccionado = self.contenedor_visual.selection()
        if ItemSeleccionado:
            ID = ItemSeleccionado[0]
            valores = self.contenedor_visual.item(ID, "values")
            if valores:
                Nombre = valores[
                    0
                ]  # El nombre se encuentra en la primera columna ('Nombre')
                Clasificacion = valores[1]
                if Clasificacion == "C":
                    self.Core.avanzar(Nombre, self.contenedor_visual)
                    self.PATH_UPDATE()

    def Borrar(self):
        """
        Función para manejar la acción de borrar.
        """
        ItemSeleccionado = self.contenedor_visual.selection()
        if ItemSeleccionado:
            ID = ItemSeleccionado[0]
            valores = self.contenedor_visual.item(ID, "values")
            if valores:
                Clasificacion = valores[1]
                if Clasificacion == "C":
                    self.Core.borrar(
                        valores[0], True, self.contenedor_visual
                    )
                    self.PATH_UPDATE()
                else:
                    self.Core.borrar(
                        valores[0] + valores[2],
                        False,
                        self.contenedor_visual,
                    )

    def Nuevo(self):
        """
        Función para manejar la acción de nuevo.
        """
        Nombre = self.PATH_VAR.get()
        self.Core.crear(Nombre, self.contenedor_visual)

    def Recargar(self):
        """
        Función para manejar la acción de recargar.
        """
        self.Core.insertar_datos(self.contenedor_visual)

    def Configuracion(self):
        """
        Función para manejar la acción de configuración.
        """
        self.Visualisador(self.ArgumentoVisualizador)

    def View(self, home):
        """
        Configura y muestra la interfaz de usuario principal.

        Args:
            home (tk.Tk): Ventana principal de la aplicación.
        """
        # Frame superior que contiene los botones y entry
        contenedor = ttk.Frame(home)
        contenedor.pack(fill="x", padx=10, pady=10)

        # Configurar grid para centrado
        for i in range(5):
            contenedor.columnconfigure(i, weight=1)

        # Botón para retroceder
        boton_retroceder = ttk.Button(
            contenedor, text="<", command=self.Retroceder
        )
        boton_retroceder.grid(
            row=0, column=0, sticky="we", padx=5, pady=5
        )

        # Botón para avanzar
        boton_avanzar = ttk.Button(
            contenedor, text=">", command=self.Avanzar
        )
        boton_avanzar.grid(
            row=0, column=1, sticky="we", padx=5, pady=5
        )

        # Botón para borrar
        boton_borrar = ttk.Button(
            contenedor, text="Borrar", command=self.Borrar
        )
        boton_borrar.grid(
            row=0, column=2, sticky="we", padx=5, pady=5
        )

        # Botón Crear
        boton_Crear = ttk.Button(
            contenedor, text="Crear", command=self.Nuevo
        )
        boton_Crear.grid(row=0, column=3, sticky="we", padx=5, pady=5)

        # Botón Recargar
        boton_recargar = ttk.Button(
            contenedor, text="Recargar", command=self.Recargar
        )
        boton_recargar.grid(
            row=0, column=4, sticky="we", padx=5, pady=5
        )

        # Entry para manejar el path
        path_manager = ttk.Entry(
            contenedor, textvariable=self.PATH_VAR
        )
        path_manager.grid(
            row=1, column=0, columnspan=4, sticky="we", padx=5, pady=5
        )

        # Botón para ir a ajustes
        boton_ajustes = ttk.Button(
            contenedor, text="⚙️", command=self.Configuracion
        )
        boton_ajustes.grid(
            row=1, column=4, sticky="we", padx=5, pady=5
        )

        # Treeview para mostrar la información
        columnas = ["Nombre", "Clasificación", "Extensión", "Tamaño"]

        scrollbar = ttk.Scrollbar(
            home, orient="vertical", bootstyle="secondary-round"
        )
        scrollbar.pack(side="right", fill="y")

        self.contenedor_visual = ttk.Treeview(
            home,
            columns=columnas,
            show="headings",
            yscrollcommand=scrollbar.set,
        )
        self.contenedor_visual.pack(fill="both", expand=True)
        self.contenedor_visual.bind("<Double-1>", self.Avanzar)

        self.contenedor_visual.column(
            "Nombre", width=70, anchor=tk.CENTER
        )
        self.contenedor_visual.column(
            "Clasificación", width=100, anchor=tk.CENTER
        )
        self.contenedor_visual.column(
            "Extensión", width=70, anchor=tk.CENTER
        )
        self.contenedor_visual.column(
            "Tamaño", width=70, anchor=tk.CENTER
        )

        self.contenedor_visual.heading("Nombre", text="Nombre")
        self.contenedor_visual.heading(
            "Clasificación", text="Clasificación"
        )
        self.contenedor_visual.heading("Extensión", text="Extensión")
        self.contenedor_visual.heading("Tamaño", text="Tamaño")

        # Insertar datos por primera vez
        self.Core.insertar_datos(self.contenedor_visual)
