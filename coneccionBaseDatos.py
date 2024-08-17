import mysql.connector

class Crear_Conexion:
    @staticmethod
    def conexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Usuarios",
            )
            print("Conexión correcta")
            return conexion
        except mysql.connector.Error as e:
            print(f"Error en la conexión: {e}")
            return None

# Uso de la clase para obtener la conexión
conexion = Crear_Conexion.conexionBaseDeDatos()