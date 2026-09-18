def iniciar_sesion(usuario:str, clave:int) -> bool:
    """verificacion de usuario y clave
    precondicion: al ingresar usuario no debe estar vacio y clave debe ser un numero entero de 4 digitos posivos
       postcondicion: retornar true si el acceso es correcto"""
    print("Esta funcion permite ingresar el usuario")

def cajero_fecha(dia:int, mes:int, anio:int)->bool:
    """solicita y valida la fecha en la que opera el cajero
    precondición: fecha debe ser un entero positivo 
    postcondición: retorna True si la fecha es valida"""
    print("Esta función valida la fecha")

def definir_rol(rol: str)->str: 
    """ determina a que menu debe redirigirse el usuario
    precondión: rol debe ser admin o cajero
    postcondición: retorna la ruta del menu correspondiente"""
    print("Esta funcion deriva el rol de admin o usuario")

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

def registrar_apertura_caja(saldo_base: float)->bool:
    """ solicita al usuario el saldo inicial de efectivo disponible al inicio de turno
    precondicion: saldo_base debe ser un numero mayor o igual a 0 
    postcondicion: retorna True si el saldo base es valido"""
    print("Esta funcion registra y valia el saldo inicial del turno")

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

def tipo_de_pago(opcion:int)->int:
    """define el medio de pago seleccionado por el cliente
    precondicion: opcion debe ser numero entero 1 (efectico) o 2 (tarjeta/billetera virtual)
    postcondicion: Retorna el nombre del metodo de pago"""
    print("Esta funcion retorna que tipo de pago fue")

def cerrar_venta(confirmacion:int)->bool: 
    """confirma si se concreta la venta  si se reseta la compra
    precondicion: confirmacion debe ser 1 (si) o 0 (no)
    postcondicion: retorna True si se confirma, False si se cancela o vuelve"""
    print("Esta funcion confirma/cancela la venta")

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

def descontar_uni(producto:str, cantidad:int)->None:
    """resta las unidades vendidas del stock una vez cerrada la compra
    precondicion: producto debe existir en el stock y cantidad debe ser menor o igual al stock registrado
    postcondicion: actualiza el stock cargado"""
    print("La funcion actualiza el stock cargado")

def emision_ticket(total:float, medio_pago:str)->None:
    """ imprime el comproante final del operacion
    percondicion: total debe ser mayor a 0 y medio_pago debe ser efectivo o tarjeta/billetera
    postcondicion: muestra el ticket emitido en pantalla"""
    print("Esta funcion imprime un ticket de la compra finalizada")
    
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
    opcion != "-1"
    while opcion != "0":
        opcion_admin()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1": 
            consultar_stock(seccion)
        elif opcion == "2": 
            agregar_stock(producto, cantidad)
        elif opcion == "3":
            eliminar_stock(producto, cantidad)
        elif opcion == "4": 
            reporte_ventas_dia(dia) 
        elif opcion == "5":
            reportes_ventas_mes(mes)
        elif opcion == "0":
            print("Cerrando sesion de administrador...")
        else: 
            print("Opcion no valida")
        
def opcion_cajero()->None:
    """imprime las opciones que el cajero puede ejecutar"""
    print("\n================================================")
    print("           PANEL DE VENTAS (CAJA)               ") 
    print("\n================================================")
    print("1. Iniciar nueva venta")
    print("0. Cerrar turno")

def menu_cajero()->None:
    cajero_fecha(dia, mes, anio)
    registrar_apertura_caja(saldo_base)
    opcion = "-1" 
    while opcion != "0":
        opcion = input("Ingrese una opcion: ")
        if opcion == "1": 
            cargar_producto_carrito(codigo_producto, cantidad)
            total = calcular_total_compra (subtotal)
            medio = tipo_de_pago(opcion)
            if medio == 1: 
                calcular_vuelto(total, pago)
            confirmado = cerrar_venta(confirmacion)
            if confirmado == True: 
                descontar_uni(producto, cantidad)
                emision_ticket(total, medio)
        elif opcion == "0":
            print("Cerrando turno de caja...")
        else: 
            print("Opcion no valida")

def principal_opciones()->None: 
    "imprime el inicion de sesion al sitema"
    print("\n================================================") 
    print("           SISTEMA DE COMERCIO Y VENTAS            ") 
    print("\n================================================")
    print("1. Iniciar sesion como administrador")
    print("2. Iniciar sesion como cajero")
    print("0. Salir")
    
def derivar_usuario()->None:
    "verificar la opcion ingresada y lo deriva al usuario corresponinte"
    opcion = "-1"
    while opcion != "0":
        principal_opciones()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            iniciar_sesion(usuario, clave)
            rol = definir_rol(rol)
        elif opcion == "2":
            iniciar_sesion(usuario, clave)
            rol = definir_rol(rol)
            menu_cajero()
        elif opcion == "0":
            print("saliendo del sistema...")
        else: 
            print("Opcion incorrecta.")

principal_opciones()

