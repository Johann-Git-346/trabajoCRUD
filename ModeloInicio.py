class ModeloUsuario:
    def __init__(self, conexion):
        self.connection = conexion
        self.informe=None
        self.session = {}

    def getInforme(self):
        return self.informe
    
    def setInforme(self,informe):
        self.informe=informe
        self.guardarInforme()

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

    def obtenerMasYMenosVendidos(self):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                # Obtener todos los productos ordenados por cantidad de ventas
                query = """
                SELECT * FROM productos
                ORDER BY cantidad DESC
                """
                cursor.execute(query)
                productos = cursor.fetchall()
                
                # Si no hay productos, retornar listas vacías
                if not productos:
                    return [], []
                
                # Encontrar el punto medio
                total_productos = len(productos)
                punto_medio_index = total_productos // 2
                
                # Dividir los productos en más vendidos y menos vendidos
                menos_vendidos = productos[punto_medio_index:]  # Productos con ventas menores
                mas_vendidos = productos[:punto_medio_index]    # Productos con ventas mayores o iguales
                
                return mas_vendidos, menos_vendidos
            except Exception as e:
                print(f"Error: {e}")
                return [], []

            
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

                cursor.execute("INSERT INTO usuario (email, password, Id_rol) VALUES (%s, %s, %s)", 
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
                JOIN rol r ON u.Id_rol = r.id
                WHERE u.email = %s AND u.password = %s
            """, (email, contrasena))
            resultado = cursor.fetchone()
            cursor.close()
            if resultado:
                self.session['usuario_id'] = resultado[0]
                return resultado[0]
        return None
    
    def obtener_usuario_id(self):
        return self.session.get('usuario_id')

    def comprar_producto(self, productos):
        for producto in productos:
            nombre=productos[0]
            cantidad_comprada=productos[1]

        producto = self.obtener_producto_por_nombre(nombre)
        if producto:
            cantidad_actual = producto[4]  # Asumiendo que la cantidad está en la columna 4
            if cantidad_actual >= cantidad_comprada:
                nueva_cantidad = cantidad_actual - cantidad_comprada
                if nueva_cantidad == 0:
                    self.eliminar_producto(nombre)
                else:
                    self.modificar_producto(nombre, nueva_cantidad=nueva_cantidad)
                return True
            else:
                print("No hay suficiente cantidad disponible.")
                return False
        else:
            print("Producto no encontrado.")
            return False
        
    def actualizar_cantidad_productos(self, productos):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                for producto in productos:
                    nombre, cantidad_seleccionada = producto[0], producto[1]
                    cursor.execute("SELECT cantidad FROM productos WHERE nombre = ?", (nombre,))
                    cantidad_actual = cursor.fetchone()[0]

                    if cantidad_actual >= cantidad_seleccionada:
                        nueva_cantidad = cantidad_actual - cantidad_seleccionada
                        cursor.execute("UPDATE productos SET cantidad = ? WHERE nombre = ?", (nueva_cantidad, nombre))
                    else:
                        print(f"No hay suficiente cantidad para el producto: {nombre}.")
                        return False
                
                self.connection.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error al actualizar la cantidad de productos: {e}")
                return False
        else:
            print("No hay conexión con la base de datos.")

    def imagenABaseDatos2(self, nombreProducto, imagenBinario):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                # Consulta para actualizar la imagen del producto basado en el nombre
                sql = "UPDATE productos SET imagenBinario = %s WHERE nombre = %s"
                valores = (imagenBinario, nombreProducto)
                cursor.execute(sql, valores)
                self.connection.commit()
                print("Imagen actualizada exitosamente en la base de datos")
            
            except Exception as e:
                print(f"Error al actualizar en la base de datos: {e}")
            finally:
                cursor.close()

    def agregar_producto(self, id, nombre, precio, categoria, cantidad):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                # Check if the product with the same ID already exists
                cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))
                if cursor.fetchone():
                    print(f"Error: Ya existe un producto con el ID {id}.")
                    return False

                # Insert the new product
                cursor.execute("INSERT INTO productos (id, nombre, precio, categoria, cantidad) VALUES (%s, %s, %s, %s, %s)",
                            (id, nombre, precio, categoria, cantidad))
                self.connection.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error al agregar producto: {e}")
                return False
        else:
            print("No hay conexión con la base de datos.")
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

    def modificar_producto(self, ID, nuevo_nombre=None, nuevo_precio=None, nueva_categoria=None, nueva_cantidad=None):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                sql = "UPDATE productos SET "
                params = []
                if nuevo_nombre:
                    sql += "nombre = %s, "
                    params.append(nuevo_nombre)
                if nuevo_precio is not None:
                    sql += "precio = %s, "
                    params.append(nuevo_precio)
                if nueva_categoria:
                    sql += "categoria = %s, "
                    params.append(nueva_categoria)
                if nueva_cantidad is not None:
                    sql += "cantidad = %s, "
                    params.append(nueva_cantidad)
                
                sql = sql.rstrip(", ") + " WHERE id = %s"
                params.append(ID)
                cursor.execute(sql, tuple(params))
                self.connection.commit()
            except Exception as e:
                print(f"Error al modificar producto: {e}")
                return []

    def eliminar_producto(self, id):
        if self.connection:
            cursor=self.connection.cursor()
            try:
                sql = "DELETE FROM productos WHERE Id = %s"
                cursor.execute(sql, (id,))
                self.connection.commit()

            except Exception as e:
                print(f"Error al eliminar producto: {e}")
                return False
            
    def realizar_pedido(self,productos_seleccionados):
        """ Realiza un pedido y actualiza el inventario para cada producto. """
        for producto in productos_seleccionados:
            id_producto = producto[0]  # Suponiendo que el ID del producto está en la primera posición
            cantidad_comprada = producto[4]  # La cantidad comprada está en la posición 4

            # Actualizar el inventario por cada producto
            self.actualizar_inventario(id_producto, cantidad_comprada)

        # Aquí puedes agregar más lógica para finalizar el pedido, como registrar el pedido en la base de datos
        print("Pedido realizado con éxito.")

    def actualizar_inventario(self, id_producto, cantidad_comprada):
        """ Actualiza el inventario de un producto tras realizar una compra. """
        if self.connection:
            cursor = self.connection.cursor()
            try:
                # Primero, obtener la cantidad actual del producto
                cursor.execute("SELECT cantidad FROM productos WHERE id = %s", (id_producto,))
                cantidad_actual = cursor.fetchone()[0]

                # Calcular la nueva cantidad después de la compra
                nueva_cantidad = cantidad_actual - cantidad_comprada

                # Evitar cantidades negativas
                if nueva_cantidad < 0:
                    nueva_cantidad = 0

                # Actualizar la cantidad en la base de datos
                cursor.execute("UPDATE productos SET cantidad = %s WHERE id = %s", (nueva_cantidad, id_producto))
                self.connection.commit()

            except Exception as e:
                print(f"Error al actualizar el inventario: {e}")
            finally:
                cursor.close()
            
    def guardarInforme(self):
        try:
            with open("informeProductos.txt", "w") as file:
                file.write(self.informe)
            print("Informe generado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el informe: {e}")