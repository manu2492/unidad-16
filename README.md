# Creación de conector a PostgreSQL con SQLAlchemy
Se creó un ORM con SQLAlchemy para crear, borrar, actualizar y leer data de una tabla llamada 'customer'

## Instrucciones 
1. crear un entorno virtual e instalar las dependencias necesarias con el archivo requirements.txt
```
python3 -m venv venv
```
```
pip install -r requirements.txt
```
2. Configurar la conexión a la base de datos PostgreSQL. Crea un archivo `.env` en la raíz del proyecto. Dentro deberás crear las siguientes 3 variables, los nombres deben respetarse ya que se usan en el archivo `config.py` para crear la conexión a la base de datos.
```
USUARIO= your_user
PASS= your_password
DB_NAME= your_db_name
```
