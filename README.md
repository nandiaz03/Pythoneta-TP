Presentacion: file:///C:/Users/Usuario/Downloads/reveal.js-master/index.html#/6
UX: https://www.canva.com/design/DAHUMTJZIlA/8wZYhnJ_cXjczNtzVDa7zg/edit

# Vaythoneta - Sistema de gestión de ventas

Proyecto desarrollado en Python para administrar el stock de productos y registrar ventas de un comercio pequeño. La información se almacena en archivos JSON.

## Funcionalidades

- Inicio de sesión con usuarios y roles.
- Menú de administración para consultar, agregar y descontar stock.
- Menú de caja para cargar productos al carrito, calcular descuentos, cobrar y emitir tickets.
- Registro de apertura y cierre de caja.
- Registro de ventas y consulta de reportes diarios y mensuales.

## Requisitos

- Python 3.10 o superior (el código utiliza anotaciones de tipo como `float | None`).
- Opcional: `colorama` para ver los colores en la consola (`pip install colorama`). Si no está instalado, el programa funciona igual, sin colores.

## Archivos del proyecto

| Archivo | Responsabilidad |
|---|---|
| `sistema_ventas.py` | Punto de entrada y menús principales. |
| `archivos.py` | Lectura/escritura de JSON y rutas de los archivos de datos. |
| `funciones/autenticacion_roles.py` | Usuarios, autenticación, roles y operaciones de caja. |
| `funciones/stock.py` | Consulta y modificación del inventario. |
| `funciones/ventas_y_cobros.py` | Carrito, métodos de pago, cálculos y emisión de tickets. |
| `funciones/reportes.py` | Registro de ventas y reportes de recaudación. |
| `data/usuarios.json` | Usuarios y roles registrados. |
| `data/turno_caja.json` | Estado y saldos del turno de caja. |
| `data/productos.json` | Catálogo de productos e inventario. |
| `data/ventas.json` | Historial de ventas. |

## Cómo ejecutar

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Verificar que exista `data/productos.json` y que tenga productos con las claves que utiliza el programa.
4. Ejecutar:

```bash
python sistema_ventas.py
```

Se puede ejecutar desde cualquier carpeta: las rutas de los datos se calculan a partir de la ubicación del proyecto.

En algunos equipos puede ser necesario utilizar `python3` en lugar de `python`.

## Estructura esperada de productos.json

El catálogo debe ser una lista de objetos. Cada producto debe incluir `ID`, `Nombre`, `Seccion`, `Precio` y `Stock`. Por ejemplo:

```json
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
```

Los nombres de las claves deben respetarse exactamente, incluyendo mayúsculas y minúsculas.

## Usuarios de prueba

El archivo `usuarios.json` incluido contiene estas credenciales iniciales:

| Usuario | Contraseña | Rol |
|---|---|---|
| `nandiaz` | `1234` | Administrador |
| `ibattelli` | `4321` | Cajero |
| `agallarati` | `5678` | Cajero |
| `vguarachi` | `8765` | Cajero |

Son credenciales de demostración. No deben utilizarse así en un sistema real: las contraseñas están guardadas en texto plano.

## Estado y consideraciones

Esta versión es un proyecto académico y utiliza archivos JSON como almacenamiento local. El flujo completo (login, stock, venta con descuento y ticket, apertura/cierre de caja y reportes) fue probado de punta a punta.
