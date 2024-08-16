import mysql.connector

class Crear_Conexion:
    @staticmethod
    def conexion_base_de_datos(host, user, password, database):
        try:
            conexion = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
            )
            print("Conexión correcta")
            return conexion
        except mysql.connector.Error as e:
            print("Error en la conexión: {}".format(e))
            return None
