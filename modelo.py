class ModeloUsuario:
    def __init__(self, conexion):
        self.connection = conexion

    def registrar_usuario(self, nombre_usuario, contrasena):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(
                    "INSERT INTO usuario (usuario, contraseña) VALUES (%s, %s)", 
                    (nombre_usuario, contrasena)
                )
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
            cursor.execute("SELECT contraseña FROM usuario WHERE usuario = %s", (nombre_usuario,))
            resultado = cursor.fetchone()
            if resultado and resultado[0] == contrasena:
                return True
        return False