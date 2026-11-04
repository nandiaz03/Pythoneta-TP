from sistema_ventas import leer_archivo
from sistema_ventas import escribir_archivo

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
    f = leer_archivo("productos.json")
    verificador = False #El verificador sirve para indicar si existe algun producto en esa seccion

    for dic in f:
            if dic["Seccion"] == seccion:
                verificador = True
                print(f"Producto: {dic['Nombre']}", end="")
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
    f = leer_archivo("productos.json")
    for dic in f:
        if producto == dic["Nombre"]:
            print(f"El producto {producto} tiene {dic['Stock']} stock.")
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

            escribir_archivo("productos.json", f)
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
    f = leer_archivo("productos.json")

    for dic in f:
        if producto == dic["Nombre"]:
            print(f"El producto {producto} tiene {dic['Stock']} stock.")
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

            escribir_archivo("productos.json", f)
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
    f = leer_archivo("productos.json")
    for dic in f:
        if producto == dic["ID"]:
            dic["Stock"] -= cantidad            
            escribir_archivo("productos.json", f)
            break