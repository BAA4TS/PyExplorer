import json
import os
import shutil

import ttkbootstrap as ttk


class Cargador:

    def __init__(self):
        """
        Constructor: Verifica si existe la carpeta de configuración,
        si no, la crea asignándole valores por defecto.
        """
        config_path = f'/Users/{os.getenv("USERNAME")}/AppData/Local/PyExplorer/configuracion.json'
        if not os.path.exists(config_path):
            # Crear la carpeta si no existe
            os.makedirs(
                f'/Users/{os.getenv("USERNAME")}/AppData/Local/PyExplorer/',
                exist_ok=True,
            )

            # Datos a guardar por defecto
            DATO = {"PATH": os.getcwd(), "Tema": "superhero"}
            with open(config_path, "w") as file:
                json.dump(DATO, file, indent=4)

    @staticmethod
    def obtener(clave):
        """
        Obtener: Mediante la clave obtienes el dato de la
        configuración en el JSON.

        :param clave: Clave del dato que se desea obtener.
        :return: Valor asociado a la clave.
        """
        with open(
            f'/Users/{os.getenv("USERNAME")}/AppData/Local/PyExplorer/configuracion.json',
            "r",
        ) as file:
            data_json = json.load(file)
            return data_json.get(clave)

    @staticmethod
    def modificar(index, valor):
        """
        Modificar: Modifica un ajuste en el JSON mediante la clave
        (index) y el nuevo valor.

        :param index: Clave del dato que se desea modificar.
        :param valor: Nuevo valor a asignar.
        """
        with open(
            f'/Users/{os.getenv("USERNAME")}/AppData/Local/PyExplorer/configuracion.json',
            "r",
        ) as file:
            data_json = json.load(file)
        data_json[index] = valor
        with open(
            f'/Users/{os.getenv("USERNAME")}/AppData/Local/PyExplorer/configuracion.json',
            "w",
        ) as file:
            json.dump(data_json, file, indent=4)

    @staticmethod
    def borrar_lista(obj_tree_view):
        """
        BorrarLista: Borra todos los elementos de un TreeView.

        :param obj_tree_view: El objeto TreeView del cual se eliminarán todos los elementos.
        """
        obj_tree_view.delete(*obj_tree_view.get_children())

    @staticmethod
    def formateo_tamanio_archivo(archivo_path):
        """
        FormateoTamanioArchivo: Devuelve el tamaño formateado de un archivo en KB, MB o GB.

        :param archivo_path: Ruta del archivo del cual se desea obtener el tamaño.
        :return: Tamaño del archivo formateado como cadena de texto.
        """
        tamanio = os.path.getsize(archivo_path) / (1024 * 1024)

        if tamanio < 1:
            tamanio = os.path.getsize(archivo_path) / 1024
            return f"{tamanio:.4f} KB"
        elif tamanio < 1024:
            return f"{tamanio:.2f} MB"
        elif tamanio >= 1024:
            tamanio = os.path.getsize(archivo_path) / (1024**3)
            return f"{tamanio:.2f} GB"
        else:
            return str(tamanio)

    @staticmethod
    def clasificador(extension):
        """
        Clasificador: Clasifica la extensión de un archivo en categorías.

        :param extension: Extensión del archivo que se desea clasificar.
        :return: Categoría de la extensión ('Win' para extensiones de Windows, o la misma extensión).
        """
        ARCHIVOS_WIN = [
            ".blf",
            ".regtrans-ms",
            ".DAT",
            ".LOG1",
            ".LOG2",
            ".LOG3",
            ".ini",
        ]

        if extension.lower() in ARCHIVOS_WIN:
            return "Win"
        else:
            return "A"

    @staticmethod
    def establecer_tema(tema):
        """
        EstablecerTema: Establece el tema de la aplicación utilizando ttk.Style.

        :param tema: Nombre del tema a establecer.
        """
        estilo = ttk.Style()
        estilo.theme_use(tema)

    def listar_path(self):
        """
        ListarPath: Lista todos los archivos y carpetas en el
        directorio configurado en el JSON.

        :return: Lista de nombres de archivos y carpetas.
        """
        # Path actual en configuración
        path_actual = self.obtener("PATH")

        # Listado de archivos y carpetas en el path actual
        listado = os.listdir(path_actual)

        return listado

    def retroceder(self, obj_tree_view):
        """
        Retroceder: Actualiza el directorio actual en la configuración
        al directorio padre del directorio actual.

        :param obj_tree_view: Objeto TreeView donde se actualizarán los datos después del retroceso.
        """
        path_actual = self.obtener("PATH")
        self.modificar("PATH", os.path.dirname(path_actual))

        self.insertar_datos(obj_tree_view)

    def insertar_datos(self, obj_tree_view):
        """
        InsertarDatos: Inserta datos en un TreeView con información de archivos y carpetas.

        :param obj_tree_view: Objeto TreeView donde se insertarán los datos.
        """
        # Borrar datos previos del TreeView
        self.borrar_lista(obj_tree_view)

        # Obtener archivos y carpetas del directorio actual
        archivos = self.listar_path()

        for archivo in archivos:
            # Crear la ruta completa del archivo o carpeta
            archivo_path = os.path.join(self.obtener("PATH"), archivo)

            if os.path.isfile(archivo_path):
                # Si es un archivo, obtener información relevante
                nombre, extension = os.path.splitext(archivo)
                clasificacion = self.clasificador(extension)
                tamaño_formateado = self.formateo_tamanio_archivo(
                    archivo_path
                )

                # Datos a insertar en el TreeView
                datos = [
                    nombre,
                    clasificacion,
                    extension,
                    tamaño_formateado,
                ]
            else:
                # Si es una carpeta, definir los datos
                datos = [archivo, "C", "None", ""]

            # Insertar datos en el TreeView
            obj_tree_view.insert("", "end", values=datos)

    def avanzar(self, nuevo_path, obj_tree_view):
        """
        Avanzar: Actualiza el directorio actual en la configuración
        al directorio especificado por nuevo_path.

        :param nuevo_path: Ruta del nuevo directorio al cual avanzar.
        :param obj_tree_view: Objeto TreeView donde se actualizarán los datos después de avanzar.
        """
        path_actual = self.obtener("PATH")
        self.modificar("PATH", os.path.join(path_actual, nuevo_path))
        self.insertar_datos(obj_tree_view)

    def borrar(self, index, es_carpeta, obj_tree_view):
        """
        Borrar: Borra un archivo o carpeta del directorio actual.

        :param index: Nombre del archivo o carpeta a borrar.
        :param es_carpeta: Indica si el elemento a borrar es una carpeta (True) o no (False).
        :param obj_tree_view: Objeto TreeView donde se actualizarán los datos después de borrar.
        """
        path_actual = self.obtener("PATH")
        if not es_carpeta:
            if os.path.exists(os.path.join(path_actual, index)):
                os.remove(os.path.join(path_actual, index))
        else:
            shutil.rmtree(os.path.join(path_actual, index))
        self.insertar_datos(obj_tree_view)

    def crear(self, index, obj_tree_view):
        """
        Crear: Crea un archivo vacío o una carpeta en el directorio actual.

        :param index: Nombre del archivo o carpeta a crear.
        :param obj_tree_view: Objeto TreeView donde se actualizarán los datos después de crear.
        """
        path_actual = self.obtener("PATH")
        Medida = len(index)
        Indentificador = index[:1]
        Archivo = index[1:Medida]

        if Indentificador == "$":
            os.makedirs(os.path.join(path_actual, Archivo))
            self.insertar_datos(obj_tree_view)
        elif Indentificador == "&":
            if not os.path.exists(os.path.join(path_actual, Archivo)):
                with open(
                    os.path.join(path_actual, Archivo), "w"
                ) as file:
                    file.write("")
        else:
            pass
