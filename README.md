# ejemplo-orm-tipos

## 

1. Realizar un Fork del repositorio

2. Clonar su Fork
```
git clone https://github.com/SU-USUARIO/ejemplo-orm-tipos.git
cd ejemplo-orm-tipos
```
3. Usar un entorno virtual para la ejecución de Python

4. Con el entorno activado usar pip install -r app/requirements.txt para instalar las librerías necesarias

5. Crear carpetas de persistencia de información de las bases de datos

* Linux/macOS:

    ```
    mkdir -p data/postgres
    mkdir -p data/mariadb
    mkdir -p data/sqlite
    ```
* Windows PowerShell:

    ```
    mkdir data\postgres
    mkdir data\mariadb
    mkdir data\sqlite
    ```

6. Levantar contenedores

```
docker compose up -d
```

7. Ejecutar los scripts de Python de la carpeta app, en el siguiente orden

* Verificar a que base de datos se está conectador, por intermedio de la variable enlace del archivo config.py
* Ejecutar modelo.py (verificar en la base de datos que exista la tabla)
* Ejecutar ingresar_datos.py (verificar que la tabla en la base de datos tenga información)
* Ejecutar consultar_datos.py (verificar la información de salida correspondiente)
