import os 
from colorama import init, Fore, Style
init(autoreset=True)

import json

from archivos import leer_archivo, escribir_archivo
RUTA_USUARIOS = "data/usuarios.json"
RUTA_TURNO = "data/turno_caja.json"

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
            dia = int(input("Dia: "))
            reporte_ventas_dia(dia) 
        elif opcion == "5":
            mes = int(input("Mes: "))
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
    saldo_base = float(input("Saldo inicial: "))
    registrar_apertura_caja(saldo_base) 
    opcion = "-1" 
    while opcion != "0":
        opcion_cajero()
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1": 
            carrito = []
            catalogo = leer_archivo("data/productos.json")
            continuar_compra = "si"
            while continuar_compra.lower() == "si":
                id_prod = input("Codigo/ID de producto: ").strip()
                if not buscar_producto(catalogo, id_prod):
                    print("El producto no existe en el catálogo.")
                    continue
                
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0: 
                    print("La cantidad debe ser positiva.")
                    continue
                
                if not validar_stock_productos(catalogo, id_prod, cantidad):
                    print("Stock insuficiente.")
                    continue
                
                item = cargar_producto_carrito(catalogo, id_prod, cantidad)
                carrito.append(item)
                continuar_compra = input("¿Desea agregar otro producto? (si/no): ").strip()
            
            if carrito: 
                metodo_nombre, descuento_porc = tipo_de_pago()
                total = calcular_total_compra(carrito, descuento_porc)
                print(f"Total a pagar: ${total: .2f}")
                monto_entregado = None
                vuelto = None
                    
                if metodo_nombre == "Efectivo":
                    pago_valido = False
                    while not pago_valido:
                        monto_entregado = float(input("Monto entregado: "))
                        pago_valido = validar_monto(monto_entregado, total)
                    vuelto = calcular_vuelto(monto_entregado, total)
                    print(f"Vuelto: ${vuelto:.2f}")
                    
                confirmacion = input("¿Confirmar venta? (si/no): ")
                if confirmacion.lower().strip() == "si":
                    for item in carrito: 
                        cerrar_venta("si", id_prod, cantidad)
                    registrar_venta(total, metodo_nombre)
                    emision_ticket(carrito, metodo_nombre, descuento_porc, total, vuelto, monto_entregado)
                else: 
                    print(Fore.LIGHTGREEN_EX + "venta cancelada...")
            else: 
                print(Fore.LIGHTYELLOW_EX + "El carrito está vacío...")
        elif opcion == "0":
            saldo_final = float(input("Efectivo contado en caja: "))
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

