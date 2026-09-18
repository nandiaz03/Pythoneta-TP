# ========================================================
# SISTEMA DE COMERCIO Y VENTAS
#=========================================================
usuarios = {
    'nandiaz': {'clave': '1234', 'rol':'admin'},
    'ibattelli':{'clave': '4321', 'rol': 'cajero'}
    }

#-----------------------------------------------------------
#                       LOGIN Y ROLES
#-----------------------------------------------------------
def pedir_credenciales() -> tuple:
    """solicita usuario y clave 
    precondicion: no tiene
    postcondicion: retorna una tupla (usuario, clave)"""
    usuario = input("ingresar usuario: ").strip()
    clave = input("ingresar contraseña: ").strip()
    return usuario, clave

def iniciar_sesion(usuario:str, clave:int) -> bool:
    """verificacion de usuario y clave
    precondicion: al ingresar usuario no debe estar vacio y clave debe ser un numero entero de 4 digitos posivos
    postcondicion: retornar true si el acceso es correcto"""
    if usuario in usuarios and usuarios[usuario]['clave'] == clave:
        return True
    return False

def definir_rol(rol: str)->str: 
    """ determina a que menu debe redirigirse el usuario
    precondión: rol debe ser admin o cajero
    postcondición: retorna la ruta del menu correspondiente"""
    return rol

def cajero_fecha(dia:int, mes:int, anio:int)->bool:
    """solicita y valida la fecha en la que opera el cajero
    precondición: fecha debe ser un entero positivo 
    postcondición: retorna True si la fecha es valida"""
    print("Esta función valida la fecha")

def registrar_apertura_caja(saldo_base: float)->bool:
    """ solicita al usuario el saldo inicial de efectivo disponible al inicio de turno
    precondicion: saldo_base debe ser un numero mayor o igual a 0 
    postcondicion: retorna True si el saldo base es valido"""
    print("Esta funcion registra y valia el saldo inicial del turno")

def cierre_caja(saldo_base: float, saldo_final: float)->float:
    """Calcula y registra el efectivo final de caja al cerrar el turno
    precondicion: saldo_final debe ser un numero mayor o igual a 0 
    postcondicion: retorna la diferencia entre el saldo final y el saldo base registrado"""
    print("Esta funcion registra el cierre de caja calculo la diferencia con el saldo base")

#-----------------------------------------------------------
#                                 STOCK
#-----------------------------------------------------------

def consultar_stock(seccion: str)->None:
    """muestra los productos de una seccion o faltante de stock
    precondición: seccion debe ser una seccion valida o sin stock o poco stock
    postcondición: muestea en pantalla los productos correspondientes"""
    print("Esta funcion muestra el stock disponible  a punto de quedarse sin stock")
    
def agregar_stock(producto: str, cantidad: int)->None:
    """agregar unidades al carrito de un producto
    precondicion: producto debe ser un string no vacio 
    postcondicion: incrementa el stock del producto"""
    print("Esta funcion agrega unidades al carrito")
    
def eliminar_stock(producto: str, cantidad:int)->None:
    """ descuenta unidades manualmente del stock 
    precondiciones: producto debe ser un string no vacio y cantidad debe ser un numero positivo
    postcondicion: reduce el stock del producto"""
    print("Esta funcion elimina productos del stock")

def descontar_uni(producto:str, cantidad:int)->None:
    """resta las unidades vendidas del stock una vez cerrada la compra
    precondicion: producto debe existir en el stock y cantidad debe ser menor o igual al stock registrado
    postcondicion: actualiza el stock cargado"""
    print("La funcion actualiza el stock cargado")

#-----------------------------------------------------------
#                                 REPORTES
#-----------------------------------------------------------

def reporte_ventas_dia(dia:int)->None:
    """calcula y muestra la recaudacion del dia
    precondicion: dia debe ser una fecha valida del numero entero positivo
    postcondicion: muestra el toal de ventas del dia""" 
    print("Esta funcion muestra la recaudacion del dia")

def reportes_ventas_mes(mes:int)->None:
    """calcula y muestra recaudacion mensual
    precondicion: mes debe ser un numero entre 1 y 12
    postcondicion: muestra el total acumulado del mes"""
    print("Esta funcion muestra el total del mes")

#-----------------------------------------------------------
#                                 VENTA
#-----------------------------------------------------------

def cargar_producto_carrito(codigo_producto: int, cantidad: int)->None:
    """agregar un producto disponible al carrito de compra
    precondicion: producto debe ser un string no vacio. cantidad debe ser mayor a 0 y menor igual al stock disponible.
    postcondicion: el producto se suma al carrito"""
    print("Esta funcion permite agregar producto al carrito")

def calcular_total_compra(subtotal: float)->float:
    """calcula el precio final a cobrar de la compra actual
    precondicion: subtotal debe ser mayor igual a 0
    postcondicones: retorna el valor total de la venta"""
    print("Esta funcion calcula el total de la compra")

def tipo_de_pago(medio_de_pago:int)->int:
    """define el medio de pago seleccionado por el cliente
    precondicion: opcion debe ser numero entero 1 (efectico) o 2 (tarjeta/billetera virtual)
    postcondicion: Retorna el nombre del metodo de pago"""
    print("Esta funcion retorna que tipo de pago fue")

def validar_monto(monto: float, total: float)->bool:
    """Validar el monto entregado por el cliente
    precondicion: monto debe ser un numero positivo y mayor igual al total
    postcondicion: retorna True si el monto es valido y Falso en caso contrario"""
    print("Esta funcion valida si el monto entregado es correcto")
    
def calcular_vuelto(total:float, pago:float)->float:
    """si es en efectivo, calcula el vuelto y la cantidad a devolver del cliente
    precondicion: pago debe ser mayor a total
    postcondicion: retorna el monto a devolver en billetes"""
    print("Esta funcion realiza el calculo del vuelto")

def cerrar_venta(confirmacion:int)->bool: 
    """confirma si se concreta la venta  si se reseta la compra
    precondicion: confirmacion debe ser 1 (si) o 0 (no)
    postcondicion: retorna True si se confirma, False si se cancela o vuelve"""
    print("Esta funcion confirma/cancela la venta")

def emision_ticket(total:float, medio_pago:str)->None:
    """ imprime el comproante final del operacion
    percondicion: total debe ser mayor a 0 y medio_pago debe ser efectivo o tarjeta/billetera
    postcondicion: muestra el ticket emitido en pantalla"""
    print("Esta funcion imprime un ticket de la compra finalizada")

#-----------------------------------------------------------
#                       MENÚ ADMINISTRADOR
#-----------------------------------------------------------

def opcion_admin()->None:
    """imprime las opciones que el admin puede ejecutar"""
    print("\n================================================")
    print("           PANEL DE ADMINISTRACIÓN               ")
    print("\n================================================")
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
            cantidad = input("cantidad: ")
            agregar_stock(producto, cantidad)
        elif opcion == "3":
            producto = input("producto: ")
            cantidad = input("cantidad: ")
            eliminar_stock(producto, cantidad)
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
    print("\n================================================")
    print("           PANEL DE VENTAS (CAJA)               ") 
    print("\n================================================")
    print("1. Iniciar nueva venta")
    print("0. Cerrar turno")

def menu_cajero()->None:
    saldo_base = float(input("Saldo inicial: "))
    cajero_fecha(dia=18, mes=9, anio=2026)
    registrar_apertura_caja(saldo_base) 
    opcion = "-1" 
    while opcion != "0":
        opcion_cajero()
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1": 
            codigo_producto = int(input("Codigo de producto: "))
            cantidad = int(input("Cantidad: "))
            cargar_producto_carrito(codigo_producto, cantidad)
            
            subtotal = float(input("subtotal: "))
            total = calcular_total_compra (subtotal)
            
            medio_de_pago = int(input("medio de pago (1- efectivo, 2- tarjeta/billetera virtual): ")) 
            medio = tipo_de_pago(medio_de_pago)
            
            if medio == 1: 
                pago = float(input("Monto: "))
                calcular_vuelto(total, pago)
                
            confirmacion = int(input("confirmar venta (1- si, 0- no): ")) 
            confirmado = cerrar_venta(confirmacion)
            
            if confirmado == True: 
                producto = input("producto vendido: ")
                descontar_uni(producto, cantidad)
                emision_ticket(total, medio)
            else: 
                print("venta cancelada...")
        elif opcion == "0":
            saldo_final = float(input("Efectivo contado en caja: "))
            cierre_caja(saldo_base, saldo_final)
            print("Cerrando turno de caja...")
        else: 
            print("Opcion no valida")

#-----------------------------------------------------------
#                       LOGIN PRINCIPAL
#----------------------------------------------------------- 

def principal_opciones()->None: 
    "imprime el inicion de sesion al sitema"
    print("\n================================================") 
    print("           SISTEMA DE COMERCIO Y VENTAS            ") 
    print("\n================================================")
    print("1. Iniciar sesion como administrador")
    print("2. Iniciar sesion como cajero")
    print("0. Salir")
    
    
def derivar_usuario()->None:
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
        
            usuario,clave = pedir_credenciales()
            if not iniciar_sesion(usuario, clave):
                print("usuario o contraseña incorrectos")
                continue
            
            rol = definir_rol(usuarios[usuario]['rol'])
            if rol != rol_solicitado: 
                print("el usuario" + usuario + "no tiene permisos de" + rol_solicitado)
                continue
            else:
                print("Bienvenido" + usuario + "!")
            
            if rol == 'admin':
                menu_admin()
            else: 
                menu_cajero()
            
        elif opcion == "0":
            print("saliendo del sistema...")
        else: 
            print("Opcion incorrecta.")

derivar_usuario()

