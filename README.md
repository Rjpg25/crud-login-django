# Inventario Django: CRUD con login

![Python 3.14](https://img.shields.io/badge/Python-3.14-blue)
![Django 5.2.17](https://img.shields.io/badge/Django-5.2.17-092E20)
![Estado: demostración funcional](https://img.shields.io/badge/Estado-Demostraci%C3%B3n%20funcional-green)

## Índice

- [Descripción del proyecto](#descripción-del-proyecto)
- [Estado del proyecto](#estado-del-proyecto)
- [Funcionalidades y demostración](#funcionalidades-y-demostración)
- [Acceso e instalación](#acceso-e-instalación)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Organización y patrón MVC](#organización-y-patrón-mvc)
- [Comprobación del acceso protegido](#comprobación-del-acceso-protegido)
- [Autor](#autor)

## Descripción del proyecto

Aplicación web de inventario desarrollada para demostrar las operaciones CRUD (crear, leer, actualizar y eliminar) y la autenticación de usuarios. Cada persona inicia sesión para administrar sus propios productos.

El proyecto utiliza Django para la lógica y los datos, Bootstrap para la interfaz y SQLite como base de datos local.

## Estado del proyecto

El login y las cuatro operaciones CRUD funcionan en el entorno local. La demostración en video se agregará antes de la entrega.

## Funcionalidades y demostración

- **Crear:** registrar un producto con nombre, cantidad y descripción.
- **Leer:** consultar los productos del usuario autenticado.
- **Actualizar:** modificar un producto propio.
- **Eliminar:** confirmar y borrar un producto propio.
- **Autenticación:** iniciar y cerrar sesión.
- **Acceso protegido:** solicitar el login al abrir una URL del inventario sin sesión.

**Video de demostración:** [Ver en YouTube](https://youtu.be/cepbhVJGWic) (2 min 55 s).

## Acceso e instalación

El código se puede descargar desde este repositorio mediante el botón **Code** de GitHub. Para ejecutarlo en Windows, instala Python y abre PowerShell en la carpeta del proyecto.

### 1. Crear el entorno e instalar dependencias

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Crear la configuración local

```powershell
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia la clave generada y pégala en `.env` después de `DJANGO_SECRET_KEY=`. El archivo `.env` contiene una clave local y está excluido de Git.

### 3. Preparar la base de datos y crear un usuario

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
```

### 4. Ejecutar la aplicación

```powershell
.\.venv\Scripts\python.exe manage.py runserver --noreload
```

Abre `http://127.0.0.1:8000/` en el navegador. Para detener el servidor, pulsa `Ctrl+C` en su terminal.

## Tecnologías utilizadas

| Tecnología | Uso |
| --- | --- |
| Python 3.14 | Lenguaje de programación. |
| Django 5.2.17 | Aplicación web, formularios y autenticación. |
| Bootstrap | Estilos de la interfaz. |
| SQLite | Almacenamiento local de usuarios y productos. |
| Git y GitHub | Control de versiones y publicación del código. |

## Organización y patrón MVC

Django organiza sus aplicaciones con el patrón **MVT** (Modelo, Vista y Plantilla). Esta estructura separa los datos, el procesamiento de solicitudes y la presentación, que es el objetivo arquitectónico de MVC.

| Archivo o carpeta | Responsabilidad |
| --- | --- |
| `productos/models.py` | Define el modelo `Producto` y su propietario. |
| `productos/forms.py` | Define los campos del formulario. |
| `productos/views.py` | Procesa las operaciones CRUD y comprueba el usuario. |
| `productos/templates/` | Presenta las páginas HTML. |
| `productos/urls.py` | Relaciona las URL del inventario con sus vistas. |
| `config/urls.py` | Define las rutas generales, incluido el login. |
| `productos/migrations/` | Conserva los cambios de estructura de la base de datos. |

## Comprobación del acceso protegido

Las vistas del CRUD utilizan `@login_required`. Para editar o eliminar también se busca el producto por su identificador y por el usuario que inició sesión.

Prueba manual:

1. Abre `http://127.0.0.1:8000/productos/` en una ventana de incógnito. Debe aparecer el login.
2. Inicia sesión y crea un producto.
3. Edita el producto y comprueba el cambio en el listado.
4. Elimínalo y comprueba que desaparece.
5. Cierra sesión e intenta abrir directamente `/productos/nuevo/`. Debe solicitar el login.

También puedes comprobar la configuración con:

```powershell
.\.venv\Scripts\python.exe manage.py check
```

## Autor

Ricardo Piñango — estudiante de Ingeniería en Software, Universidad de las Américas (UDLA).