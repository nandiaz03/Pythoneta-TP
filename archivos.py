import json
import os

# Las rutas se calculan a partir de la ubicación de este archivo,
# así el programa funciona sin importar desde qué carpeta se ejecute.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

RUTA_PRODUCTOS = os.path.join(DATA_DIR, "productos.json")
RUTA_VENTAS = os.path.join(DATA_DIR, "ventas.json")
RUTA_USUARIOS = os.path.join(DATA_DIR, "usuarios.json")
RUTA_TURNO = os.path.join(DATA_DIR, "turno_caja.json")


def leer_archivo(nombre: str):
    """Lee un archivo JSON. Si no existe o está vacío/corrupto devuelve una lista vacía."""
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def escribir_archivo(nombre: str, archivo) -> None:
    """Escribe datos en un archivo JSON (crea la carpeta si hace falta)."""
    os.makedirs(os.path.dirname(nombre) or ".", exist_ok=True)
    with open(nombre, "w", encoding="utf-8") as f:
        json.dump(archivo, f, indent=4, ensure_ascii=False)
