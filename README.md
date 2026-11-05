Presentacion: file:///C:/Users/Usuario/Downloads/reveal.js-master/index.html#/6
UX: https://www.canva.com/design/DAHUMTJZIlA/8wZYhnJ_cXjczNtzVDa7zg/edit

                                    Vaythoneta - Sistema de gestión de ventas
Proyecto desarrollado en Python para administrar el stock de productos y registrar ventas de un comercio pequeño. La información se almacena en archivos JSON.
Funcionalidades
Inicio de sesión con usuarios y roles.
Menú de administración para consultar, agregar y descontar stock.
Menú de caja para cargar productos al carrito, calcular descuentos, cobrar y emitir tickets.
Registro de apertura y cierre de caja.
Registro de ventas y consulta de reportes diarios y mensuales.
Requisitos
Python 3.10 o superior (el código utiliza anotaciones de tipo como float | None).
No requiere instalar bibliotecas externas: utiliza módulos incluidos en Python.
Archivos del proyecto
Archivo
Responsabilidad
sistema_ventas.py
Punto de entrada y menús principales.
archivos.py
Lectura y escritura de archivos JSON.
autenticacion_roles.py
Usuarios, autenticación, roles y operaciones de caja.
stock.py
Consulta y modificación del inventario.
ventas_y_cobros.py
Carrito, métodos de pago, cálculos y emisión de tickets.
Reportes.py
Registro de ventas y reportes de recaudación.
usuarios.json
Usuarios y roles registrados.
turno_caja.json
Estado y saldos del turno de caja.
productos.json
Catálogo de productos e inventario (debe crearse).
ventas.json
Historial de ventas (se crea al registrar la primera venta).
Cómo ejecutar
Descargar o clonar el repositorio.
Abrir una terminal en la carpeta del proyecto.
Verificar que exista productos.json y que tenga productos con las claves que utiliza el programa.
Ejecutar:
python sistema_ventas.py
En algunos equipos puede ser necesario utilizar python3 en lugar de python.
Estructura esperada de productos.json
El catálogo debe ser una lista de objetos. Cada producto debe incluir ID, Nombre, Seccion, Precio y Stock. Por ejemplo:
[
    {
        "ID": "P001",
        "Nombre": "Leche",
        "Seccion": "Lacteos",
        "Precio": 1500.0,
        "Stock": 20
    },
    {
        "ID": "P002",
        "Nombre": "Queso",
        "Seccion": "Lacteos",
        "Precio": 3200.0,
        "Stock": 8
    }
]
Los nombres de las claves deben respetarse exactamente, incluyendo mayúsculas y minúsculas.
Usuarios de prueba
El archivo usuarios.json incluido contiene estas credenciales iniciales:
Usuario: nandiaz -- ibattelli -- agallarati -- vguarachi
Contraseña: 1234 --   4321    --    5678    --   8765
Rol: Administrador -- Cajero  --   Cajero   --  Cajero

Son credenciales de demostración. No deben utilizarse así en un sistema real: las contraseñas están guardadas en texto plano.
Estado y consideraciones
Esta versión es un proyecto académico y utiliza archivos JSON como almacenamiento local. Antes de ejecutar el flujo completo de ventas, hay que corregir algunos detalles pendientes del código, entre ellos la función abrir_json() que se importa desde ventas_y_cobros.py pero no está definida, y el flujo de confirmación y cobro dentro de menu_cajero().
También se debe revisar el filtrado del reporte mensual para que tenga en cuenta el mes y el año seleccionados, y validar que las cantidades ingresadas sean positivas.