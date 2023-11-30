import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Own104829*miguel',
    database = "bdpython"

)

cursor = conexion.cursor()

try:
    cursor.execute('CREATE TABLE usuarios (id int AUTO_INCREMENT PRIMARY KEY, nombre varchar(50), apellido varchar(50), edad int, email varchar(50))')
    print('Se creo correctamente la tabla')
except:
    print('Error al crear la tabla')

