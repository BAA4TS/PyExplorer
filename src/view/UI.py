import os
import tkinter as tk

import ttkbootstrap as ttk
from src.core.Cargador import Cargador
from src.view.views.Configuracion import Config
from src.view.views.Home import Home


class PyExplorer(tk.Tk):

    def __init__(self):
        super().__init__()

        # Instancia al Core
        self.Core = Cargador()

        # Actualizar la Ruta desde donde se Incio
        self.Core.modificar("PATH", os.getcwd())

        # Cargar Configuracion
        self.Configuracion()

        # Cargar el Ui
        self.UI()

        # Actualizar la Ruta desde donde se Incio
        self.Core.modificar("PATH", os.getcwd())

    def Configuracion(self):
        self.title("PyExplorer")

        # Cargar Tema del Archivo
        Tema = self.Core.obtener("Tema")
        self.Core.establecer_tema(Tema)
        self.minsize(width=450, height=450)
        self.maxsize(width=560, height=600)

    def UI(self):

        # Interfaces
        self.InterfasHome = ttk.Frame(self)
        self.InterfasConfiguracion = ttk.Frame(self)

        # Llamar las Interfas
        Home(self.Visualisador, self.InterfasConfiguracion).View(
            self.InterfasHome
        )

        Config(self.Visualisador, self.InterfasHome).view(
            self.InterfasConfiguracion
        )

        self.Visualisador(self.InterfasHome)

    def Visualisador(self, Pestaña):
        self.InterfasHome.pack_forget()
        self.InterfasConfiguracion.pack_forget()
        Pestaña.pack(expand=True, fill="both")
