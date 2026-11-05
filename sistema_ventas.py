import os

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    # Si colorama no está instalado el programa funciona igual, sin colores.
    class _SinColor:
        def __getattr__(self, nombre):
            return ""
    Fore = Style = _SinColor()

from archivos import leer_archivo, RUTA_PRODUCTOS

from funciones.autenticacion_roles import (
    cargar_usuarios,
    pedir_credenciales,
    iniciar_sesion,
    definir_rol,
    cajero_fecha,
    registrar_apertura_caja,
    cierre_caja,
)

from funciones.stock import (
    agregar_stock, 
    consultar_stock, 
    eliminar_stock
)

from funciones.ventas_y_cobros import (
    buscar_producto,
    validar_stock_productos,
    cargar_producto_carrito,
    tipo_de_pago,
    calcular_total_compra,
    validar_monto,
    calcular_vuelto,
    cerrar_venta,
    emision_ticket,
)

from funciones.reportes import (
    reporte_ventas_dia,
    reportes_ventas_mes,
    registrar_venta,
    total_efectivo_hoy
)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pedir_entero(mensaje: str) -> int | None:
    """Pide un entero por consola. Devuelve None si el texto no es un entero válido."""
    try:
        return int(input(mensaje).strip())
    except ValueError:
        print(Fore.RED + "Debe ingresar un número entero.")
        return None


def pedir_numero(mensaje: str) -> float | None:
    """Pide un número por consola. Devuelve None si el texto no es un número válido."""
    try:
        return float(input(mensaje).strip().replace(",", "."))
    except ValueError:
        print(Fore.RED + "Debe ingresar un número válido.")
        return None
#-----------------------------------------------------------
#                       MENÚ ADMINISTRADOR
#-----------------------------------------------------------

def opcion_admin()->None:
    """imprime las opciones que el admin puede ejecutar"""
    print(Fore.LIGHTGREEN_EX + "\n================================================")
    print(Fore.GREEN + "           PANEL DE ADMINISTRACIÓN               ")
    print(Fore.LIGHTGREEN_EX + "\n================================================")
    print("1. Consultar Stock (Seccion o Alertas)")
    print("2. Agregar Stock")
    print("3. Eliminar/Modificar Stock")
    print("4. Reporte de Ventas del dia")
    print("5. Reporte de ventas del mes")
    print("0. Volver al login")
    
def menu_admin()->None:
    opcion = "-1"
    while opcion != "0":
        opcion_admin()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1": 
            seccion = input("Ingrese la seccion: ")
            consultar_stock(seccion)
        elif opcion == "2": 
            producto = input("producto: ")
            agregar_stock(producto)
        elif opcion == "3":
            producto = input("producto: ")
            eliminar_stock(producto)
        elif opcion == "4": 
            dia = pedir_entero("Dia: ")
            if dia is not None:
                reporte_ventas_dia(dia)
        elif opcion == "5":
            mes = pedir_entero("Mes: ")
            if mes is not None:
                reportes_ventas_mes(mes)
        elif opcion == "0":
            print("Cerrando sesion de administrador...")
        else: 
            print("Opcion no valida")

#-----------------------------------------------------------
#                       MENÚ CAJERO
#-----------------------------------------------------------

def opcion_cajero()->None:
    """imprime las opciones que el cajero puede ejecutar"""
    print(Fore.LIGHTGREEN_EX + "\n================================================")
    print(Fore.GREEN + "           PANEL DE VENTAS (CAJA)               ") 
    print(Fore.LIGHTGREEN_EX + "\n================================================")
    print("1. Iniciar nueva venta")
    print("0. Cerrar turno")

def menu_cajero()->None:
    saldo_base = None
    while saldo_base is None or not registrar_apertura_caja(saldo_base):
        saldo_base = pedir_numero("Saldo inicial: ")
    opcion = "-1" 
    while opcion != "0":
        opcion_cajero()
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1": 
            carrito = []
            catalogo = leer_archivo(RUTA_PRODUCTOS)
            continuar_compra = "si"
            while continuar_compra.lower() == "si":
                id_prod = input("Codigo/ID de producto: ").strip().upper()
                if not buscar_producto(catalogo, id_prod):
                    print("El producto no existe en el catálogo.")
                    continue
                
                cantidad = pedir_entero("Cantidad: ")
                if cantidad is None:
                    continue
                if cantidad <= 0: 
                    print("La cantidad debe ser positiva.")
                    continue
                
                # Se suma lo que ya hay en el carrito del mismo producto para no pasarse del stock
                ya_en_carrito = sum(i[2] for i in carrito if i[0] == id_prod)
                if not validar_stock_productos(catalogo, id_prod, cantidad + ya_en_carrito):
                    print("Stock insuficiente.")
                    continue
                
                item = cargar_producto_carrito(catalogo, id_prod, cantidad)
                carrito.append(item)
                continuar_compra = input("¿Desea agregar otro producto? (si/no): ").strip()
            
            if carrito: 
                metodo_nombre, descuento_porc = tipo_de_pago()
                total = calcular_total_compra(carrito, descuento_porc)
                print(f"Total a pagar: ${total:.2f}")
                monto_entregado = None
                vuelto = None
                    
                if metodo_nombre == "Efectivo":
                    pago_valido = False
                    while not pago_valido:
                        monto_entregado = pedir_numero("Monto entregado: ")
                        if monto_entregado is None:
                            continue
                        pago_valido = validar_monto(monto_entregado, total)
                    vuelto = calcular_vuelto(monto_entregado, total)
                    print(f"Vuelto: ${vuelto:.2f}")
                    
                confirmacion = input("¿Confirmar venta? (si/no): ")
                if confirmacion.lower().strip() == "si":
                    for item in carrito: 
                        cerrar_venta("si", item[0], item[2])
                    registrar_venta(total, metodo_nombre)
                    emision_ticket(carrito, metodo_nombre, descuento_porc, total, vuelto, monto_entregado)
                else: 
                    print(Fore.LIGHTGREEN_EX + "venta cancelada...")
            else: 
                print(Fore.LIGHTYELLOW_EX + "El carrito está vacío...")
        elif opcion == "0":
            saldo_final = None
            while saldo_final is None or saldo_final < 0:
                saldo_final = pedir_numero("Efectivo contado en caja: ")
                if saldo_final is not None and saldo_final < 0:
                    print(Fore.RED + "El efectivo no puede ser negativo.")
            esperado = saldo_base + total_efectivo_hoy()
            diferencia = cierre_caja(esperado, saldo_final)
            print(f"Diferencia de arqueo: ${diferencia:.2f}")
            print(Fore.BLUE + "Cerrando turno de caja...")
        else: 
            print("Opcion no valida")

#-----------------------------------------------------------
#                       LOGIN PRINCIPAL
#----------------------------------------------------------- 

def principal_opciones()->None: 
    "imprime el inicion de sesion al sitema"
    print(Fore.LIGHTCYAN_EX + "\n================================================") 
    print(Fore.CYAN + "           SISTEMA DE COMERCIO Y VENTAS            ") 
    print(Fore.LIGHTCYAN_EX + "\n================================================")
    print("1. Iniciar sesion como administrador")
    print("2. Iniciar sesion como cajero")
    print("0. Salir")
    
    
def main()->None:
    """llamarla main"""
    "verificar la opcion ingresada y lo deriva al menu corresponinte"
    opcion = "-1"
    while opcion != "0":
        principal_opciones()
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1" or opcion == "2":
            if opcion == "1":
                rol_solicitado = 'admin'
            else:
                rol_solicitado = 'cajero'
            usuarios = cargar_usuarios()

            usuario, clave = pedir_credenciales()
            if not iniciar_sesion(usuario, clave):
                print(Fore.RED + "usuario o contraseña incorrectos")
                continue
            
            rol = definir_rol(usuarios[usuario]['rol'])
            if rol != rol_solicitado: 
                print(Fore.RED + f"el usuario {usuario} no tiene permisos de {rol_solicitado}")
                continue
            else:
                print(Fore.LIGHTYELLOW_EX + f"Bienvenido {usuario}!")
            
            if rol == 'admin':
                menu_admin()
            else: 
                menu_cajero()
            
        elif opcion == "0":
            print(Fore.BLUE + "saliendo del sistema...")
            limpiar_pantalla()
        else: 
            print(Fore.RED + "Opcion incorrecta.")

if __name__ == "__main__":
    main()

