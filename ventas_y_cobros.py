import json
from archivos import leer_archivo, escribir_archivo
from funciones.stock import descontar_uni

def buscar_producto(productos: list[dict], ID_producto: str) -> bool:
    """
    Indica si existe un producto con el ID dado.
    Contrato:
        Pre:  - productos es una lista de diccionarios con la clave "ID".
              - ID_producto es un string.
        Post: - Devuelve True si algún producto tiene ese ID.
              - Devuelve False en caso contrario.
    """
    # Recorre el catálogo comparando ID por ID
    for producto in productos:
        if producto["ID"] == ID_producto:
            return True
    return False

def validar_stock_productos(productos: list[dict], ID_producto: str, cantidad: int) -> bool:
    """
    Verifica si hay stock suficiente de un producto para la cantidad pedida.
    Contrato:
        Pre:  - productos es una lista de diccionarios con las claves "ID" y "Stock".
              - ID_producto es un string.
              - cantidad es un entero.
        Post: - Devuelve True si el stock del producto es >= cantidad.
              - Devuelve False si el stock es menor a cantidad.
    """
    for producto in productos:
        if producto["ID"] == ID_producto:
            # Compara el stock disponible con la cantidad solicitada
            return producto["Stock"] >= cantidad

def cargar_producto_carrito(productos: list[dict], ID_producto: str, cantidad: int) -> tuple[str, str, int, float]:
    """
    Arma el ítem que se agrega al carrito para un producto dado.
    Contrato:
        Pre:  - productos es una lista de diccionarios con las claves
                "ID", "Nombre" y "Precio".
              - ID_producto existe en productos y hay stock suficiente
                (validado previamente).
              - cantidad es un entero positivo.
        Post: - Devuelve una tupla (ID, Nombre, cantidad, Precio).
    """
    for producto in  productos:
        if producto["ID"] == ID_producto:
            # El ítem se guarda como tupla: [0]=ID, [1]=Nombre, [2]=cantidad, [3]=Precio
            return producto["ID"], producto["Nombre"], cantidad, producto["Precio"]


def tipo_de_pago() -> tuple[str, int]:
    """
    Pide por consola el método de pago y devuelve el método con su descuento.
    Contrato:
        Pre:  - El usuario ingresa un entero por consola (0, 1 o 2).
        Post: - Devuelve una tupla (nombre_del_método, porcentaje_de_descuento).
              - Descuentos: Efectivo=10, Billetera virtual=5, Tarjeta=0.
    """
    # Métodos de pago y descuento (%) en el mismo orden: el índice los relaciona
    metodos_de_pago = ("Efectivo", "Billetera virtual", "Tarjeta de Débito/Crédito")
    descuentos  = (10, 5, 0)
    print("Seleccione su método de pago.")
    metodo = -1
    while metodo not in (0, 1, 2):
        try:
            metodo = int(input("Ingresar método(0-Efectivo, 1-Billetera virtual, 2- Tarjeta de Débito/Crédito): "))
            if metodo not in(0, 1, 2):
                print("Opción inválida. Intente nuevamente")
        except ValueError:
            print("Debe ingresar un número(0, 1 o 2)")        

    return metodos_de_pago[metodo], descuentos[metodo]


def calcular_total_compra(carrito: list[tuple[str, str, int, float]], descuento: int) -> float:
    """
    Calcula el total de la compra aplicando el descuento del método de pago.
    Contrato:
        Pre:  - carrito es una lista de tuplas (ID, Nombre, cantidad, Precio).
              - descuento es un porcentaje(10, 5 o 0)
        Post: - Devuelve la suma de cantidad * Precio de cada ítem,
                menos el porcentaje de descuento.
    """
    total = 0
    # Suma el subtotal (cantidad * precio) de cada producto del carrito
    for producto in carrito:
        subtotal = producto[2] * producto[3]
        total += subtotal
    # Aplica el descuento porcentual sobre el total
    total -= total * descuento / 100
    return total

def validar_monto(monto: float, total: float) -> bool:
    """
    Verifica que el monto entregado alcance para pagar el total.
    Contrato:
        Pre:  - monto y total son números.
        Post: - Devuelve True si monto >= total.
              - Devuelve False (e imprime un mensaje de error) si monto < total.
    """
    if monto < total:
        print("Monto insuficiente. Por favor, ingrese un monto mayor o igual al total de la compra.")
        return False
    return True

def calcular_vuelto(monto: float, total: float) -> float:
    """
    Calcula el vuelto a devolver al cliente.
    Contrato:
        Pre:  - monto y total son números.
        Post: - Devuelve el vuelto que se debe dar
    """
    return monto - total

def cerrar_venta(confirmacion: str, ID: str, cantidad: int) -> None:
    """
    Cierra o cancela la venta según la confirmación del usuario.
    Contrato:
        Pre:  - confirmacion es un string (se espera "si" o "no").
              - ID y cantidad corresponden a un producto y cantidad válidos.
              - descontar_uni(ID, cantidad) debe estar disponible (importada).
        Post: - Si confirmacion es "si" (sin importar mayúsculas ni espacios):
                descuenta el stock del producto e imprime mensaje de agradecimiento.
              - En cualquier otro caso imprime "Venta cancelada." y no modifica stock.
    """
    # Se normaliza la respuesta: sin espacios y en minúsculas
    if confirmacion.lower().strip() == "si":
        descontar_uni(ID, cantidad)
        print("Venta cerrada. ¡Gracias por su compra!")
    else:
        print("Venta cancelada.")
        
def emision_ticket(carrito: list[tuple[str, str, int, float]], metodo: str, descuento: int,
                   total: float, vuelto: float, monto: float | None = None) -> None:
    """
    Imprime por consola el ticket de la venta realizada.
    Contrato:
        Pre:  - carrito es una lista de tuplas (ID, Nombre, cantidad, Precio).
              - metodo es el nombre del método de pago elegido.
              - descuento es un porcentaje entre 0 y 100.
              - total es el total final ya calculado con el descuento aplicado.
              - monto y vuelto son opcionales (se informan solo si se pagó en efectivo).
        Post: - Imprime el detalle de cada producto, subtotal, descuento, total,
                y (si se indicaron) monto entregado y vuelto.
              - No modifica el carrito ni ningún otro dato.
              - No devuelve ningún valor.
    """
    ancho = 44
    # Subtotal sin descuento y monto descontado
    subtotal = sum(p[2] * p[3] for p in carrito)
    monto_descuento = subtotal - total

    print("=" * ancho)
    print("TICKET DE COMPRA".center(ancho))
    print("=" * ancho)
    print(f"{'Producto':<20}{'Cant.':>6}{'Precio':>9}{'Importe':>9}")
    print("-" * ancho)
    # Una línea por producto del carrito
    for producto in carrito:
        nombre = producto[1][:19]
        importe = producto[2] * producto[3]
        print(f"{nombre:<20}{producto[2]:>6}{producto[3]:>9.2f}{importe:>9.2f}")
    print("-" * ancho)
    print(f"{'Subtotal:':<35}${subtotal:>8.2f}")
    print(f"{f'Descuento ({descuento}%):':<35}-${monto_descuento:>7.2f}")
    print(f"{'TOTAL:':<35}${total:>8.2f}")
    print(f"Método de pago: {metodo}")
    # Monto y vuelto solo si se informaron
    if monto is not None:
        print(f"{'Monto entregado:':<35}${monto:>8.2f}")
    if vuelto is not None:
        print(f"{'Vuelto:':<35}${vuelto:>8.2f}")
    print("=" * ancho)
    print("¡Gracias por su compra!".center(ancho))
