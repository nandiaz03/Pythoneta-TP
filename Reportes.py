from datetime import date
from archivos import leer_archivo, escribir_archivo

RUTA_VENTAS = "ventas.json"


def registrar_venta(total: float, metodo: str) -> None:
    """Guarda una venta confirmada en 'ventas.json'.

    Precondición:
        - 'total' es un número mayor o igual a 0.

    Postcondición:
        - Agrega al archivo un registro con fecha de hoy, total y método.
    """
    ventas = leer_archivo(RUTA_VENTAS)
    ventas.append({
        "fecha": date.today().isoformat(),
        "total": total,
        "metodo": metodo
    })
    escribir_archivo(RUTA_VENTAS, ventas)


def reporte_ventas_dia(dia: int) -> None:
    """Muestra la recaudación de un día del mes actual.

    Precondición:
        - 'dia' es un entero entre 1 y 31.

    Postcondición:
        - Muestra el total recaudado y la cantidad de ventas del día.
        - Si el día no existe en el mes actual, informa el error.
    """
    hoy = date.today()
    try:
        fecha = date(hoy.year, hoy.month, dia).isoformat()
    except ValueError:
        print(f"El día {dia} no existe en el mes actual.")
        return

    ventas_dia = [v for v in leer_archivo(RUTA_VENTAS) if v["fecha"] == fecha]
    total = sum(v["total"] for v in ventas_dia)

    print(f"\n--- REPORTE DÍA {dia}/{hoy.month}/{hoy.year} ---")
    if not ventas_dia:
        print("No hay ventas registradas para ese día.")
    else:
        print(f"Cantidad de ventas: {len(ventas_dia)}")
        print(f"Recaudación total: ${total:.2f}")


def reportes_ventas_mes(mes: int) -> None:
    """Muestra la recaudación de un mes del año actual.

    Precondición:
        - mes es un entero entre 1 y 12.
        - anio debe ser un entero positivo

    Postcondición:
        - Muestra el total recaudado, la cantidad de ventas y el desglose por método de pago.
    """
    if mes < 1 or mes > 12:
        print("El mes debe estar entre 1 y 12.")
        return

    anio = date.today().year
    ventas_mes = [v for v in leer_archivo(RUTA_VENTAS) if v["fecha"]]

    print(f"\n--- REPORTE MES {mes}/{anio} ---")
    if not ventas_mes:
        print("No hay ventas registradas para ese mes.")
        return

    por_metodo: dict = {}
    for v in ventas_mes:
        por_metodo[v["metodo"]] = por_metodo.get(v["metodo"], 0) + v["total"]

    print(f"Cantidad de ventas: {len(ventas_mes)}")
    for metodo, subtotal in por_metodo.items():
        print(f"  {metodo}: ${subtotal:.2f}")
    print(f"Recaudación total: ${sum(por_metodo.values()):.2f}")


def total_efectivo_hoy() -> float:
    """Suma las ventas en efectivo de hoy 
    Precondición:
        - Ninguna.

    Postcondición:
        - Retorna el total cobrado en efectivo en la fecha actual.
    """
    hoy = date.today().isoformat()
    return sum(v["total"] for v in leer_archivo(RUTA_VENTAS)
               if v["fecha"] == hoy and v["metodo"] == "Efectivo")