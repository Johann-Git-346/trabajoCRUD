import mysql.connector

class ProductoModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inicio"
        )
        self.cursor = self.conn.cursor()

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def obtener_producto_por_nombre(self, nombre):
        sql = "SELECT * FROM productos WHERE nombre = %s"
        self.cursor.execute(sql, (nombre,))
        return self.cursor.fetchone()

    def agregar_producto(self, nombre, precio, descripcion, cantidad):
        sql = "INSERT INTO productos (nombre, precio, descripcion, cantidad) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nombre, precio, descripcion, cantidad))
        self.conn.commit()

    def modificar_producto(self, nombre, nuevo_precio=None, nueva_descripcion=None, nueva_cantidad=None):
        sql = "UPDATE productos SET "
        params = []
        if nuevo_precio is not None:
            sql += "precio = %s, "
            params.append(nuevo_precio)
        if nueva_descripcion:
            sql += "descripcion = %s, "
            params.append(nueva_descripcion)
        if nueva_cantidad is not None:
            sql += "cantidad = %s, "
            params.append(nueva_cantidad)
        
        sql = sql.rstrip(", ") + " WHERE nombre = %s"
        params.append(nombre)
        self.cursor.execute(sql, tuple(params))
        self.conn.commit()

    def eliminar_producto(self, nombre):
        sql = "DELETE FROM productos WHERE nombre = %s"
        self.cursor.execute(sql, (nombre,))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
