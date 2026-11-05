import json

def leer_archivo(nombre: str):
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            productos = json.load(f)

    except FileNotFoundError:
        productos = []

    return productos


def escribir_archivo(nombre: str, archivo: list):
    with open(nombre, "w", encoding="utf-8") as f:
        json.dump(archivo, f, indent=4)