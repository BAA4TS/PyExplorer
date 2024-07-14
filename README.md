# PyExplorer

PyExplorer es un administrador de archivos simple hecho en Python con una interfaz gráfica basada en `tkinter` y `ttkbootstrap`.

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg) ![License](https://img.shields.io/badge/license-MIT-green) ![Version](https://img.shields.io/badge/version-1.0.0-green) ![Python](https://img.shields.io/badge/python-green?logo=python)

## Descripción

PyExplorer es una herramienta fácil de usar para gestionar archivos y directorios en tu sistema. La aplicación ofrece una interfaz sencilla.

## Requisitos

- Python 3.x
- tkinter
- ttkbootstrap


## Configuración

PyExplorer utiliza una ruta en `AppData` para guardar su configuración de uso. La ruta exacta es:

```bash
C:\Users\TuUsuario\AppData\Local\PyExplorer\configuracion.json
```

El contenido del archivo de configuración es el siguiente:

```json
{
    "PATH": "C:\\Users\\baa4t",
    "Tema": "minty"
}
```

Este archivo es esencial para el funcionamiento de la aplicación. Cuando la aplicación está en ejecución, cualquier cambio en el directorio actual se guardará automáticamente en este archivo.

## Licencia

PyExplorer está licenciado bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

¡Gracias por usar PyExplorer! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio.

---
