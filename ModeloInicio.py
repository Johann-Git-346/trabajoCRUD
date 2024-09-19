class ModeloUsuario:
    def __init__(self, conexion):
        self.connection = conexion

    def obtener_productos(self):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute("SELECT * FROM productos")
                productos=cursor.fetchall()
                return productos
            
            except Exception as e:
                print(f"Error al obtener producto: {e}")
                return []

            
    def obtenerMasVendidos(self):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                query = """
                SELECT * FROM productos
                ORDER BY cantidad DESC
                LIMIT 5
                """
                cursor.execute(query)
                mas_vendidos = cursor.fetchall()
                return mas_vendidos
            except Exception as e:
                print(f"Error: {e}")
                return []
    
    def obtenerMenosVendidos(self):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                query = """
                SELECT * FROM productos
                ORDER BY cantidad ASC
                LIMIT 5
                """
                cursor.execute(query)
                menos_vendidos = cursor.fetchall()
                return menos_vendidos
            except Exception as e:
                print(f"Error: {e}")
                return []
            
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
    
    def imagenABaseDatos(self, nombreProducto, imagen):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                # Consulta para actualizar la imagen del producto basado en el nombre
                sql = "UPDATE productos SET imagenes = %s WHERE nombre = %s"
                valores = (imagen, nombreProducto)
                cursor.execute(sql, valores)
                self.connection.commit()
                print("Imagen actualizada exitosamente en la base de datos")
            
            except Exception as e:
                print(f"Error al actualizar en la base de datos: {e}")
            finally:
                cursor.close()

    def agregar_producto(self,nombre,precio,categoria,cantidad):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                cursor.execute("INSERT INTO productos (nombre, precio, categoria, cantidad) VALUES (%s, %s, %s, %s)",
                                (nombre,precio,categoria,cantidad))
                self.connection.commit()

            except Exception as e:
                print(f"Error al agregar producto: {e}")
                return False
            
    def obtener_producto_por_nombre(self, nombre):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                sql = "SELECT * FROM productos WHERE nombre = %s"
                cursor.execute(sql, (nombre,))
                return cursor.fetchone()
            except Exception as e:
                print(f"Error al obtener producto: {e}")
                return []

    def modificar_producto(self, nombre, nuevo_precio=None, nueva_categoria=None, nueva_cantidad=None):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                sql = "UPDATE productos SET "
                params = []
                if nuevo_precio is not None:
                    sql += "precio = %s, "
                    params.append(nuevo_precio)
                if nueva_categoria:
                    sql += "categoria = %s, "
                    params.append(nueva_categoria)
                if nueva_cantidad is not None:
                    sql += "cantidad = %s, "
                    params.append(nueva_cantidad)
                
                sql = sql.rstrip(", ") + " WHERE nombre = %s"
                params.append(nombre)
                cursor.execute(sql, tuple(params))
                self.connection.commit()
            except Exception as e:
                print(f"Error al obtener producto: {e}")
                return []

    def eliminar_producto(self, nombre):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                sql = "DELETE FROM productos WHERE nombre = %s"
                cursor.execute(sql, (nombre,))
                self.connection.commit()

            except Exception as e:
                print(f"Error al eliminar producto: {e}")
                return False