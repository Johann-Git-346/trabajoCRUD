class ModeloUsuario:
    def __init__(self, conexion):
        self.connection = conexion

    def registrar_usuario(self, email, contrasena, rol):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
                if cursor.fetchone():
                    cursor.close()
                    return False  # El correo ya está registrado

                # Asigna el rol según la selección del usuario
                rol_id = 1 if rol == 'Administrador' else (2 if rol == 'Vendedor' else 3) #<-- lo hice para ver si servia lo de la vista administrador
                #si va a usar el suyo no elimine el mio comentelo como yo estoy haciendo.
                # Y NO CREE OTRO ARCHIVO CON EL MISMO NOMBRE....
                #rol_id = 2 if rol == 'Vendedor' else 3  # 2 para Vendedor, 3 para Usuario <-- este es el suyo JULIAN

                cursor.execute("INSERT INTO usuario (email, password, rol_id) VALUES (%s, %s, %s)", 
                               (email, contrasena, rol_id))
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
            cursor.execute("""
                SELECT r.nombre FROM usuario u
                JOIN rol r ON u.rol_id = r.id
                WHERE u.email = %s AND u.password = %s
            """, (email, contrasena))
            resultado = cursor.fetchone()
            cursor.close()
            if resultado:
                return resultado[0]  # Devuelve el nombre del rol ('Administrador', 'Vendedor', 'Usuario')
        return None
