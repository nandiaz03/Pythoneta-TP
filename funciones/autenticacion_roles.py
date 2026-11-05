from datetime import date
from archivos import leer_archivo, escribir_archivo, RUTA_USUARIOS, RUTA_TURNO


def cargar_usuarios() -> dict:
    """Carga los usuarios desde el archivo JSON de usuarios. Si no existe o está vacío,
    lo inicializa con valores por defecto.

    Precondición:
        - Ninguna.

    Postcondición:
        - Retorna un diccionario con los datos de los usuarios registrados.
    """
    usuarios= leer_archivo(RUTA_USUARIOS)
    
    if not usuarios or not isinstance(usuarios, dict):
        usuarios_default: dict = {
            "nandiaz": {"clave": "1234", "rol": "admin"},
            "ibattelli": {"clave": "4321", "rol": "cajero"},
            "agallarati": {"clave": "5678", "rol": "cajero"},
            "vguarachi": {"clave": "8765", "rol": "cajero"}

        }
        escribir_archivo(RUTA_USUARIOS, usuarios_default)
        return usuarios_default
        
    return usuarios


def pedir_credenciales() -> tuple[str, str]:
    """Solicita el nombre de usuario y la contraseña por consola.

    Precondición:
        - Ninguna.

    Postcondición:
        - Retorna una tupla (usuario, clave) con las cadenas ingresadas sin espacios extras.
    """
    usuario= input("Ingresar usuario: ").strip()
    clave= input("Ingresar contraseña: ").strip()
    return usuario, clave


def iniciar_sesion(usuario: str, clave: str) -> bool:
    """Verifica si las credenciales coinciden con algún usuario registrado.

    Precondición:
        - 'usuario' y 'clave' deben ser cadenas de texto no vacías.

    Postcondición:
        - Retorna True si las credenciales son válidas y corresponden a un usuario existente.
        - Retorna False en caso contrario.
    """
    usuarios = cargar_usuarios()
    
    if usuario in usuarios:
        if str(usuarios[usuario]["clave"]) == str(clave):
            return True
            
    return False


def definir_rol(rol: str) -> str:
    """Determina a qué menú debe redirigirse el usuario según su rol.

    Precondición:
        - 'rol' debe ser un string no vacío.

    Postcondición:
        - Retorna 'admin' o 'cajero' si el rol es válido.
        - Retorna 'desconocido' si el rol no tiene permisos asignados.
    """
    rol_limpio= rol.strip().lower()
    
    if rol_limpio in ("admin", "cajero"):
        return rol_limpio
        
    print(f"Advertencia: El rol '{rol}' no es reconocido en el sistema.")
    return "desconocido"


def cajero_fecha(dia: int, mes: int, anio: int) -> bool:
    """Solicita y valida la fecha en la que opera el cajero.

    Precondición:
        - 'dia', 'mes' y 'anio' deben ser números enteros positivos.

    Postcondición:
        - Retorna True si los valores corresponden a una fecha existente en el calendario.
        - Retorna False si la fecha es inválida (ej. 31/02/2026).
    """
    try:
        date(anio, mes, dia)
        return True
    except ValueError:
        print("La fecha ingresada no existe.")
        return False

def registrar_apertura_caja(saldo_base: float) -> bool:
    """Registra el monto inicial de efectivo disponible al abrir la jornada o turno.

    Precondición:
        - 'saldo_base' debe ser un número flotante mayor o igual a 0.0.

    Postcondición:
        - Guarda el turno con estado 'abierta' y el saldo inicial en 'turno_caja.json'.
        - Retorna True si la apertura fue exitosa, False si el saldo base es inválido.
    """
    if saldo_base < 0:
        print("Error: El saldo base inicial no puede ser negativo.")
        return False

    datos_turno: dict = {
        "estado": "abierta",
        "saldo_base": saldo_base,
        "saldo_final": None,
        "diferencia": None
    }

    escribir_archivo(RUTA_TURNO, datos_turno)
    print(f"Jornada iniciada. Saldo base registrado: ${saldo_base:.2f}")
    return True


def cierre_caja(saldo_base: float, saldo_final: float) -> float:
    """Calcula el arqueo de caja, determinando diferencias entre el saldo esperado
    y el efectivo final acumulado.

    Precondición:
        - 'saldo_base' (saldo inicial/esperado) y 'saldo_final' (efectivo contado) 
          deben ser números flotantes mayores o iguales a 0.0.

    Postcondición:
        - Actualiza el archivo 'turno_caja.json' marcando la jornada como 'cerrada'.
        - Retorna la diferencia del arqueo (saldo_final - saldo_base).
          Si la diferencia es 0, la caja cuadra perfectamente.
          Si es positiva, hay sobrante de caja.
          Si es negativa, hay faltante de caja.
    """
    if saldo_final < 0:
        print("Error: El efectivo final acumulado no puede ser negativo.")
        return 0.0

    diferencia = saldo_final - saldo_base

    datos_cierre: dict = {
        "estado": "cerrada",
        "saldo_base": saldo_base,
        "saldo_final": saldo_final,
        "diferencia": diferencia
    }

    escribir_archivo(RUTA_TURNO, datos_cierre)
    
    return diferencia