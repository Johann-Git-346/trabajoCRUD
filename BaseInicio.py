import mysql.connector

class Crear_Conexion:
    @staticmethod
    def conexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="principal"
            )
            print("Conexión correcta")
            return conexion
        except mysql.connector.Error as e:
            print(f"Error en la conexión: {e}")
            return None
