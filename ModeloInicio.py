class ModeloUsuario:
    def __init__(self, conexion):
        self.connection = conexion

    def registrar_usuario(self, email, contrasena):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    cursor.close()
                    return False  # El correo ya está registrado
                
                cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", 
                               (email, contrasena))
                self.connection.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error al registrar usuario: {e}")
                return False
        else:
            print("No hay conexión con la base de datos.")
            return False

    def autenticar_usuario(self, email, contrasena):
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
            resultado = cursor.fetchone()
            cursor.close()
            if resultado and resultado[0] == contrasena:
                return True
        return False
