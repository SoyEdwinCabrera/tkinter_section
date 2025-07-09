# Tkinter Project: GUI and Database Integration

Este proyecto combina el uso de **Tkinter** para crear interfaces gráficas de usuario (GUIs) y bases de datos (SQLite y PostgreSQL) para almacenar y gestionar datos. A continuación, se detalla la funcionalidad de cada archivo, las dependencias necesarias y los pasos para replicar el proyecto.

---

## Archivos del Proyecto

### 1. `exercise_km.py`
Este archivo crea una interfaz gráfica con Tkinter que convierte un valor en kilogramos a gramos, libras y onzas. Incluye:
- Entrada de datos (en kilogramos).
- Botón para realizar la conversión.
- Tres cuadros de texto para mostrar los resultados.

### 2. `script1.py`
Este archivo implementa una GUI simple que convierte kilómetros a millas. Incluye:
- Entrada de datos (en kilómetros).
- Botón para realizar la conversión.
- Cuadro de texto para mostrar el resultado.

### 3. `sqlite.py`
Este archivo utiliza SQLite para gestionar una base de datos local. Las funciones incluidas son:
- Crear una tabla llamada `store`.
- Insertar datos en la tabla.
- Ver todos los registros.
- Actualizar registros existentes.
- Eliminar registros.

### 4. `psql.py`
Este archivo utiliza PostgreSQL para gestionar una base de datos remota. Las funciones incluidas son similares a las de `sqlite.py`:
- Crear una tabla llamada `store`.
- Insertar datos en la tabla.
- Ver todos los registros.
- Actualizar registros existentes.
- Eliminar registros.


---

## Dependencias

Para replicar este proyecto, asegúrate de instalar las siguientes dependencias:

### 1. Python
El proyecto está desarrollado en **Python 3.12.1**. Asegúrate de tenerlo instalado en tu sistema.

### 2. Tkinter
Tkinter es un módulo estándar de Python para crear GUIs. No requiere instalación adicional si tienes Python instalado.

### 3. SQLite
SQLite es una base de datos ligera integrada en Python. No requiere instalación adicional.

### 4. PostgreSQL
Para usar PostgreSQL, necesitas instalar:
- **PostgreSQL**: [Descargar aquí](https://www.postgresql.org/download/)
- **psycopg2**: Un adaptador para conectar Python con PostgreSQL. Instálalo con:
  ```bash
  pip install psycopg2
  
Pasos para Replicar el Proyecto

1. **Clonar el Repositorio**
   Clona este proyecto en tu máquina local:
   ```bash
   git clone https://github.com/SoyEdwinCabrera/tkinter_section.git
   cd tkinter_section
   ```

2. **Configurar PostgreSQL**
   - Asegúrate de que PostgreSQL esté instalado y en ejecución.
   - Crea una base de datos llamada `database1`.
   - Actualiza las credenciales en `psql.py` con tu usuario y contraseña.

3. **Instalar Dependencias**
   Ejecuta el siguiente comando para instalar las dependencias necesarias:
   ```bash
   pip install psycopg2
   ```

4. **Ejecutar los Archivos**
   - Para probar las GUIs, ejecuta `exercise_km.py` o `script1.py`:
     ```bash
     python exercise_km.py
     ```
     ```bash
     python script1.py
     ```
   - Para interactuar con las bases de datos, ejecuta `sqlite.py` o `psql.py`:
     ```bash
     python sqlite.py
     ```
     ```bash
     python psql.py
     ```

---

## Notas Adicionales

- **Seguridad**: No compartas el archivo `database_credentials.txt` públicamente, ya que contiene información sensible.
- **Extensibilidad**: Puedes modificar las funciones en `sqlite.py` y `psql.py` para adaptarlas a tus necesidades específicas.
- **Compatibilidad**: Este proyecto es compatible con sistemas operativos Windows, macOS y Linux.