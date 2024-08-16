from aifc import Error
import hashlib
from BaseInicio import Crear_Conexion

class ModeloUsuario:
    def __init__(self, conexion):
        self.connection = conexion

    def registrar_usuario(self, nombre_usuario, contrasena):
        if self.connection:
            cursor = self.connection.cursor()
            contrasena_hash = self.hashear_contrasena(contrasena)
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (nombre_usuario, contrasena_hash))
                self.connection.commit()
                return True
            except Exception as e:
                print(f"Error al registrar usuario: {e}")
                return False
        else:
            return False

    def autenticar_usuario(self, nombre_usuario, contrasena):
        if self.connection:
            cursor = self.connection.cursor()
            contrasena_hash = self.hashear_contrasena(contrasena)
            cursor.execute("SELECT password FROM users WHERE username = %s", (nombre_usuario,))
            resultado = cursor.fetchone()
            if resultado and resultado[0] == contrasena_hash:
                return True
        return False

    def hashear_contrasena(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
