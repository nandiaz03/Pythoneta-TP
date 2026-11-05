from archivos import leer_archivo, escribir_archivo, RUTA_PRODUCTOS

def consultar_stock(seccion: str) -> None:
    """
    Contrato:
        - Muestra los productos de una sección o faltante de stock.

    Precondición:
        - Seccion es un string que indica el nombre una sección para ordenar varios productos
        (Ejemplo, Seccion: lacteos, Productos: queso, leche, crema).

    Postcondición:
        - Muestra en pantalla los productos correspondientes.
    """
    f = leer_archivo(RUTA_PRODUCTOS)
    verificador = False #El verificador sirve para indicar si existe algun producto en esa seccion

    for dic in f:
            if dic["Seccion"].lower() == seccion.strip().lower():
                verificador = True
                print(f"Producto: {dic['Nombre']} - ", end="")
                if dic["Stock"] == 0:
                    print("No hay stock!")

                elif dic["Stock"] <= 10:
                    print(f"Hay poco stock {dic['Stock']}.")

                else:
                    print(f"Hay suficiente stock ({dic['Stock']})")

    if verificador == False:
        print("No existe dicha seccion en el sistema o no hay ningun producto en ella.")


def agregar_stock(producto: str) -> None:
    """
    Contrato:
        - Permite agregar unidades al stock de un producto.

    Precondicion:
        - Producto es un string que indica el nombre de un producto en el archivo 'productos.json'

    postcondicion:
        - Actualiza el archivo json aumentando el stock del producto seleccionado por el usuario.
        - En caso de no existir el producto ingresado en el archivo 'productos.json', se realiza un print que
        informa que no existe el producto.
    """
    f = leer_archivo(RUTA_PRODUCTOS)
    for dic in f:
        if producto.strip().lower() == dic["Nombre"].lower():
            print(f"El producto {dic['Nombre']} tiene {dic['Stock']} stock.")
            while True:
                try:
                    nuevo_stock = int(input("Ingrese la cantidad de stock que quiere añadir al producto: "))

                    if nuevo_stock <= 0:
                        print("Error, la cantidad de stock a agregar debe ser positiva.")
                        continue

                except ValueError:
                    print("El numero debe ser un entero positivo.")

                else:
                    dic["Stock"] += nuevo_stock
                    break

            escribir_archivo(RUTA_PRODUCTOS, f)
            return

    print("No existe ese producto.")


def eliminar_stock(producto: str) -> None:
    """
    Contrato:
        - Permite descontar unidades manualmente del stock.

    Precondiciones:
        - Producto es un string que indica el nombre de un producto en el archivo 'productos.json'

    Postcondicion:
        - Actualiza el archivo json reduciendo el stock del producto ingresado.
        - En caso de no existir el producto ingresado en el archivo 'productos.json', se realiza un print que
        informa que no existe el producto.
    """
    f = leer_archivo(RUTA_PRODUCTOS)

    for dic in f:
        if producto.strip().lower() == dic["Nombre"].lower():
            print(f"El producto {dic['Nombre']} tiene {dic['Stock']} stock.")
            while True:
                try:
                    nuevo_stock = int(input("Ingrese la cantidad de stock que quiere reducir del producto: "))
                    if nuevo_stock <= 0:
                        print("Error, el stock debe ser un entero positivo.")
                        continue

                except ValueError:
                    print("Se debe ingresar un entero positivo.")

                else:
                    # Si el stock que quiere eliminar es mayor o igual que el stock disponible, este pasa a ser 0.
                    if nuevo_stock >= dic["Stock"]:
                        dic["Stock"] = 0

                    # Si no, se le resta lo ingresado al stock disponible.
                    else:
                        dic["Stock"] -= nuevo_stock
                    break

            escribir_archivo(RUTA_PRODUCTOS, f)
            return

    print("No existe ese producto.")


def descontar_uni(producto: str, cantidad: int) -> None:
    """
    Contrato:
        - Resta las unidades vendidas del stock una vez cerrada la compra.

    Precondicion:
        - producto es un string que indica que producto del archivo 'productos.json'}
        - cantidad es un entero que indica la cantidad de stock que se le debe.

    Postcondicion:
        - Actualiza el archivo json descontando del producto indicado el stock equivalente a la venta realizada.
        - Retorna
    """
    f = leer_archivo(RUTA_PRODUCTOS)
    for dic in f:
        if producto == dic["ID"]:
            dic["Stock"] = max(0, dic["Stock"] - cantidad)
            escribir_archivo(RUTA_PRODUCTOS, f)
            break

def _generar_id(productos: list[dict]) -> str:
    """Devuelve el próximo ID libre con formato P001, P002, ..."""
    numeros = [int(d["ID"][1:]) for d in productos
               if d["ID"][1:].isdigit()]
    return f"P{max(numeros, default=0) + 1:03d}"


def agregar_producto(nombre: str) -> None:
    """
    Contrato:
        - Permite dar de alta un producto nuevo en el catálogo.

    Precondicion:
        - nombre es un string no vacío con el nombre del producto nuevo.

    Postcondicion:
        - Pide por consola la sección, el precio y el stock inicial.
        - Agrega al archivo 'productos.json' el producto con un ID generado automáticamente
          (ID, Nombre, Seccion, Precio, Stock).
        - Si el nombre está vacío o ya existe un producto con ese nombre, informa el error
          y no modifica el archivo.
    """
    nombre = nombre.strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    f = leer_archivo(RUTA_PRODUCTOS)
    for dic in f:
        if dic["Nombre"].lower() == nombre.lower():
            print(f"Ya existe un producto llamado {dic['Nombre']} (ID {dic['ID']}). "
                  "Use 'Agregar Stock' para sumarle unidades.")
            return

    seccion = ""
    while not seccion:
        seccion = input("Sección: ").strip()
        if not seccion:
            print("La sección no puede estar vacía.")

    # Si la sección ya existe con otra capitalización, se reutiliza esa (ej. "lacteos" -> "Lacteos")
    for dic in f:
        if dic["Seccion"].lower() == seccion.lower():
            seccion = dic["Seccion"]
            break

    while True:
        try:
            precio = float(input("Precio: ").strip().replace(",", "."))
            if precio <= 0:
                print("Error, el precio debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("El precio debe ser un número.")

    while True:
        try:
            stock = int(input("Stock inicial: ").strip())
            if stock < 0:
                print("Error, el stock no puede ser negativo.")
                continue
            break
        except ValueError:
            print("El stock debe ser un número entero.")

    nuevo = {
        "ID": _generar_id(f),
        "Nombre": nombre,
        "Seccion": seccion,
        "Precio": precio,
        "Stock": stock
    }
    f.append(nuevo)
    escribir_archivo(RUTA_PRODUCTOS, f)
    print(f"Producto agregado: {nuevo['Nombre']} (ID {nuevo['ID']}, {nuevo['Seccion']}, "
          f"${nuevo['Precio']:.2f}, stock {nuevo['Stock']}).")